import openai
from flask import Flask, request
import prompts
from db_model import db, JobOpening, InterviewSession, Message
from playhouse.shortcuts import model_to_dict

app = Flask(__name__, static_folder='static', static_url_path='/')

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.before_request
def _db_connect():
    db.connect()

@app.teardown_request
def _db_close(exc):
    if not db.is_closed():
        db.close()

def get_previous_messages(session):
  previous_messages = []
  messages = Message.select().where(Message.session == session).order_by(Message.order)
  for message in messages:
    previous_messages.append({ "role" : message.role, "content": message.content })
  return previous_messages


@app.route('/api/chat/<token>', methods = ['POST'])
def chat_completion(token):
  session = InterviewSession.get_or_none(InterviewSession.token == token)
  if not session:
    return None
  previous_messages = get_previous_messages(session)

  message = request.json
  print(message)
  if not message and len(previous_messages) > 2:
    return previous_messages[2:]

  if message:
    previous_messages.append(message)
  
  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", 
    messages=previous_messages
  )
  print(completion)
  response = completion["choices"][0]["message"]
  if message:
    Message.create(order=len(previous_messages)+1, role = message["role"], content=message["content"], session=session)
  Message.create(order=len(previous_messages)+2, role = response["role"], content=response["content"], session=session)
  return response

@app.route('/api/evaluate/<token>', methods = ['POST'])
def chat_evaluate(token):
  session = InterviewSession.get_or_none(InterviewSession.token == token)
  if not session:
    return None
  previous_messages = get_previous_messages(session)
  
  previous_messages.append({"role": "system", "content": prompts.evaluate_prompt})
  completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo", 
    messages=previous_messages
  )

  return completion["choices"][0]["message"]

@app.route('/api/openings', methods = ['GET'])
def get_openings():
  openings = []
  for opening in JobOpening.select():
    openings.append(model_to_dict(opening))
  return openings 

@app.route('/api/new_session', methods = ['POST'])
def create_session():
  name = request.json.get("name")
  opening_id = request.json.get("openingId")

  opening = JobOpening.get_by_id(opening_id)
  session = InterviewSession.create(candidate_name=name, job_opening=opening_id)

  Message.create(order=1, role="system", content=prompts.system_prompt(opening.description), session=session)
  Message.create(order=2, role="user", content=prompts.user_welcome(name), session=session)

  return { "token": str(session.token) } 
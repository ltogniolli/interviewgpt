import os
from playhouse.db_url import connect
import uuid
from peewee import *

database_url = os.environ['DATABASE_URL']

db = connect(database_url)
db.close()

class BaseModel(Model):
    class Meta:
        database = db

class JobOpening(BaseModel):
    description = CharField()

class InterviewSession(BaseModel):
    token = UUIDField(default=uuid.uuid4)
    candidate_name = CharField()
    job_opening = ForeignKeyField(JobOpening)

class Message(BaseModel):
    order = IntegerField()
    role = CharField()
    content = TextField()
    session = ForeignKeyField(InterviewSession)

if not JobOpening.table_exists():
    db.create_tables([JobOpening, InterviewSession, Message])
    JobOpening.create(description="Java e ReactJS")
    JobOpening.create(description=".Net Core no Linux")
    JobOpening.create(description="Javascript full stack")
    JobOpening.create(description="Testes Automatizados")
### setup
```
set OPENAI_API_KEY=...
set DATABASE_URL=postgres://...
cd interview_frontend
npm install
cd interview_backend
pip install -r requirements.txt
```

### development
```
cd interview_frontend
npm run serve
```

```
cd interview_backend
flask run --debug
open http://localhost:8080
```

### deployment
```
cd interview_frontend
npm run build
cd interview_backend
fly deploy
```
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to Professional Cloud App"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/api/message")
def message():
    return {"message": "Hello from cloud app!"}


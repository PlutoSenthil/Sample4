import uvicorn
from fastapi import FastAPI
import os

# load environment variables
port = os.environ["PORT"]

# initialize FastAPI
app = FastAPI()

@app.get("/")
def index():
    return {"data": "Application ran successfully - FastAPI"}
  
@app.get("/test")
def index1():
    return {"data": "Dynamic Output"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)

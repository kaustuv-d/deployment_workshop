#pip install fastapi
#pip install uvicorn
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/')
def root_api():
    return{"message": "AI Winter is Coming"}

if __name__ == "__main__":
    uvicorn.run(app, port=8000, host="127.0.0.1")

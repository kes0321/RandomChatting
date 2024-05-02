from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

from fastapi.responses import FileResponse
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def abc():
    return 'hello'

@app.get("/data")
def abc():
    return {'hello': 1234}


from pydantic import BaseModel
class Model(BaseModel):
    message :str

@app.post("/send")
def abc(data : Model):
    if data.message == "/날씨":
        return "맑을까?"
    return data


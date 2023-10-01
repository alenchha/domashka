import wikipedia
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from pydantic import BaseModel

class QueryBody(BaseModel):
    query: str
class Response(BaseModel):
    result: str

wikipedia.set_lang("ru")

app = FastAPI()

@app.post("/", response_model=Response)
def create_request(req: QueryBody):
    res = "Резюме из body: \n "
    res += wikipedia.summary(req.query)
    return Response(result=res)

@app.get("/{path}")
def fun1(path: str):
    res = "Резюме из path: \n "
    res += wikipedia.summary(path)
    return PlainTextResponse(res)

@app.get("/")
def fun2(query: str):
    res = "Резюме из query: \n "
    res += wikipedia.summary(query)
    return PlainTextResponse(res)

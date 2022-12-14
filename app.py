from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from utils import convert_json_to_yaml

app = FastAPI()
templates = Jinja2Templates(directory="templates/")

@app.get("/")
def read_form():
    return "hello world"

@app.get("/form")
def form_post(request: Request):
    result =  "Type a text"
    return templates.TemplateResponse('form.html',context={'request': request, 'result': result})

@app.post("/form")
def form_post(request: Request,fname: str = Form(...)):
    result = convert_json_to_yaml(fname)
    return templates.TemplateResponse('form.html',context={"request":request, 'result': result})
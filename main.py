from urllib import request

from test import Url_FromUser
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import random

app = FastAPI()
templates = Jinja2Templates(directory='templates')
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    list_id_games = [10, 570, 620, 730, 242760]
    r = random.choice(list_id_games)
    return templates.TemplateResponse("test_main.html", {"request": request, "r" : r})
@app.post("/url_background")
async def url_background(url: Url_FromUser):
    return {'text':url,'response':'ok'}
@app.get("/change_background", response_class=HTMLResponse)
async def change_background(request: Request, text: str):
    return templates.TemplateResponse("hash_storage.html", {
        "request": request,
        "text": text
    })

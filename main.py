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
    list_id_games = [10, 570, 620, 730]
    r = random.choice(list_id_games)
    return templates.TemplateResponse("test_main.html", {"request": request, "r" : r})
@app.get("/change_background", response_class=HTMLResponse)
async def change_background():
    with open('templates/change_background.html', 'r', encoding='utf-8') as f:
        h=f.read()
    return HTMLResponse(content=h,status_code=200)
from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from hash import create_hash
from database import Database
from md import md2html
from logging_config import config

import os


config
LINK = os.getenv('DATABASE_URL')
app = FastAPI()
db = Database(LINK)
templates = Jinja2Templates(directory='src/templates')
app.mount('/static', StaticFiles(directory='src/static'), name='static')

@app.get('/', response_class=RedirectResponse)
async def start(request : Request):
    link = create_hash()
    return RedirectResponse(f'/{link}', status_code=302)

@app.get('/{link}', response_class=HTMLResponse)
async def start1(request: Request, link: str):
    linkk = db.select_data(hash=link)
    if linkk != None:
        text = md2html(linkk[1])
        return templates.TemplateResponse(request, 'text.html', context={'text': text, "link": linkk[0]})
    else:
        return templates.TemplateResponse(request, 'index.html')

@app.post('/{link}')
async def post(text: str = Form(...), link: str = str):
    db = Database(LINK)
    
    db.insert_data(hash=link, text=text)
    return RedirectResponse(f'/{link}', status_code=302)
    


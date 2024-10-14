from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

users = []

@app.get("/users", response_class=HTMLResponse)
async def Llistat(request: Request):
    return templates.TemplateResponse("item.html", {"request": request, "users": users})


@app.get("/users/{username}", response_class=HTMLResponse)
async def Detalls_Usuari(request: Request, username: str):
    
    return templates.TemplateResponse("user_detail.html", {"request": request, "username": username})

@app.post("/add-user", response_class=HTMLResponse)
async def agregar_usuari(request: Request, username: str = Form(...)):
    users.append(username)
    return templates.TemplateResponse("item.html", {"request": request, "users": users})


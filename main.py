from fastapi import FastAPI, Request
from API.routes import receta_routes
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="templates")
app.mount("/assets", StaticFiles(directory="static/assets"), name="assets")
app.mount("/vendor", StaticFiles(directory="static/vendor"), name="vendor")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("recetas/details.html", {"request": request})

app.include_router(receta_routes.router)


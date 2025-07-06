from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from broker.rabbit import broker
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="app/static")

@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@router.get("/health")
async def health_check():
    return {"status": "healthy", "service": "notificate-api"}


@router.post("/order")
async def make_order(name: str):
    await broker.publish_order(f"Новый заказ: {name}")
    return {"data": "OK"}

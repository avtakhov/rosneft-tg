from fastapi import APIRouter

from routes import telegram

router = APIRouter()
router.include_router(telegram.router)

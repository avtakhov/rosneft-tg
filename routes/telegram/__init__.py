from fastapi import APIRouter

from routes.telegram import updates

router = APIRouter(prefix='/telegram')
router.include_router(updates.router)

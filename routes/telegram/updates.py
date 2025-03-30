import logging
import typing
from http import HTTPStatus

import fastapi
from telegram import Update

from models.application import application
from settings import settings

router = fastapi.APIRouter()


@router.post('/updates')
async def process_update(
        request: fastapi.Request,
        x_telegram_bot_api_secret_token: typing.Annotated[str, fastapi.Header()],
):
    if settings.telegram_updates_secret_token != x_telegram_bot_api_secret_token:
        return fastapi.responses.Response(status_code=HTTPStatus.UNAUTHORIZED)

    logging.info('Received update')
    await application.process_update(
        Update.de_json(await request.json(), application.bot)
    )
    return fastapi.Response(status_code=200)

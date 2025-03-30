from telegram.ext import Application, ApplicationBuilder

from settings import settings

application: Application = (
    ApplicationBuilder()
    .token(settings.telegram_token)
    .base_url(settings.telegram_api_base_url)
    .build()
)

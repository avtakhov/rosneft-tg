import contextlib

from fastapi import FastAPI

from models.application import application
from routes import router
from utils.command_handler import command_handlers
from utils.callback_handler import callback_query_handlers
from utils.text_handler import text_handlers
from views.telegram.command import *
from views.telegram.callback import *
from views.telegram.text import *


@contextlib.asynccontextmanager
async def lifespan(_: FastAPI):
    async with application:
        await application.start()
        yield
        await application.stop()


# app = FastAPI(lifespan=lifespan)
# app.include_router(router)

application.add_handlers(
    command_handlers + callback_query_handlers + text_handlers,
)

application.run_polling()

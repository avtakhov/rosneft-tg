import functools
import itertools
import typing

from telegram import Update
from telegram.ext import ContextTypes, MessageHandler
from telegram.ext.filters import *

text_handlers = []


def text_handler(
    text_regex: str,
):
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(update: Update, context: ContextTypes.DEFAULT_TYPE):
            await func(
                update,
                context,
            )

        text_handlers.append(
            MessageHandler(filters=Regex(text_regex), callback=wrapper, block=False),
        )
        return wrapper

    return decorator

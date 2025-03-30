import functools
import itertools
import typing

from telegram import Update
from telegram.ext import CallbackContext, CommandHandler, ContextTypes

command_handlers = []


def command_handler(
        command: str,
        types: tuple[typing.Type, ...] = (),
):
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(update: Update, context: ContextTypes.DEFAULT_TYPE):
            await func(
                update,
                context,
                *(
                    t(i) if t else i
                    for t, i in itertools.zip_longest(types, context.args)
                )
            )

        command_handlers.append(
            CommandHandler(command=command, callback=wrapper, has_args=len(types), block=False),
        )
        return wrapper

    return decorator

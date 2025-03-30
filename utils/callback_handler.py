import functools
import itertools
import re
import typing

from telegram import Update
from telegram.ext import CallbackContext, CallbackQueryHandler

callback_query_handlers = []


def callback_handler(
        regex: str,
        types: tuple[typing.Type, ...] = (),
):
    compiled_regex: re.Pattern = re.compile(regex)

    def decorator(func):
        @functools.wraps(func)
        async def wrapper(update: Update, context: CallbackContext):
            groups = re.match(compiled_regex, update.callback_query.data).groups()
            await func(
                update,
                context,
                *(
                    t(i) if t else i
                    for t, i in itertools.zip_longest(types, groups)
                )
            )

        callback_query_handlers.append(
            CallbackQueryHandler(wrapper, pattern=compiled_regex.pattern, block=False),
        )
        return wrapper

    return decorator

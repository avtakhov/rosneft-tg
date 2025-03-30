from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ContextTypes

from models import messages
from models.user import users_db, User
from utils.command_handler import command_handler

_greeting_message = f'''Привет, бот поможет сделать обращение'''

_keyboard = [
    [KeyboardButton(messages.CREATE_NEW_TICKET), ],
]


@command_handler('start')
async def start(update: Update, _: ContextTypes.DEFAULT_TYPE) -> None:
    if users_db.get(update.effective_user.id) is None:
        users_db[update.effective_user.id] = User()

    await update.message.reply_text(
        text=_greeting_message,
        reply_markup=ReplyKeyboardMarkup(_keyboard)
    )

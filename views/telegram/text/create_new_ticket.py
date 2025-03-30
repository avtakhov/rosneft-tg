import datetime

from telegram import Update, ForceReply
from telegram.ext import ContextTypes

from models import messages
from models.user import users_db, User, WaitingForTicket
from utils.text_handler import text_handler


@text_handler(messages.CREATE_NEW_TICKET)
async def handle(update: Update, _: ContextTypes.DEFAULT_TYPE):
    users_db.setdefault(update.effective_user.id, User())
    users_db[update.effective_user.id].status = WaitingForTicket(
        from_chat=update.effective_chat.id,
        wait_until=datetime.datetime.now() + datetime.timedelta(minutes=20),
    )

    await update.message.reply_text(
        text='В следующем сообщении опишите свою проблему 📝',
        reply_markup=ForceReply(),
    )

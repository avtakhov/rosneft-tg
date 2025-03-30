from telegram import Update
from telegram.ext import ContextTypes

from models.user import TicketStatus, users_db
from settings import settings
from utils.callback_handler import callback_handler
from views.admin_chat.notify import notify_admins, notify_user


@callback_handler(r'/status/(\d+)/(\w+)/(\w+)', types=(int, str, str))
async def handle(
    update: Update,
    _: ContextTypes.DEFAULT_TYPE,
    telegram_user_id: int,
    ticket_id: str,
    new_status: TicketStatus,
):
    if update.effective_chat.id != settings.admin_chat_id:
        return

    for ticket in users_db[telegram_user_id].tickets:
        if ticket.ticket_id == ticket_id:
            ticket.ticket_status = new_status
            await update.callback_query.delete_message()
            await notify_admins(telegram_user_id, ticket)
            await notify_user(ticket)

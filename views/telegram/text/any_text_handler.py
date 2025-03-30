import uuid

from telegram import Update
from telegram.ext import ContextTypes

from models import messages
from models.user import User, users_db, Ticket, WaitingForTicket, Default
from utils.text_handler import text_handler
from views.admin_chat.notify import notify_admins


@text_handler(rf'^(?!{messages.CREATE_NEW_TICKET}$).*')
async def handle(update: Update, _: ContextTypes.DEFAULT_TYPE):
    users_db.setdefault(update.effective_user.id, User())
    user = users_db[update.effective_user.id]
    match user.status:
        case WaitingForTicket(from_chat=update.effective_chat.id):
            user.status = Default()
            ticket = Ticket(
                from_user=update.effective_user.username,
                from_chat=update.effective_chat.id,
                ticket_id=uuid.uuid4().hex,
                ticket_status='New',
                user_request=update.message.text,
            )
            user.tickets.append(ticket)
            await update.message.reply_text(
                f'Зарегистрировано обращение {ticket.ticket_id}\n'
                f'Статус {ticket.ticket_status}'
            )
            await notify_admins(update.effective_user.id, ticket)
        case _:
            return

from telegram import InlineKeyboardMarkup, InlineKeyboardButton

from models.application import application
from models.user import Ticket
from settings import settings


async def notify_admins(telegram_user_id: int, ticket: Ticket):
    buttons = [
        InlineKeyboardButton(
            text=f'📍 {status}' if ticket.ticket_status == status else status,
            callback_data=f'/status/{telegram_user_id}/{ticket.ticket_id}/{status}',
        )
        for status in ['New', 'InProgress', 'Done', 'Cancelled']
    ]

    await application.bot.send_message(
        chat_id=settings.admin_chat_id,
        text=f'Обращение {ticket.ticket_id} от пользователя @{ticket.from_user or "аноним"}\n\n{ticket.user_request}',
        reply_markup=InlineKeyboardMarkup([buttons]),
    )


async def notify_user(ticket: Ticket):
    await application.bot.send_message(
        chat_id=ticket.from_chat,
        text=f'Обращение {ticket.ticket_id} от {ticket.from_user or "аноним"} перешло в статус {ticket.ticket_status}',
    )

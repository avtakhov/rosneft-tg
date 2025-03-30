import dataclasses
import datetime
import enum
import typing


@dataclasses.dataclass
class WaitingForTicket:
    from_chat: int
    wait_until: datetime.datetime


class Default:
    def __init__(self):
        pass


UserStatus = WaitingForTicket | Default

TicketStatus = typing.Literal['New', 'InProgress', 'Done', 'Cancelled']


@dataclasses.dataclass
class Ticket:
    from_user: str | None
    from_chat: int
    ticket_id: str
    ticket_status: TicketStatus
    user_request: str


@dataclasses.dataclass
class User:
    def __init__(self):
        self.status = Default()
        self.tickets = []

    status: UserStatus
    tickets: list[Ticket]


users_db: dict[int, User] = {}

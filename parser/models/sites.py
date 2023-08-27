import uuid

from .base import BaseOrjsonModel


class SiteModel(BaseOrjsonModel):
    id: uuid.UUID = uuid.uuid4()
    url: str
    title: str
    html: str

from models.base import BaseOrjsonModel


class PageResponseModel(BaseOrjsonModel):
    id: str
    title: str
    url: str
    html: str

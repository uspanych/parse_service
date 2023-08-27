from functools import lru_cache
from typing import List

from elasticsearch import AsyncElasticsearch
from fastapi import Depends

from adapters.elastic import get_elastic
from core.config import settings
from models.pages import PageResponseModel
from .storage import AbstractStorage, ElasticStorage
from .utils.elastic_query import get_body_search


class SearchService:

    def __init__(
        self,
        storage: AbstractStorage
    ):
        self.storage = storage

    async def get_page(
        self,
        uuid: str
    ) -> str | None:
        """Метод возвращает html страницы по url.

        Args:
            uuid (str): Id записи в хранилище.

        Returns:
            (str): HTML переданного сайта.


        """
        result = await self.storage.get_by_id(
            index=settings.elastic_index,
            data_id=uuid,
        )

        if result:

            html_page = result.get('html')
            return html_page

        return None

    async def get_pages_list(
        self,
        url: str | None = None,
        title: str | None = None,
    ) -> List[PageResponseModel]:
        """Метод возвращает список страниц по запросу.

        Args:
            url (str): URL-адрес страницы.
            title (str): Заголовок страницы.

        Returns:
            (list): Список страниц.


        """

        result = await self.storage.search_data(
            index=settings.elastic_index,
            body=get_body_search(
                url=url,
                title=title,
            )
        )

        return [PageResponseModel(**item) for item in result]


@lru_cache()
def get_search_service(
    client: AsyncElasticsearch = Depends(get_elastic),
) -> SearchService:
    return SearchService(
        ElasticStorage(client)
    )

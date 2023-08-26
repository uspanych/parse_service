import abc

from elasticsearch import AsyncElasticsearch, NotFoundError


class AbstractStorage(abc.ABC):
    @abc.abstractmethod
    async def get_by_id(
        self,
        *args,
        **kwargs,
    ):
        raise NotImplementedError

    @abc.abstractmethod
    async def search_data(
        self,
        *args,
        **kwargs,
    ):
        raise NotImplementedError


class ElasticStorage(AbstractStorage):
    """Класс-инструмент предоставляет интерфейс для работы с хранилищем."""

    def __init__(
        self,
        elastic: AsyncElasticsearch,
    ):
        self.elastic = elastic

    async def get_by_id(
        self,
        *args,
        **kwargs,
    ) -> dict | None:
        """Метод осуществляет поиск в индексе по id."""

        try:
            response = await self.elastic.get(
                index=kwargs.get('index'),
                id=kwargs.get('data_id'),
            )

        except NotFoundError:
            return None

        return response.get('_source')

    async def search_data(
        self,
        *args,
        **kwargs,
    ) -> list[dict]:
        """Метод осуществляет поиск по query в индексе."""

        data = await self.elastic.search(
            index=kwargs.get('index'),
            body=kwargs.get('body'),
        )

        return [item['_source'] for item in data['hits']['hits']]

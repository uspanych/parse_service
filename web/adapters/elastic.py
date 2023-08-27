from elasticsearch import AsyncElasticsearch
from elasticsearch.exceptions import ConnectionError
es: AsyncElasticsearch | None = None


async def get_elastic() -> AsyncElasticsearch:
    if not es:
        raise ConnectionError
    return es

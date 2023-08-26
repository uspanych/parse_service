from adapters import elastic
from elasticsearch import AsyncElasticsearch
from core.config import settings
from .scheme import SITES_SCHEME
from elasticsearch.exceptions import RequestError
from core.logger import logger


async def startup() -> None:
    elastic.es = AsyncElasticsearch(
        hosts=[settings.get_es_uri()]
    )
    try:
        await elastic.es.indices.create(
            index=settings.elastic_index,
            body=SITES_SCHEME
        )
    except RequestError as error:
        logger.error(f'Index already exists {error}')


async def shutdown() -> None:
    if elastic.es:
        await elastic.es.close()

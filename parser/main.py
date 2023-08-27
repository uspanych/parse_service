import uuid

from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

from adapters import elastic
from core.config import settings
from models.sites import SiteModel
from services.parser import get_parse_service, SiteParser


def parse_sites(
    parse_service: SiteParser,
):
    data = parse_service.search_data(
        pool_limit=settings.worker_count,
        level_down=settings.level_down,
        url=settings.url
    )

    result = [
        SiteModel(
            id=uuid.uuid4(),
            url=key,
            title=value.get('title'),
            html=value.get('html'),
        )
        for key, value in data.items()
    ]

    return result


def load_sites(
    sites: list[SiteModel] | None = None,
) -> None:
    """Функция загружает данные в Elasticsearch.

    Args:
        sites (list): Данные с сайтов.

    """

    if sites:
        document = [
            {
                '_index': settings.elastic_index,
                '_id': site.id,
                '_source': site.dict(),
            }
            for site in sites
        ]

        bulk(elastic.get_elastic(), document)


if __name__ == '__main__':
    elastic.es = Elasticsearch(
        hosts=settings.get_es_uri()
    )
    load_sites(parse_sites(get_parse_service()))

from elasticsearch import Elasticsearch
from elasticsearch.exceptions import ConnectionError
es: Elasticsearch | None = None


def get_elastic() -> Elasticsearch:
    if not es:
        raise ConnectionError
    return es

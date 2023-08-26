from elasticsearch import Elasticsearch

es: Elasticsearch | None = None


def get_elastic() -> Elasticsearch:
    return es

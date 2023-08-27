
def get_body_search(
    title: str | None = None,
    url: str | None = None,
) -> dict:
    """Метод формирует qury запрос в Elasticsearch.

    Args:
        title (str): Заголовок сайта.
        url (str): URL-адрес сайта.

    Returns:
        (dict): Сформированный запрос по параметрам,
         если оба параметра None, то сформируется базовый запрос.


    """

    if not any([title, url]):
        return {
            "query": {
                "match_all": {}
            }
        }

    query: dict = {
        "query": {
            "bool": {
                "must": [
                ]

            }
        }
    }

    if title:
        query["query"]["bool"]["must"].append(
            {'term': {"title": title}}
        )

    if url:
        query["query"]["bool"]["must"].append(
            {'term': {"url": url}}
        )

    return query

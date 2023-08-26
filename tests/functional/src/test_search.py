from http import HTTPStatus

import pytest
from functional.settings import test_settings

pytestmark = pytest.mark.asyncio

url = test_settings.service_url + '/api/v1/page/list'
headers = {'Content-Type': 'application/json'}


async def test_get_sites(client_session):
    async with client_session.get(url, headers=headers) as response:
        assert response.status == HTTPStatus.OK

        body = await response.json()

        assert len(body) == 3


async def test_query_param(client_session):
    async with client_session.get(url, headers=headers, params=dict(url='http://test_server:5000/url4/')) as response:
        body = await response.json()

        assert body[0]['url'] == 'http://test_server:5000/url4/'

    async with client_session.get(url, headers=headers, params=dict(title='Тестовая страница')) as response:
        body = await response.json()

        assert body[0]['title'] == 'Тестовая страница'

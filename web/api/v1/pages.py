from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import HTMLResponse
from services.search import SearchService, get_search_service
from services.utils.constants import PAGE_NOT_FOUND
from models.pages import PageResponseModel
from fastapi import Query

router = APIRouter()


@router.get(
    '/page',
    response_class=HTMLResponse,
    description='Метод возвращает html конкретной страницы',
)
async def get_page_html(
    uuid: str,
    search_service: SearchService = Depends(get_search_service),
) -> str:

    result = await search_service.get_page(
        uuid=uuid
    )
    if not result:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail=PAGE_NOT_FOUND,
        )

    return result


@router.get(
    '/page/list',
    response_model=list[PageResponseModel],
    description='Метод возвращает список сайтов',
)
async def get_page_list(
    url: str | None = Query(None, title='URL-адрес сайта'),
    title: str | None = Query(None, title='Заголовок сайта'),
    search_service: SearchService = Depends(get_search_service)
) -> list[PageResponseModel]:

    sites = await search_service.get_pages_list(
        url=url,
        title=title,
    )

    return sites

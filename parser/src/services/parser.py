import concurrent.futures
from concurrent.futures import ThreadPoolExecutor
from typing import Optional
from urllib.parse import urlparse, urljoin

import requests
from bs4 import BeautifulSoup
from requests.exceptions import ConnectionError

from src.core.logger import logger
from .tools import AbstractParser


class SiteParser(AbstractParser):
    """Класс-инструмент предоставляет интерфейс для работы с локальным парсером."""

    def search_data(
        self,
        *args,
        **kwargs,
    ) -> Optional[dict]:
        """Метод осуществляет парсинг сайта."""

        if kwargs.get('level_down') == 0:
            return self._get_data_website(kwargs.get('url'))

        some_dict = {}
        with concurrent.futures.ThreadPoolExecutor(max_workers=kwargs.get('pool_limit')) as executor:
            result = self._get_website_from_level(kwargs.get('url'), kwargs.get('level_down'), executor)
            futures = [executor.submit(self._get_data_website, url) for url in result]
            for future in concurrent.futures.as_completed(futures):
                some_dict.update(future.result())

        return some_dict

    def _get_all_website_links(
        self,
        url
    ) -> set:
        """
        Возвращает все URL-адреса, найденные на `url`, в котором он принадлежит тому же веб-сайту.

        Args:
            url (str): URL-адрес сайта.

        Return:
            (set): Множество link с сайта(url)



        """

        # все URL-адреса `url`
        urls_down = set()

        with requests.Session() as session:
            try:
                response = session.get(url)

                soup = BeautifulSoup(response.text, "html.parser")

                for a_tag in soup.findAll("a"):
                    href = a_tag.attrs.get("href")
                    if href == "" or href is None:
                        # href пустой тег
                        continue

                    href = urljoin(url, href)

                    parsed_href = urlparse(href)
                    # Удаление GET-параметров URL, фрагменты URL
                    href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path

                    if not self.is_valid(href) and url not in urls_down:
                        # недействительный URL
                        continue

                    urls_down.add(href)
                return urls_down

            except (ConnectionError, UnicodeDecodeError) as error:
                logger.error(f'Ошибка в работе парсера {error}')

    def _get_website_from_level(
        self,
        url: str,
        level: int,
        executor: ThreadPoolExecutor,
    ) -> set:
        """Функция возвращает найденные ссылки на глубине level.

        Args:
            url (str): URL-адрес сайта.
            level (int): Уровень погружения.
            executor (object): ThreadPoolExecutor.

        Returns:
            set - Множество найденных url на сайте, на глубине равной level.


        """

        result = self._get_all_website_links(url)
        k = 0

        while k != level:
            urls_in_level: set = set()
            futures = [executor.submit(self._get_all_website_links, url) for url in result]
            for future in concurrent.futures.as_completed(futures):
                response = future.result()
                urls_in_level = urls_in_level.union(response)
            k += 1

        return urls_in_level

    @staticmethod
    def _get_data_website(
        url: str
    ) -> dict:
        """Метод парсит данные с сайта.

        Args:
            url (str): URL-адрес сайта.

        Returns:
            (dict): Словарь с данными сайта.

        """

        with requests.Session() as session:
            try:
                response = session.get(url)
                soup = BeautifulSoup(response.text, 'html.parser')
                if soup:
                    return {
                        url: {
                            'title': soup.find('title').string,
                            'html': response.text,
                        }
                    }
            except (ConnectionError, UnicodeDecodeError) as error:
                logger.error(f'Ошибка в работе парсера {error}')

    @staticmethod
    def is_valid(
        url: str,
    ) -> bool:
        """Проверяет, является ли 'url' действительным URL."""

        parsed = urlparse(url)
        return bool(parsed.netloc) and bool(parsed.scheme)


def get_parse_service() -> SiteParser:
    return SiteParser()

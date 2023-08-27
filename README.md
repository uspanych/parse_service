# Парсер произвольных сайтов :)


В директории проекта предоставлен файл .env.example. 
- Сайт, который необходимо распарсить, указать в переменной {URL}
- Глубину погружения указать в переменной {LEVEL_DOWN}
- Количество одновременно загружаемых страниц указать в переменной {WORKER_COUNT}

## Запуск
- docker compose up --build


## Api
#### [GET] /api/v1/page/ - Метод возвращает страницу по id.
    param - {id} Id записи в Бд.


#### [GET] /api/v1/page/list/ - Метод возвращает список найденных сайтов с данными.
    param - {url} Опциональный параметр, url нужного сайта.
    param - {title} Опциональный параметр, заголовок нужного сайта.


Swagger документация доступна по адресу http://127.0.0.1/api/openapi


При старте приложения запускается контейнер с парсером, который загружает данные в Elasticsearch,
далее контейнер заканчивает свою работу. 
Далее с данными можно работать посредством методов Апи.

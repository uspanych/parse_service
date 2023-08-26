from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def read():
    return """
!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
 <head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>Пример веб-страницы</title>
 </head>
 <body>
  <h1>Заголовок</h1>
  <!-- Комментарий -->
  <p>Первый абзац.</p>
  <p>Второй абзац.</p>
  <p>Моя первая веб-страница</p>
  <a href="http://test_server:5000/url2/">Ссылка</a>
   </body>
 </body>
</html>"""


@app.get("/url2", response_class=HTMLResponse)
def func2():
    return """
    !DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
    <html>
     <head>
      <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
      <title>Пример веб-страницы</title>
     </head>
     <body>
      <h1>Заголовок</h1>
      <!-- Комментарий -->
      <p>Первый абзац.</p>
      <p>Второй абзац.</p>
      <p>Моя первая веб-страница</p>
      <a href="http://test_server:5000/url3/">Ссылка</a>
      <a href="http://test_server:5000/url4/">Ссылка</a>
      <a href="http://test_server:5000/url5/">Ссылка</a>
       </body>
     </body>
    </html>"""


@app.get("/url3", response_class=HTMLResponse)
def read():
    return """
!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
 <head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>Пример веб-страницы</title>
 </head>
 <body>
  <h1>Заголовок</h1>
  <!-- Комментарий -->
  <p>Первый абзац.</p>
  <p>Второй абзац.</p>
  <p>Моя первая веб-страница</p>
   </body>
 </body>
</html>"""


@app.get("/url4", response_class=HTMLResponse)
def read():
    return """
!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
 <head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>Тестовая страница</title>
 </head>
 <body>
  <h1>Заголовок</h1>
  <!-- Комментарий -->
  <p>Первый абзац.</p>
  <p>Второй абзац.</p>
  <p>Моя первая веб-страница</p>
   </body>
 </body>
</html>"""


@app.get("/url5", response_class=HTMLResponse)
def read():
    return """
!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
 <head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>Пример веб-страницы</title>
 </head>
 <body>
  <h1>Заголовок</h1>
  <!-- Комментарий -->
  <p>Первый абзац.</p>
  <p>Второй абзац.</p>
  <p>Моя первая веб-страница</p>
   </body>
 </body>
</html>"""

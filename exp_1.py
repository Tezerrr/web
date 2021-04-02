from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Миссия Колонизация Марса"

@app.route("/image_mars")
# def bootstrap():
#     return '''<!doctype html>
#                 <html lang="en">
#                   <head>
#                     <meta charset="utf-8">
#                     <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
#                     <link rel="stylesheet"
#                     href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
#                     integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
#                     crossorigin="anonymous">
#                     <title>Привет, Яндекс!</title>
#                   </head>
#                   <body>
#                     <h1>Привет, Яндекс!</h1>
#                     <div class="alert alert-primary" role="alert">
#                       А мы тут компонентами Bootstrap балуемся
#                     </div>
#                   </body>
#                 </html>'''
def start():
    return '''<!DOCTYPE html>
<html lang='en'>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet"
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                    crossorigin="anonymous">
    <title>Привет, Марс!</title>
</head>

<body>
<h1>Жди нас, Марс!</h1>
<img src="/static/img/mars.jpg" alt="здесь должна была быть картинка, но не нашлась">
<p class="alert alert-secondary" role="alert">Человечество вырастает из детства.</p>
<p class="alert alert-success" role="alert">Человечеству мала одна планета.</p>
<p class="alert alert-secondary" role="alert">Мы сделаем обитаемыми безжизненные пока планеты.</p>
<p class="alert alert-warning " role="alert">И начнем с Марса!.</p>
<p class="alert alert-danger " role="alert">Присоединяйся!</p>
</body>
</html>'''

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
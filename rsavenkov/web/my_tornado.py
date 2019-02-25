
import tornado.ioloop
import tornado.web

'''
Пользовательский класс обработчик запросов
'''
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

'''
Создает tornado веб сервер со ссылкой на обработчик запросов
'''
def make_app():
    return tornado.web.Application((
        (r'/', MainHandler),
    ))

# для самостоятельного запуска скрипта
if __name__ == "__main__":
    # создаем tornado веб сервер
    app = make_app()
    # ставим его слушать по порту 8888
    app.listen(8888)
    # запускаем сервер
    tornado.ioloop.IOLoop.current().start()
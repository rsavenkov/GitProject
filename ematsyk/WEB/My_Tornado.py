import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        with open("C:/Users/Mailz/PycharmProjects/GitProject/ematsyk/WEB/My_Tornado.py", 'r', encoding='windows-1251') as f:
            a = f.read()
        self.write(a)

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8088)
    tornado.ioloop.IOLoop.current().start()
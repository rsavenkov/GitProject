# �������� � ������ ��� ���������� tornado
# https://www.tornadoweb.org/en/stable/
import tornado.ioloop
import tornado.web

'''
���������������� ����� ���������� ��������
'''
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

'''
������� tornado ��� ������ �� ������� �� ���������� ��������
'''
def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

# ��� ���������������� ������� �������
if __name__ == "__main__":
    # ������� tornado ��� ������
    app = make_app()
    # ������ ��� ������� �� ����� 8888
    app.listen(8888)
    # ��������� ������
    tornado.ioloop.IOLoop.current().start()
import cherrypy

class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        with open("C:/Users/Mailz/PycharmProjects/GitProject/ematsyk/WEB/My_cherrypy.py", 'r', encoding='windows-1251') as f:
            return f.read()

cherrypy.quickstart(HelloWorld())
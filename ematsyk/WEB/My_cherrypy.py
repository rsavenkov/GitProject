import cherrypy

class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        with open(my_cherryy.py, read, encoding='windows-1251') as f:
            return f.read()

cherrypy.quickstart(HelloWorld())
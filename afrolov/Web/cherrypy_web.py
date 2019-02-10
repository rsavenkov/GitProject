import cherrypy

class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        with open('C:/Users/Hero/PycharmProjects/GitProject/afrolov/Web/Text.txt', 'r', encoding='utf-8') as f:
            a = f.read()
        return a

cherrypy.quickstart(HelloWorld())
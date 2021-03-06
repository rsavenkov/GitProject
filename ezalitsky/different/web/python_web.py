# импортируем стандартный веб сервер и обработчик запросов
from http.server import BaseHTTPRequestHandler, HTTPServer
# импортим библиотеку для логирования, удобно логировать входящие запросы в случае с веб серверами
import logging
# импортим в код библиотеку postgresql для работы с базой данных postgresql
import postgresql

'''
Исходя из названия, обработчик http запросов. Необходим нам при создании http сервера
Определяет два метода которые будут обрабатывать get и post запросы, в которых мы напишем свою логику обработки запросов
Наследуем от BaseHTTPRequestHandler иначе ничего работать не будет!
'''
class MyHTTPRequestHandler(BaseHTTPRequestHandler):

    # Аттрибут класса нашего обработчика который запоминает соединение с базой
    # Необходим будет при обработке post запроса сразу записывать данные в базу
    connection = None

    '''
    Вспомогательный метод который устанавликает код ответа и заголовок Content-type
    '''
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    '''
    Переопределяем от родителя метод который обрабатывает все get запросы к серверу
    '''
    def do_GET(self):

        path = self.path

        self._set_response()

        if (path == '/form_student'): # если uri содержит /form_student
            with open('form_student.html', 'r+', encoding='UTF-8') as f: # читаем текстовый файл
                lines = f.readlines()  # читаем файл, результат получаем в виде списка строк
                output = ''.join(lines)  # преобразуем список строк в одну строку для отдачи на клиент
                self.wfile.write(output.encode('utf-8'))  # пишем нашу строку в сеть запросившему клиенту

        elif (path == '/form_teacher'): # если uri содержит /form_student
            with open('form_teacher.html', 'r+', encoding='UTF-8') as f: # читаем текстовый файл
                lines = f.readlines()  # читаем файл, результат получаем в виде списка строк
                output = ''.join(lines)  # преобразуем список строк в одну строку для отдачи на клиент
                self.wfile.write(output.encode('utf-8'))  # пишем нашу строку в сеть запросившему клиенту

        elif (path == '/python-happy.jpeg'):
            #webbrowser.open(r'python-happy.jpeg')
            with open('python-happy.jpeg', 'rb') as f:
                self.wfile.write(f.read())
            #img = Image.open('python-happy.jpeg')
            #img.show()
        else: # случай когда uri запроса отличный от /form_student, на этот случай обработки не предусмотрено
            logging.warning('Url {} doesn\'t prodive handler!'.format(path)) # логгируем для собственного спокойствия
            self.wfile.write('No handler for {}'.format(path).encode('UTF-8'))  # сообщение пользователю

    '''
    Переопределяем от родителя метод который обрабатывает все post запросы к серверу
    '''
    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # определяем размер входящего сообщения
        post_data = self.rfile.read(content_length) # читаем это сообщение
        student = []
        teacher = []
        data = str(post_data)[0:-1].split('&') # обрабатываем данные от запроса
        self._set_response()
        if (self.path == 'register_student'):
            for d in data:
                logging.info(d.split('=')[1])
                student.append(d.split('=')[1])
                # вот здесь по-хорошему insert в базу надо взять в try-except на тот случай если произойдет ошибка
                # и ответить клиенту что операция на сервере произошла с ошибкой
            insert = MyHTTPRequestHandler.connection.prepare('''INSERT INTO public.student (id, first_name, last_name, middle_name, birthday_date, gender, description, rating, teacher_id)
                                                                VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9);''')
            id = MyHTTPRequestHandler.connection.prepare('select nextval(\'student\')')()[0][0] # готовим и сразу выполняем select по sequence который в результате нам вернет новый id
            insert(id, student[0], student[1], student[2], None, True, student[3], int(student[4]), 1)
            self._set_response() # готовим ответ
            self.wfile.write("Student {} is added!<br><a href='/form_student'>Go back to registering form".format(''.join(student)).encode('utf-8')) # отвечаем клиенту что новый студент добавлен и даем ему ссылку на обратный переход на форму добавления
        elif (self.path == 'register_teacher'):
            for d in data:
                logging.info(d.split('=')[1])
                teacher.append(d.split('=')[1])
            insert = MyHTTPRequestHandler.connection.prepare('''INSERT INTO public.teacher (id, first_name, last_name, birthday_date, gender, description)
                                                                            VALUES ($1, $2, $3, $4, $5, $6);''')
            id = MyHTTPRequestHandler.connection.prepare('select nextval(\'teacher\')')()[0][0]  # готовим и сразу выполняем select по sequence который в результате нам вернет новый id
            insert(id, teacher[0], teacher[1], None, True, teacher[2])
            self._set_response()  # готовим ответ
            self.wfile.write("Teacher {} is added!<br><a href='/form_teacher'>Go back to registering form".format(''.join(teacher)).encode('utf-8'))  # отвечаем клиенту что новый студент добавлен и даем ему ссылку на обратный переход на форму добавления
        else:
            self.wfile.write("Bad push on server".encode('utf-8'))
'''          
Функция которая запускает сервер
'''
def run():
    db = None
    try:
        connection_string = 'pq://egor:123@127.0.0.1:5432/mytestdb'
        # создаем соединение с базой данной my_db по адресу хост 127.0.0.1, порт 5432, логин postgres, пароль 123456s
        db = postgresql.open(connection_string)
        exist = db.prepare("SELECT COUNT(*) FROM pg_class WHERE relname = 'student_id_seq'")()[0][0] # проверяем в системных каталогах есть ли наша последовательность для студентов
        if exist == 0: # если нет, то...
            db.execute("CREATE SEQUENCE student_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 10000000000 START 1 CACHE 1") # создаем ее
    except Exception:
        logging.error('Cann\'t connect to database with url {}'.format(connection_string))
        exit(-1)
    # Создаем http сервер который работает по порту 8000 и обрабатывает http запросы с помощью собственного MyHTTPRequestHandler
    try:
        PORT = 8009
        server_address = ("", PORT)
        MyHTTPRequestHandler.connection = db
        with HTTPServer(server_address, MyHTTPRequestHandler) as httpd:
            logging.debug("serving at port", PORT)
            # судя по описанию метода - обрабатывает запрос и ждет следующий пока сервер не будет выключен
            httpd.serve_forever()
    except Exception as e:
        logging.error('Something wrong with your server, port is {} \n See explanation {}'.format(PORT, e))
        exit(-1)

# для самостоятельного запуска скрипта
if __name__ == '__main__':
    run()
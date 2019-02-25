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
        self._set_response()
        if (self.path == '/form'):  # если uri содержит /form
            with open('form.html', 'r+', encoding='UTF-8') as f:  # читаем текстовый файл
                lines = f.readlines()  # читаем файл, результат получаем в виде списка строк
                output = ''.join(lines)  # преобразуем список строк в одну строку для отдачи на клиент
                self.wfile.write(output.encode('utf-8'))  # пишем нашу строку в сеть запросившему клиенту
        elif (self.path == '/python-happy.jpeg'):
            # webbrowser.open(r'python-happy.jpeg')
            with open('python-happy.jpeg', 'rb') as f:
                self.wfile.write(f.read())
            # img = Image.open('python-happy.jpeg')
            # img.show()
        else:  # случай когда uri запроса отличный от /form, на этот случай обработки не предусмотрено
            logging.warning(
                'Url {} doesn\'t prodive handler!'.format(self.path))  # логгируем для собственного спокойствия
            self.wfile.write('No handler for {}'.format(self.path).encode('UTF-8'))  # сообщение пользователю

    '''
    Переопределяем от родителя метод который обрабатывает все post запросы к серверу
    '''

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])  # определяем размер входящего сообщения
        post_data = self.rfile.read(content_length)  # читаем это сообщение
        student = {}
        data = str(post_data)[0:-1].split('&')  # обрабатываем данные от запроса
        for d in data:
            data = d.split('=')
            student[data[0]] = data[1]
        # вот здесь по-хорошему insert в базу надо взять в try-except на тот случай если произойдет ошибка
        # и ответить клиенту что операция на сервере произошла с ошибкой
        insert = MyHTTPRequestHandler.connection.prepare('''INSERT INTO public.student 
        (id, first_name, last_name, middle_name, birth_date, gender, description, rating, teacher_id)
          VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9);''')
        id = MyHTTPRequestHandler.connection.prepare('select nextval(\'student_id_seq\')')()[0][0]  # готовим и сразу выполняем select по sequence который в результате нам вернет новый id
        insert(id, student['b\'name'], student['surname'], student['third_name'], None, True, student[3], int(student[4]), int(student['teacher']))
        self._set_response()  # готовим ответ
        self.wfile.write(
            "Student {} is added!<br><a href='/form'>Go back to registering form".format(''.join(student)).encode(
                'utf-8'))  # отвечаем клиенту что новый студент добавлен и даем ему ссылку на обратный переход на форму добавления


'''
Функция которая запускает сервер
'''


def run():
    db = None
    try:
        connection_string = 'pq://postgres:123456@localhost:5432/postgres'
        # создаем соединение с базой данной my_db по адресу хост 127.0.0.1, порт 5432, логин postgres, пароль 123456s
        db = postgresql.open(connection_string)
        exist = db.prepare("SELECT COUNT(*) FROM pg_class WHERE relname = 'student_id_seq'")()[0][0]  # проверяем в системных каталогах есть ли наша последовательность для студентов
        if exist == 0:  # если нет, то...
            db.execute(
                "CREATE SEQUENCE student_id_seq INCREMENT 1 MINVALUE 1 MAXVALUE 10000000000 START 1 CACHE 1")  # создаем ее
    except Exception as e:
        logging.error('Cann\'t connect to database with url {} {}'.format(connection_string, e))
        exit(-1)
    # Создаем http сервер который работает по порту 8000 и обрабатывает http запросы с помощью собственного MyHTTPRequestHandler
    try:
        PORT = 8009
        server_address = ("", PORT)
        MyHTTPRequestHandler.connection = db
        with HTTPServer(server_address, MyHTTPRequestHandler) as httpd:
            logging.info("serving at port", PORT)
            # судя по описанию метода - обрабатывает запрос и ждет следующий пока сервер не будет выключен
            httpd.serve_forever()
    except Exception as e:
        logging.error('Something wrong with your server, port is {} \n See explanation {}'.format(PORT, e))
        exit(-1)


# для самостоятельного запуска скрипта
if __name__ == '__main__':
    run()

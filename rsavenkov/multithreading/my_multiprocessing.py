import os
# дублирует функциональность библиотеки threading только оперирует процессами а не потоками
from multiprocessing import Process, current_process, Pool

'''
Функция которая принимает число и умножает его на 2.
Печатает число, резульата, id процесса и имя процесса
'''
def doubler(number):
    result = number * 2
    proc_id = os.getpid()
    proc_name = current_process().name
    print('{0} doubled to {1} by process id {2} and name {3}'.format(number, result, proc_id, proc_name))

'''
Код выполняемый в случае если скрипт запущен самостоятельно
'''
if __name__ == '__main__':
    numbers = [5, 10, 15, 20, 25]
    procs = []

    # в цикле на каждое число из списка numbers, создаем отдельный процесс в системе
    # созданный процесс на каждой итерации помещаем в список и запускаем
    print('------- Process example -------')
    for index, number in enumerate(numbers):
        proc = Process(target=doubler, args=(number,))
        procs.append(proc)
        proc.start()

    # в цикле по списку созданных процессов, родительский поток ждек пока все они завершаться
    for proc in procs:
        proc.join()

    # это другой пример с использованием pool(пула)
    # pool это объект который самостоятельно управляет жизнью поток(запуск->работа->завершение)
    # pool нужен для того чтобы не писать код как в предыдущем примере
    print('------- Process pool example -------')
    pool = Pool(processes=3)
    result = pool.apply_async(doubler, (25,))
    print(result.get(timeout=1))

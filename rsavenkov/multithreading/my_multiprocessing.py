import os
from multiprocessing import Process, current_process, Pool

def doubler(number):
    result = number * 2
    proc_id = os.getpid()
    proc_name = current_process().name
    print('{0} doubled to {1} by process id {2} and name {3}'.format(number, result, proc_id, proc_name))


if __name__ == '__main__':
    numbers = [5, 10, 15, 20, 25]
    procs = []

    print('------- Process example -------')
    for index, number in enumerate(numbers):
        proc = Process(target=doubler, args=(number,))
        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join()

    print('------- Process pool example -------')
    pool = Pool(processes=3)
    result = pool.apply_async(doubler, (25,))
    print(result.get(timeout=1))

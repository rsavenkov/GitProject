from _thread import start_new_thread

threadId = 1

'''
доработать программу следующим образом:
1. Добавить 3-ий поток который вычисляет факториал
2. Один из потоков бросает исключение при выполнении 
'''


def factorial(n):
    global threadId
    if n < 1:
        print("%s: %d" % ("Thread", threadId))
        threadId += 1
        return 1
    else:
        returnNumber = n * factorial(n - 1)
        print(str(n) + ' ! = ' + str(returnNumber))
        return returnNumber


start_new_thread(factorial, (5,))
start_new_thread(factorial, (4,))
start_new_thread(factorial, (3,))

c = input("Waiting for threads to return...\n")

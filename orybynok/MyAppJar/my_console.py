if __name__ == '__main__':

    file = input('Введите имя файла:')
    error_code = checkIsWinCorrectPath(file)

    if error_code != 0:
        exit(error_code)

    with open(file, 'w', encoding='utf-8') as f:
        try:
            first = input('Введите содержимое файла:')
            f.writelines(first + '\n')
            while True:
                line = input()
                if line == 'quit()':
                    #exit(0)
                    raise QuitProgramException()
                f.writelines(line + '\n')
        except QuitProgramException as e:
            print(e.message.format(f.name))
            error_code = 0
        except KeyboardInterrupt as e:
            print('\nНепредвиденное завершение программы! Фалй не создан!')
            error_code = 2

    if error_code != 0:
        os.remove(file)

    exit(error_code)


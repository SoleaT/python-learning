# модуль записи и чтения лога

def write_log(str):
    with open('calc_log.txt', 'a') as calc_log:
        calc_log.writelines(str + '\n')


def view_log():
    with open('calc_log.txt', 'r') as calc_log:
        for i in calc_log:
            print(i.rstrip())

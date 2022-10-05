import log
import csv

def get_input():
    my_list = [input('Введите данные строкой: ').split(' ') for i in range(int(input('Сколько строк собираетесь ввести?: ')))]
    with open('data_base.txt', 'a', encoding="UTF-8") as data:
        for i in my_list:
            log.log_data("Добавлено из консоли", i)
            data.write(' '.join(i) + '\n')
            

            
def get_file():
    with open('input.txt', 'r', encoding="UTF-8") as data:
        text = data.read()
        my_list = [i for i in text.split('\n')]
        with open('data_base.txt', 'r', encoding="UTF-8") as data2:
            text2 = data2.read()
            my_list2 = [i for i in text2.split('\n')]
        with open('data_base.txt', 'a', encoding="UTF-8") as data3:    
            for i in my_list:
                if i not in my_list2:
                    data3.write(''.join(i) + '\n')
                    log.log_data("Загружено из файла", i) 
                else:
                    log.log_data("Неудачная попытка загрузки из файла (дубль)", i)     



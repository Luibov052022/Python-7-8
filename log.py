import datetime

def log_data(func, data):
    with open('log.txt', 'a', encoding="UTF-8") as file:
        file.write(f'{datetime.datetime.now()} - {func} - {data}' )
        file.write('\n')
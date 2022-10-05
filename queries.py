def query_txt(data_filter):
    with open('data_base.txt', 'r', encoding="UTF-8") as data:
            text2 = data.read()
            my_list = [i for i in text2.split('\n') if data_filter in i]
    if len(my_list) > 0:        
        print(*my_list, sep = '\n')
    else:
        print('Значение не найдено')         
            

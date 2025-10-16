# 5 вариант
import csv,random
import xml.etree.ElementTree as ET

massive = []
with open('books.csv', encoding='cp1251') as f:
    reader = csv.reader(f, delimiter=';')
    for row in reader:
        massive.append(row)
'''
def task1():
    c = 0
    for line in f:
        ll = [(x) for x in line.split(";")]
        if len(ll[1]) > 30:
            c += 1
    print(c)
print(task1())'''
def task2():
    author = (input(("Enter author's name").lower()))
    author = author.replace(' ','')
    stop_int=0
    for row in massive:
        file_aut_str = ''
        file_aut_str_reversed = ''
        file_aut = [(x).lower() for x in row[3].split(" ")]
        file_aut_reversed = list(reversed(file_aut))
        for i in range(len(file_aut_reversed)):
            file_aut_str_reversed = file_aut_str_reversed + file_aut_reversed[i]
        for i in range(len(file_aut)):
            file_aut_str = file_aut_str + file_aut[i]

        if author == file_aut_str or author == file_aut_str_reversed:
            print(row)
        else:
            stop_int=1
    if stop_int == 1: print("Книги не найдены :(")
print(task2())
'''
print(task2())
def task3():
    with open('bibliography.txt',"w", encoding='utf-8') as f:
        numbers = []
        i = 1
        while i <= 21:
            row_number = random.randint(0,len(massive)-1)
            numbers.append(row_number)
            i += 1
        for k in range(1,len(numbers)):

            current_row = massive[numbers[k]]
            author=str(current_row[3])
            name=str(current_row[1])
            date=str(current_row[6])

            f.writelines(str(k)+ ') ' +author+'. '+name+' - '+date+'\n')
    print('file done')
print(task3())
def task4():
    tree = ET.parse('currency.xml')
    root = tree.getroot()
    value_list=[]
    char_code_list=[]
    for val in root.findall('.//Valute'):
        value_list.append(val.find('Value').text)
        char_code_list.append(val.find('CharCode').text)
    print('Value:',value_list)
    print('CharCode:',char_code_list)
print(task4()) '''





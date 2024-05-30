# -*- coding: utf-8 -*-

from pprint import pprint

file_name = 'homework7_1.txt'
file = open(file_name, mode='rb') # mode (режим): чтение бинарное
file_content = file.read()
file.close()
pprint(file_content)

# Через цикл (что и требовалось):

file = open(file='homework7_1.txt', mode='r')
print(file.read())  # команда для прочтения файла: .read()

for line in file.readlines():  # циклом выводится построчно без скобок, но с пробелом меж строк
    print(line)  # print(line, end="") без пробела

file.close()  # после рочтения фаил надо закрыть
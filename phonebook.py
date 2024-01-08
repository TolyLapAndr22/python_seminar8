"""Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в текстовом файле
3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
4. Использование функций. Ваша программа не должна быть линейной

ДЗ: Дополнить справочник возможностью копирования данных из одного файла в другой.
Пользователь вводит номер строки, которую необходимо перенести из одного файла в другой.
"""

def input_name():
    return input('введите имя: ')

def input_surname():
    return input('введите фамилию: ')
def input_patronymic():
    return input('введите отчество: ')
def input_phone():
    return input('введите телефон: ')

def input_adress():
    return input('введите адрес: ')

def create_contact():
    surname = input_surname()
    name = input_name()
    patronymic = input_patronymic()
    phone = input_phone()
    adress = input_adress()
    return f'{surname} {name} {patronymic} {phone}\n{adress}\n\n'

def add_contact(contact):
    # contact = create_contact()
    with open('phonebook.txt', 'a', encoding='UTF-8') as file:
        file.write(contact)

def  show_info():
    with open('phonebook.txt', 'r', encoding='UTF-8') as file:
        contacts_list = file.read().rstrip().split('\n\n')
        # print(file.read().rstrip())
        for contact in enumerate(contacts_list,1):
            print(*contact)

def seach_contact():
    var_search = input('поиск по :\n'
                       '1. фамилии\n'
                       '2. имени\n'
                       '3. отчеству\n'
                       '4. телефону\n'
                       '5. адресу\n'
                       'Ввод: ')
    while var_search not in ('1', '2', '3', '4', '5'):
        print("введите число")
        var_search = input("поиск по :")

    index_var = int(var_search)-1
    search = input('что ищем: ')
    with open('phonebook.txt', 'r', encoding='UTF-8') as file:
        contacts_list = file.read().rstrip().split('\n\n')
        # print(contacts_list)
    for contact_str in contacts_list:
        contact_lst = contact_str.replace('\n',' ').split()
        # print(contact_lst)
        if search in contact_lst[index_var]:
            print(contact_str)
def copy_contact():
    with open('phonebook.txt', 'r', encoding='UTF-8') as file:
        contacts_list = file.read().rstrip().split('\n\n')
        list_num=list(enumerate(contacts_list,1))
        for contact in list_num:
            print(*contact)
    var_search = input('введите номер строки для переноса в другой файл: ')
    while (int(var_search) > len(list_num) or int(var_search) < 1):
        var_search = input("введите номер строки для переноса в другой файл: ")
    with open('phonebook_copy.txt', 'a', encoding='UTF-8') as file:
        file.write(f'{(list_num[int(var_search)-1])[1]}\n\n')

def interface():
    comm ='-1'
    while comm !='5':
        print('варианты действий:\n'
              "1. добавить контакт\n"
              "2. вывести на экран\n"
              "3. поиск контакта\n"
              "4. копирование данных\n"
              "5. выход из справочника\n")
        comm = input("введите код действия: ")
        while comm not in ('1','2','3','4','5'):
            print("введите число")
            comm = input("введите код действия: ")
        match comm:
            case '1':
                add_contact(create_contact())
            case '2':
                show_info()
            case '3':
                seach_contact()
            case '4':
                copy_contact()
            case '5':
                print('exit......')


interface()
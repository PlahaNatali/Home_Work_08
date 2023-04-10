# Создать телефонный справочник с возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной
# записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной


def read_contacts_from_file(file):
    contacts = []
    with open(file, 'r', encoding='UTF-8') as f:
        data = f.readlines()
    for line in data:
        contact = line.split(';')
        new_contact = {'name': contact[0].strip(),
                    'phone': contact[1].strip(),
                    'comment': contact[2].strip()}
        contacts.append(new_contact)
    return contacts


def save_contacts_in_file(file, contacts):
    new_data = []
    for contact in contacts:
        new_data.append('; '.join(contact.values()) + '\n')
    with open(file, 'w', encoding='UTF-8') as f:
        f.writelines(new_data)


def create_contact():
    contact = {}
    for field in ['name', 'phone', 'comment']:
        contact[field] = input(f'Введите "{field}": ')
    return contact


def find_contacts(contacts, params):
    found_contacts = []
    for contact in contacts:
        for param_key in params.keys():
            if params[param_key].lower() in contact[param_key].lower():
                found_contacts.append(contact)
                break
    return found_contacts


def change_contact(contacts, name, new_contact):
    for contact in contacts:
        if contact['name'] == name:
            for param_key in new_contact.keys():
                if new_contact[param_key] != "":
                    contact[param_key] = new_contact[param_key]
            return True
    return False


def remove_contact(contacts: list, name_to_remove):
    for contact in contacts:
        if contact['name'] == name_to_remove:
            contacts.remove(contact)
            return True
    return False


def print_contacts(contacts):
    for contact in contacts:
        for value in contact.values():
            print(value, end=';')
        print()


contacts = []

print('''
1. Открыть справочник
2. Сохранить справочник
3. Посмотреть все контакты
4. Создать контакт
5. Найти контакт
6. Изменить контакт
7. Удалить контакт
0. Выйти из справочника
''')

while True:
    command = int(input('Выберите пункт из меню: '))
    print('****************************')
    if command == 0:
        print('До свидание!')
        break
    elif command == 1:
        file = input('Введите имя справочника: ')
        contacts = read_contacts_from_file(file)
        print('Справочник открыт успешно!')
    elif command == 2:
        file = input('Введите имя справочника: ')
        save_contacts_in_file(file, contacts)
        print(f'Данные сохранены в справочник! "{file}"')
    elif command == 3:
        print('Контакты справочника: ')
        print_contacts(contacts)
    elif command == 4:
        new_contact = create_contact()
        contacts.append(new_contact)
    elif command == 5:
        params = {}
        for field in ['name', 'phone', 'comment']:
            value = input(f'Введите поле "{field}": ')
            if value != "":
                params[field] = value
        foud_contacts = find_contacts(contacts, params)
        if len(foud_contacts) == 0:
            print('Контакты не найдены')
        else:
            print_contacts(foud_contacts)
    elif command == 6:
        name = input("Введите имя контакта: ")
        print("Введите новые данные:")
        updated_contact = create_contact()
        if(change_contact(contacts, name, updated_contact)):
            print('Данные сохранены!')
        else:
            print('Такого контакта нет!')
    elif command == 7:
        name_to_remove = input("Введите имя контакта: ")
        if(remove_contact(contacts, name_to_remove)):
            print('Контакт удален!')
        else:
            print('Такого контакта нет!')
    else:
        print('Неверный номер!')
    print('****************************')
import json
import requests
from data import user, server


def getUserLogin(login, password):
    response = requests.get(
        f'{server}'+'user/login',
        params={
        'username': login,
        'password': password
        },
        headers={'accept': 'application/json'})
    return print(response.text)


def createUser(id, username, first, last, email, password, phone, status):
    payload = {'id': f'{id}',
               'username': f'{username}',
               'firstName': f'{first}',
               'lastName': f'{last}',
               'email': f'{email}',
               'password': f'{password}',
               'phone': f'{phone}',
               'userStatus': f'{status}'}
    response = requests.post(
         f'{server}'+'user',
         headers={'accept': 'application/json',
                  'Content-Type': 'application/json'},
         data=json.dumps(payload))
    return print(response.text)

def putUser(id, username, first, last, email, password, phone, status):
    payload = {'id': f'{id}',
               'username': f'{username}',
               'firstName': f'{first}',
               'lastName': f'{last}',
               'email': f'{email}',
               'password': f'{password}',
               'phone': f'{phone}',
               'userStatus': f'{status}'}
    response = requests.put(
        f'{server}user/' + username,
        headers={'accept': 'application/json',
                 'Content-Type': 'application/json'},
        data=json.dumps(payload))
    return print(response.text)

def getUserData(username):
    response = requests.get(
        f'{server}user/' + username)
    return print(response.json())

def deleteUser(username):
    response = requests.delete(
        f'{server}user/' + username)
    return print(response.text)

print('Логинимся юзером из файла data и проверяем')
getUserLogin(user['username'], user['password'])

print('Создаем юзера superuser666 и проверяем')
createUser(1010, 'superuser666', 'Usero4ek', 'Userov', 'user@user.ru', 'password', '12345678910', '0')

print('Логинимся созданным юзером')
getUserLogin('superuser666', 'password')

print('Получаем данные юзера')
getUserData('superuser666')

print('Меняем данные юзера')
putUser(1010, 'superuser666', 'New_name', 'New_lastname', 'user@user.ru', 'password', '12345678910', '0')

print('Проверяем что данные изменились новым запросом данных')
getUserData('superuser666')

print('Удаляем юзера')
deleteUser('superuser666')

print('Проверяем что юзера больше нет')
getUserData('superuser666')


import json
from datetime import datetime
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
    return response.text


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
    return response.text

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
    return response.text

def getUserData(username):
    response = requests.get(
        f'{server}user/' + username)
    return response.json()

def deleteUser(username):
    response = requests.delete(
        f'{server}user/' + username)
    return response.text

def write(smth):
    with open('results.txt', 'a', encoding='utf8') as my_file:
        my_file.write(f'{smth}\n')
def printAndWrite(smth):
    print(smth)
    dt_now = datetime.now()
    write(str(dt_now))
    write(str(smth))

print('Логинимся юзером из файла data и проверяем')
printAndWrite(getUserLogin(user['username'], user['password']))

print('Создаем юзера superuser666 и проверяем')
printAndWrite(createUser(1010, 'superuser666', 'Usero4ek', 'Userov', 'user@user.ru', 'password', '12345678910', '0'))

print('Логинимся созданным юзером')
printAndWrite(getUserLogin('superuser666', 'password'))

print('Получаем данные юзера')
printAndWrite(getUserData('superuser666'))

print('Меняем данные юзера')
printAndWrite(putUser(1010, 'superuser666', 'New_name', 'New_lastname', 'user@user.ru', 'password', '12345678910', '0'))

print('Проверяем что данные изменились новым запросом данных')
printAndWrite(getUserData('superuser666'))

print('Удаляем юзера')
printAndWrite(deleteUser('superuser666'))

print('Проверяем что юзера больше нет')
printAndWrite(getUserData('superuser666'))


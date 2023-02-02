import json
from datetime import datetime
import requests
from data import server

# логин
def getUserLogin(login, password):
    response = requests.get(
        f'{server}'+'user/login',
        params={
        'username': login,
        'password': password
        },
        headers={'accept': 'application/json'})
    return response.text

# создание юзера
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

# изменение юзера
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

# получение данных юзера
def getUserData(username):
    response = requests.get(
        f'{server}user/' + username)
    return response.json()

# удаление юзера
def deleteUser(username):
    response = requests.delete(
        f'{server}user/' + username)
    return response.text

# запись в файл
def write(smth):
    with open('results.txt', 'a', encoding='utf8') as my_file:
        my_file.write(f'{smth}\n')

# запись в файл и вывод в консоль
def printAndWrite(smth):
    print(smth)
    dt_now = datetime.now()
    write(str(dt_now))
    write(str(smth))


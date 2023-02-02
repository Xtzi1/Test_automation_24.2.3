import main
from data import user

print('Логинимся юзером из файла data и проверяем')
main.printAndWrite(main.getUserLogin(user['username'], user['password']))

print('Создаем юзера superuser666 и проверяем')
main.printAndWrite(
    main.createUser(1010, 'superuser666', 'Usero4ek', 'Userov', 'user@user.ru', 'password', '12345678910', '0'))

print('Логинимся созданным юзером')
main.printAndWrite(main.getUserLogin('superuser666', 'password'))

print('Получаем данные юзера')
main.printAndWrite(main.getUserData('superuser666'))

print('Меняем данные юзера')
main.printAndWrite(main.putUser(1010, 'superuser666', 'New_name', 'New_lastname', 'user@user.ru', 'password', '12345678910', '0'))

print('Проверяем что данные изменились новым запросом данных')
main.printAndWrite(main.getUserData('superuser666'))

print('Удаляем юзера')
main.printAndWrite(main.deleteUser('superuser666'))

print('Проверяем что юзера больше нет')
main.printAndWrite(main.getUserData('superuser666'))
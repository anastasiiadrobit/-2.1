login = "admin"
password = "1234"

for i in range(3):
    user_login = input("Логін: ")
    user_password = input("Пароль: ")

    if user_login == login and user_password == password:
        print("Вхід успішний ")
        break
else:
    print("Доступ заблоковано ")

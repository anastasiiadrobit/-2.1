login = "admin"
password = "1234"

attempts = 3

while attempts > 0:
    user_login = input("Введіть логін: ")
    user_password = input("Введіть пароль: ")

    if user_login == login and user_password == password:
        print("Вхід успішний!")
        break
    else:
        attempts -= 1
        print("Невірно. Залишилось спроб:", attempts)
else:

    print("Доступ заблоковано.")

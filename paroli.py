login = ['1212', 'qweasd']
password = ["1212", "QAZWSX"]


def vhod():
    global vse, ready
    vse = 0
    ready = 0
    i = 0
    login_norm = input('введите логин: ')
    password_norm = input('введите пароль: ')
    for i in range(len(login)):
        if login[i] != login_norm:
            ++i
        elif login[i] == login_norm:
                vse = 1
                break
        else:
            print("Неверный логин")
            break
    for i in range(len(password)):
        if password[i] != password_norm:
            ++i
        elif password[i] == password_norm:
                ready = 1
                break
        else:
            print("Неверный пароль")
            break
    if (vse == 1) and (ready==1): print("Поздравляю, вы вошли")



def registracia():
    login.append(input("создайте логин: "))
    password.append(input('создайте пароль: '))

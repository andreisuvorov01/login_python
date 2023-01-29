def registracia():
    login.append(input("создайте логин: "))
    password.append(input('создайте пароль: '))
login = ['1212', 'qweasd']
password = ["1212", "QAZWSX"]
def vhod():
    global vse, ready
    vse = 0
    ready = 0
    i = 0
    login_norm = input('введите логин: ')
    password_norm = input('введите пароль: ')
    #for i in range(len(login)):
    while i <= len(login):
        if login[i] == login_norm:
            vse = 1
            break
        elif login[i] != login_norm :
            ++i
        if all(login) != login_norm:
           print("Неверный логин")
           exit()
 #for i in range(len(password)):
    while i <= len(password):
        if password[i] != password_norm:++i
        elif password[i] == password_norm:
                ready = 1
                break
        if all(password) != password_norm:
            print("Неверный пароль")
            exit()
    if (vse == 1) and (ready==1): print("Поздравляю, вы вошли")





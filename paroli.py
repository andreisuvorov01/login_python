
def registracia():
    login_vvod=(input("создайте логин: "))
    password_vvod=(input('создайте пароль: '))
    login_file=open('login.txt','a')
    password_file=open('password.txt','a')
    login_file.write(str(login_vvod) +'\n')
    password_file.write(str(password_vvod) +'\n')
    login_file.close()
    password_file.close()
def vhod():
    global vse, ready
    vse = 0
    ready = 0
    i = 0
    login_norm = input('введите логин: ')
    password_norm = input('введите пароль: ')
    #for i in range(len(login)):
    with open("login.txt") as f:
            if login_norm in f.read():
                vse = 1
            else:
                print('Данного логина не существует.\n Зарегестрироваться?')
                yesOrno=input("да/нет")
                if yesOrno == "да":
                    registracia()
                else: exit()
 #for i in range(len(password)):
    with open("password.txt") as f:
        if password_norm in f.read():
            ready = 1
        else:
            print('Данного пароля не существует.\n Зарегестрироваться?')
            yesOrno = input("да/нет")
            if yesOrno == "да":
                registracia()
            else:
                exit()
    if (vse == 1) and (ready==1): print("Поздравляю, вы вошли")





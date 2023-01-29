def admin():
    file_login=open("login.txt",'r+')
    file_password = open("password.txt", 'r+')
    l=0
    p=0
    d=0
    print("Логины Пароли")
    while True:
        # считываем строку
        login = file_login.readline()
        password = file_password.readline()
        l = l + 1
        p = p + 1
        # прерываем цикл, если строка пустая
        if not login:
            break
        # выводим строку
        print(str(l) + "."+login.strip()+"    "+ str(p)+"."+password.strip())







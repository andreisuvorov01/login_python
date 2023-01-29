from paroli import vhod
from paroli import registracia
from administrator import admin
print("1.Войти")
print("2.зарегистрироваться")
print("3.Окно администратора")
vubor=int(input("введите"))
if vubor == 1:
    vhod()
elif vubor == 2:
 registracia()
 vhod()
elif vubor == 3:
 admin()
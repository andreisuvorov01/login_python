from paroli import vhod
from paroli import registracia
print("1.Войти")
print("2.зарегистрироваться")
vubor=int(input("введите"))
if vubor == 1:
    vhod()
elif vubor == 2:
    registracia()
    vhod()
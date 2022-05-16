#Возьмите код #1 и создайте для него try... except... 
#Создайте несколько except выражений для разных типов ошибок.



at = 10

n = 15

wo = 20

try: 
    for e in range(-at, at):
        print(wo / e)

except ZeroDivisionError:
    print("delenie na 0")
except TypeError:
    if at > '5':

        print(at > 5)


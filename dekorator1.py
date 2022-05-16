
def vnut():
    print('Я вложенная функция')

def vnesh():
    print('Я главная функция')
    vnut()
vnesh()

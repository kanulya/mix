


from accessify import private

class Car:
    def __init__(self, door, window, wheel):
        self.door = self.window = self.wheel = 4
        if self.check(door) and self.check(window) and self.check(wheel):
            self.door = door
            self.window = window
            self.wheel = wheel

    @private
    @classmethod
    def check(cls, parking, move):
        return type(parking)

    def set_number(self, a, b):
        if self.check(a) and self.check(b):
            self.__a = a
            self.__b = b
        else:
            raise ValueError('Передай инфу в типе Integer или Float')

    def get_number(self):
        return self.__a, self.__b

n = Number(1, 2)
print(dir(n))
n.set_number(14, 15)
print(n.get_number())
print(n.check(6))





# class Number:
#     max_number = 1000
#     min_number = 0
#
#     @classmethod
#     def check(cls, arg):    # Классметод для использования внутри класса
#         return cls.min_number <= arg <= cls.max_number
#
#     def __init__(self, a, b):
#         self.a = self.b = 0
#         if Number.check(a) and Number.check(b):
#             self.a = a
#             self.b = b
#
#     def get_data(self):     # Обычный метод
#         return self.a, self.b
#
#     @staticmethod
#     def negative(a1, b1):   # Статичный метод который не может работать со свойствами класса
#         return a1 * -1, b1 * -1
#
# n = Number(15, 200)
# print(n.get_data())
# print(n.negative(100, 555))
# print(Number.negative(100, 555))

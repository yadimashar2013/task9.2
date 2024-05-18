print('Задача 1: Фабрика Функций')


def func_1(operation):
    if operation == 'multiplication':
        def mult_(x, y):
            return x * y

        return mult_
    elif operation == 'division':
        def div_(x, y):
            return x / y

        return div_


func_mult = func_1('multiplication')
print(func_mult(2, 3))
func_mult1 = func_1('division')
print(func_mult1(10, 2))

print('Задача 2: Лямбда-Функции')
exponentiation = lambda x, y: x ** y
print(exponentiation(3, 2))


def expo_func(x, y):
    return x ** y


print(expo_func(5, 2))
print('Задача 3: Вызываемые Объекты')


class Rect:

    def __init__(self, a, b):
        self.side_a = a
        self.side_b = b

    def __call__(self):
        return self.side_a * self.side_b


area_five = Rect(10, 5)
print(f'Сторны:{area_five.side_a},{area_five.side_b}')
print(f'Площадь прямоугольника равна:{area_five.__call__()}')

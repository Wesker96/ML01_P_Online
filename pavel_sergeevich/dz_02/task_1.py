"""
Напишите программу, которая ищет корни квадратного уравнения вида a*x*x+b*x+c. На вход программы подаются a,b,c.
Результатом работы программы – действительные корни или сообщение что корней нет.
"""

"""
Решение и выводы: написана функция, реализующая решение задачи. Расчет кореней осуществлялся через дискриминант. 
Как известно, для квадратного уравнения, если дискриминант меньше нуля, то  действительных корней в уравнении нет
(есть комплексные), если равен нулю - то корень один (или, вернее, два одинаковых) и, наконец, если дискриминант
больше нуля, уравнение имеет два действительных корня. Помимо этого реализовал функцию построения графика функции
на основе библиотеки matplotlib и отображения корней (красные точки на графике)
"""

import math

import matplotlib.pyplot as plt
import numpy as np


def get_roots(cf: list):
    c_a = cf[0]
    c_b = cf[1]
    c_c = cf[2]

    if c_a == 0:
        print("Error: invalid coefficients")
        return None

    discriminant = c_b ** 2 - 4 * c_a * c_c

    if discriminant < 0:
        print("Quadratic equation not have real roots.")
        return []
    elif discriminant == 0:
        one_root = -c_b / (2 * c_a)
        print("Quadratic equation have your one real root:", one_root)
        return [one_root]
    else:
        first_root = (-c_b - math.sqrt(discriminant)) / (2 * c_a)
        second_root = (-c_b + math.sqrt(discriminant)) / (2 * c_a)

        print("Quadratic equation have your two real roots:", first_root, second_root)

        return [first_root, second_root]


def show_equation(name: str, cf: list, roots: list):
    c_a = cf[0]
    c_b = cf[1]
    c_c = cf[2]

    x = np.linspace(-10, 10, 100)
    y = c_a*x*x + c_b*x + c_c

    fig, ax = plt.subplots(num=name)
    ax.plot(x, y, linewidth=2.0)

    if roots:
        for root in roots:
            print(root)
            ax.plot(root, 0, 'ro', label='root')

    plt.grid()
    plt.show()


if __name__ == "__main__":
    cf_example = [10, 24, 3]
    show_equation("2 roots", cf_example, get_roots(cf_example))

    cf_example = [1, -6, 9]
    show_equation("1 root", cf_example, get_roots(cf_example))

    cf_example = [10, 1, 2]
    show_equation("no roots", cf_example, get_roots(cf_example))

    # error
    cf_example = [0, 24, 3]
    get_roots(cf_example)

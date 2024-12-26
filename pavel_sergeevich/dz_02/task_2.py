"""
Напишите программу, находящую наибольшее и наименьшее значение функции y = -26*x**2+25*x-9 на отрезке [-5,5].
Для решения и используйте while и какой то шаг (например 0.1). Найти производную и особую точку.

Решение:
    - производная: y = -52*x+25
    - особая точка: 0 = -52*x + 25 -> x = -25/(-52) = 0,4808

Комментарий: коэффициенты уравнения a, b, c расставлены следующим образом:
    y = a*x**2+b*x-c
"""

import matplotlib.pyplot as plt


def equation(cf: list, x: float):
    return cf[0] * (x ** 2) + cf[1] * x + cf[2]


def equation_print(cf: list):
    # this function forming txt equation for printing

    txt = str(cf[0]) + "x^2"

    if cf[1] > 0:
        txt += "-" + str(abs(cf[1])) + "x"
    else:
        txt += "+" + str(abs(cf[1])) + "x"

    if cf[2] > 0:
        txt += "-" + str(abs(cf[1]))
    else:
        txt += "+" + str(abs(cf[1]))

    return txt


def critical_point(cf: list):
    # get derivative and calculate critical point for quadratic equation

    return -cf[1] / (2 * cf[0])


def show_equation(name: str, x: list, y: list, critical_p: list):
    fig, ax = plt.subplots(num=name)
    ax.plot(x, y, linewidth=2.0)

    if critical_p:
        for critical_p in critical_p:
            # print(critical_p)
            ax.plot(critical_p[0], critical_p[1], 'ro', label='critical_p')

    plt.grid()
    plt.show()


if __name__ == "__main__":
    cf_example = [-26, 25, -9]
    segment = [-5, 5]
    step = 0.1

    # получаем особую точку
    critical_point_val = critical_point(cf_example)
    print("Critical point for equation " + equation_print(cf_example) + " equals: " + str(critical_point_val))

    x_list = []
    y_list = []

    x_way = segment[0]
    while x_way < segment[1]:
        y_way = equation(cf_example, x_way)

        x_list.append(x_way)
        y_list.append(y_way)

        x_way += step

    print("Total points:", len(x_list))

    print("Min value: " + str(min(y_list)))
    print("Max value: " + str(max(y_list)))

    critical_point_xy = [[critical_point_val, equation(cf_example, critical_point_val)]]
    show_equation("Graph of equation", x_list, y_list, critical_point_xy)

"""
Задача: Напишите программу, которая рассчитывает расход топлива маршрута, на вход подается длина маршрута и расход топлива
на 100 километров. Используйте try catch (проверка что пользователь ввел число > 0).
"""

"""
Решение и выводы: написана функция, реализующая решение задачи; в функции применена конструкция try/except на случай,
когда входные аргументы меньше, либо равны 0.
"""


def fuel_consumption(length: float, consumption: float) -> float:
    """
    Рассчет расхода топлива маршрута.

    :param length: длинна маршрута, км
    :param consumption: расход топлива на 100 км, л
    :return: расход топлива маршрута, л
    """

    assert length > 0 and consumption > 0, "Error: Invalid input arguments"

    return length * consumption / 100


if __name__ == "__main__":
    way_length = 245  # км
    lada_vesta_consumption = 9.9  # л

    print("Расход топлива для Lada Vesta на маршруте, протяженностью " + str(way_length) + " км составит: ", end="")
    print(fuel_consumption(way_length, lada_vesta_consumption), "л")

    # демонстрация работы try/except
    print("Расход топлива для Lada Vesta на маршруте, протяженностью " + str(way_length) + " км составит: ", end="")
    print(fuel_consumption(0, lada_vesta_consumption), "л")

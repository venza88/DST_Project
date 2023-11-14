import numpy as np
import math

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101) # предполагаемое число
        if number == predict_number:
            break # выход из цикла, если угадали
    return(count)

def game_core_v2(number: int = 1) -> int:
    """Сначала устанавливаем любое random число, а потом уменьшаем
    или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток
       
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    predict = np.random.randint(1, 101)
    
    while number != predict:
        count += 1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1

    return count

def game_core_v3(number: int = 1) -> int:
    """ Воспользуемся наилучшим известным мне алгоритмом для поиска 
        заданного числа - деление отрезка попоплам
    
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь
    # Инициализируем переменные
    count = 0          # Количество попыток
    left = 1           # Левая граница отрезка
    right = 100        # Правая граница отрезка
    
    while True:
        # Вычисляем сердину отрезка
        center = math.ceil((left + right - 1) / 2)
        #print(left, center, right)
        
        count += 1
        
        # Если в какой-то момент границы окажутся соседними числами 
        # - значит загаданное число одно из них
        if left == right-1: 
            break
        
        # В зависимости от знака равенства смещаем границы
        if center > number:            
            right = center
        elif center < number:            
            left = center
        else:
            break
        
    # Ваш код заканчивается здесь

    return count

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
if __name__ == "__main__":
    score_game(random_predict)
    score_game(game_core_v2)
    score_game(game_core_v3)
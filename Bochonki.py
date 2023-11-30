import random
import logging

logging.basicConfig(filename='Bochonki.log', level=logging.INFO)

# Функция для создания мешка с бочонками
def create_barrel_bag(N):
    return list(range(1, N + 1))

# Функция для вытаскивания бочонка (+ логгирование)
def pull_barrel(barrel_bag):
    if len(barrel_bag) > 0:
        pulled_barrel = random.choice(barrel_bag)
        barrel_bag.remove(pulled_barrel)
        logging.info(f'Вытянут бочонок: {pulled_barrel}')
        return pulled_barrel
    else:
        logging.info('Бочонки в мешке закончились.')
        return None

# Функция для ввода
def user_interaction():
    while True:
        try:
            N = int(input("Введите количество бочонков в мешке: "))
            if N < 1:
                print("Некорректный ввод. Количество бочонков должно быть больше 0.")
            else:
                return N
        except ValueError:
            print("! Ошибка ! Пожалуйста, введите натуральное число.")

def main():
    N = user_interaction()
    logging.info(f'Запуск программы для N = {N}')
    barrel_bag = create_barrel_bag(N)
    random.shuffle(barrel_bag)  # Перемешиваем бочонки

    print("Давайте вытаскивать бочонки из мешка!")

    while barrel_bag:
        input("Нажмите Enter, чтобы вытянуть бочонок...")
        pulled_barrel = pull_barrel(barrel_bag)
        if pulled_barrel:
            print(f"Вы вытянули бочонок с номером: {pulled_barrel}")
            

if __name__ == "__main__":
    main()
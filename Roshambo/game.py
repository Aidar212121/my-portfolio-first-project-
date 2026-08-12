import random

# функция случайного выбора компьютера
def get_computer_choice():
    choices = ["камень", "ножницы", "бумага"]
    return random.choice(choices)

# функция определения победителя
def determine_winner(player, computer):
    if player == computer:
        return "draw"
    elif (player == "камень" and computer == "ножницы") or \
         (player == "ножницы" and computer == "бумага") or \
         (player == "бумага" and computer == "камень"):
        return "player"
    else:
        return "computer"

# основная логика игры
def main():
    player_score = 0
    computer_score = 0

    print("Добро пожаловать в игру Камень-Ножницы-Бумага!")
    print("Правила:")
    print("Камень бьет ножницы")
    print("Ножницы бьют бумагу")
    print("Бумага бьет камень")
    print("Игра идет до 3 очков\n")

    while player_score < 3 and computer_score < 3:
        player_choice = input("Введите камень, ножницы или бумага: ").lower()

        if player_choice not in ["камень", "ножницы", "бумага"]:
            print("Неверный ввод, попробуйте снова.")
            continue

        computer_choice = get_computer_choice()
        print("Компьютер выбрал:", computer_choice)

        result = determine_winner(player_choice, computer_choice)

        if result == "draw":
            print("Ничья!")
        elif result == "player":
            print("Вы выиграли раунд!")
            player_score += 1
        else:
            print("Компьютер выиграл раунд!")
            computer_score += 1

        print("Счет:", player_score, "-", computer_score)
        print()

    print("Финальный счет:", player_score, "-", computer_score)

    if player_score > computer_score:
        print("Поздравляем! Вы победили!")
    else:
        print("Компьютер победил!")

# запуск программы
main()
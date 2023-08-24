import random

LENGTH_OF_SHIPS = [2, 2, 3, 1, 1, 1, 1]
PLAYER_BOARD = [[" "] * 6 for i in range(6)]
COMPUTER_BOARD = [[" "] * 6 for i in range(6)]
PLAYER_GUESS_BOARD = [[" "] * 6 for i in range(6)]
COMPUTER_GUESS_BOARD = [[" "] * 6 for i in range(6)]
LETTERS_TO_NUMBERS = {'А': 0, 'Б': 1, 'В': 2, 'Г': 3, 'Д': 4, 'Е': 5, 'И': 6}


def print_board(board):
    print("  А Б В Г Д Е И")
    print("  +-+-+-+-+-+-+-+")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1


def place_ships(board):
    for ship_length in LENGTH_OF_SHIPS:

        while True:
            if board == COMPUTER_BOARD:
                orientation, row, column = random.choice(["Г", "В"]), random.randint(0, 7), random.randint(0, 7)
                if check_ship_fit(ship_length, row, column, orientation):

                    if ship_overlaps(board, row, column, orientation, ship_length) == False:

                        if orientation == "Г":
                            for i in range(column, column + ship_length):
                                board[row][i] = "X"
                        else:
                            for i in range(row, row + ship_length):
                                board[i][column] = "X"
                        break
            else:
                place_ship = True
                print('Поместите корабль длиной в ' + str(ship_length))
                row, column, orientation = user_input(place_ship)
                if check_ship_fit(ship_length, row, column, orientation):

                    if ship_overlaps(board, row, column, orientation, ship_length) == False:

                        if orientation == "Г":
                            for i in range(column, column + ship_length):
                                board[row][i] = "X"
                        else:
                            for i in range(row, row + ship_length):
                                board[i][column] = "X"
                        print_board(PLAYER_BOARD)
                        break


def check_ship_fit(SHIP_LENGTH, row, column, orientation):
    if orientation == "Г":
        if column + SHIP_LENGTH > 8:
            return False
        else:
            return True
    else:
        if row + SHIP_LENGTH > 8:
            return False
        else:
            return True


def ship_overlaps(board, row, column, orientation, ship_length):
    if orientation == "Г":
        for i in range(column, column + ship_length):
            if board[row][i] == "X":
                return True
    else:
        for i in range(row, row + ship_length):
            if board[i][column] == "X":
                return True
    return False


def user_input(place_ship):
    if place_ship == True:
        while True:
            try:
                orientation = input("Введите координату (Г или В): ").upper()
                if orientation == "Г" or orientation == "В":
                    break
            except TypeError:
                print('Введите подходящую координату Г или В')
        while True:
            try:
                row = input("Введите ряд 1-6: ")
                if row in '123456':
                    row = int(row) - 1
                    break
            except ValueError:
                print('Введите корректный ряд 1-6')
        while True:
            try:
                column = input("Введите коллонну: ").upper()
                if column in 'АБВГДЕИ':
                    column = LETTERS_TO_NUMBERS[column]
                    break
            except KeyError:
                print('Введите подходящий ряд А-И')
        return row, column, orientation
    else:
        while True:
            try:
                row = input("Введите ряд 1-6 : ")
                if row in '123456':
                    row = int(row) - 1
                    break
            except ValueError:
                print('Введите ряд 1-6')
        while True:
            try:
                column = input("Введите коллону : ").upper()
                if column in 'АБВГДЕИ':
                    column = LETTERS_TO_NUMBERS[column]
                    break
            except KeyError:
                print('Введите ряд А-И')
        return row, column


def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count


# user and computer turn
def turn(board):
    if board == PLAYER_GUESS_BOARD:
        row, column = user_input(PLAYER_GUESS_BOARD)
        if board[row][column] == "-":
            turn(board)
        elif board[row][column] == "X":
            turn(board)
        elif COMPUTER_BOARD[row][column] == "X":
            board[row][column] = "X"
        else:
            board[row][column] = "-"
    else:
        row, column = random.randint(0, 7), random.randint(0, 7)
        if board[row][column] == "-":
            turn(board)
        elif board[row][column] == "X":
            turn(board)
        elif PLAYER_BOARD[row][column] == "X":
            board[row][column] = "X"
        else:
            board[row][column] = "-"


print("\n======= Добро пожаловать в Морской Бой =======\n\n")
place_ships(COMPUTER_BOARD)
print_board(PLAYER_BOARD)
place_ships(PLAYER_BOARD)

while True:

    while True:
        print("\n -- Ход игрока --\n")
        print('Угадайте расположение корабля противника\n')
        print_board(PLAYER_GUESS_BOARD)
        turn(PLAYER_GUESS_BOARD)
        break
    if count_hit_ships(PLAYER_GUESS_BOARD) == 17:
        print("Вы выиграли!")
        break

    while True:
        print("\n-- Ход компьютера --\n")
        turn(COMPUTER_GUESS_BOARD)
        break
    print_board(COMPUTER_GUESS_BOARD)
    if count_hit_ships(COMPUTER_GUESS_BOARD) == 17:
        print("К сожалению, выиграл компьютер")
        break
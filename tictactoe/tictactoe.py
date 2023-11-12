
def print_board(cells):
    print("---------")
    for i in range(0, len(cells), 3):
        row = cells[i:i + 3]
        print(f"| {' '.join(row)} |")
def analyze_board(cells):
    x_count = cells.count('X')
    o_count = cells.count('O')

    if abs(x_count - o_count) >= 2:
        return "Impossible"

    rows = [cells[i:i + 3] for i in range(0, len(cells), 3)]
    columns = [cells[i::3] for i in range(3)]
    diagonals = [cells[::4], cells[2:8:2]]

    lines = rows + columns + diagonals

    x_wins = any(line.count('X') == 3 for line in lines)
    o_wins = any(line.count('O') == 3 for line in lines)

    if x_wins:
        return "X wins"
    elif o_wins:
        return "O wins"
    elif '_' not in cells:
        return "Draw"
    else:
        return "Game not finished"

def make_move(cells, coordinates, current_player):
    row, col = coordinates

    if not (1 <= row <= 3) or not (1 <= col <= 3):
        print("Coordinates should be from 1 to 3!")
        return False

    index = (3 - row) * 3 + col - 1

    if cells[index] == '_':
        cells[index] = current_player
        return True
    else:
        print("This cell is occupied! Choose another one!")
        return False

def main():
    cells = ['_'] * 9
    print_board(cells)

    current_player = 'X'

    while True:
        try:
            row, col = map(int, input("Enter the coordinates: ").split())

            if not (1 <= row <= 3) or not (1 <= col <= 3):
                print("Coordinates should be from 1 to 3!")
                continue

            coordinates = (row, col)
        except ValueError:
            print("You should enter numbers!")
            continue

        if make_move(cells, coordinates, current_player):
            print_board(cells)
            result = analyze_board(cells)
            print(result)

            if result.startswith('X') or result.startswith('O') or result == 'Draw':
                break

            current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()

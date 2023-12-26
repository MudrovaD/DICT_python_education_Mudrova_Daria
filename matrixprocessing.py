import numpy as np

def add_matrices(matrix_a, matrix_b):
    # Функція для додавання матриць
    return np.add(matrix_a, matrix_b)

def multiply_matrix_by_constant(matrix, constant):
    # Функція для множення матриці на константу
    return np.multiply(matrix, constant)

def multiply_matrices(matrix_a, matrix_b):
    # Функція для множення матриць
    return np.dot(matrix_a, matrix_b)

def transpose_menu():
    # Функція для меню транспонування
    print("1. Main diagonal\n2. Side diagonal\n3. Vertical line\n4. Horizontal line")
    choice = int(input("Your choice: > "))
    return choice

def transpose_matrix(matrix, transpose_type):
    # Функція для транспонування матриці
    if transpose_type == 1:
        return np.transpose(matrix)
    elif transpose_type == 2:
        return np.flipud(np.fliplr(matrix))
    elif transpose_type == 3:
        return np.fliplr(matrix)
    elif transpose_type == 4:
        return np.flipud(matrix)

def calculate_determinant(matrix):
    # Функція для знаходження визначника матриці
    return round(np.linalg.det(matrix), 2)

def calculate_inverse_matrix(matrix):
    # Функція для знаходження зворотної матриці
    try:
        inverse_matrix = np.linalg.inv(matrix)
        return np.round(inverse_matrix, 2)
    except np.linalg.LinAlgError:
        return None

def read_matrix():
    # Функція для зчитування матриці з користувача
    rows, cols = map(int, input("Enter matrix size: > ").split())
    matrix = []
    print("Enter matrix:")
    for _ in range(rows):
        row = list(map(float, input().split()))
        matrix.append(row)
    return np.array(matrix)

def print_matrix(matrix):
    # Функція для виведення матриці
    print("The result is:")
    for row in matrix:
        print(" ".join(map(str, row)))

def menu():
    # Функція для головного меню
    print("1. Add matrices\n2. Multiply matrix by a constant\n3. Multiply matrices")
    print("4. Transpose matrix\n5. Calculate a determinant\n6. Inverse matrix\n0. Exit")
    choice = int(input("Your choice: > "))
    return choice

if __name__ == "__main__":
    while True:
        try:
            choice = menu()

            if choice == 0:
                break
            elif choice == 1:
                matrix_a = read_matrix()
                matrix_b = read_matrix()

                if len(matrix_a) != len(matrix_b) or len(matrix_a[0]) != len(matrix_b[0]):
                    print("The operation cannot be performed.")
                else:
                    result_matrix = add_matrices(matrix_a, matrix_b)
                    print_matrix(result_matrix)
            elif choice == 2:
                matrix = read_matrix()
                constant = int(input("Enter constant: > "))
                result_matrix = multiply_matrix_by_constant(matrix, constant)
                print_matrix(result_matrix)
            elif choice == 3:
                matrix_a = read_matrix()
                matrix_b = read_matrix()

                if len(matrix_a[0]) != len(matrix_b):
                    print("The operation cannot be performed.")
                else:
                    result_matrix = multiply_matrices(matrix_a, matrix_b)
                    print_matrix(result_matrix)
            elif choice == 4:
                transpose_type = transpose_menu()
                matrix = read_matrix()
                result_matrix = transpose_matrix(matrix, transpose_type)
                print_matrix(result_matrix)
            elif choice == 5:
                matrix = read_matrix()
                determinant = calculate_determinant(matrix)
                print(determinant)
            elif choice == 6:
                matrix = read_matrix()
                inverse_matrix = calculate_inverse_matrix(matrix)

                if inverse_matrix is not None:
                    print_matrix(inverse_matrix)
                else:
                    print("This matrix doesn't have an inverse.")
        except Exception as e:
            print("ERROR")

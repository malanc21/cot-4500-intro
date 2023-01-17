import sys
import numpy as np

def create_matrix(rows, columns):
    # new_matrix = new_array.reshape(rows, columns)
    new_matrix = np.zeros((rows, columns), dtype=int)
    for row in range(rows):
        for column in range(columns):
            if row == column:
                new_matrix[row, column] = 1
    return new_matrix

def add_operation(matrix_for_operation, number_to_add):
    rows = len(matrix_for_operation)
    columns = len(matrix_for_operation[0])
    for row in range(rows):
        for column in range(columns):
            if row != column:
                matrix_for_operation[row, column] += number_to_add
    return matrix_for_operation

def remove_last_column(matrix_for_operation):
    column_to_remove = len(matrix_for_operation[0]) - 1
    matrix_for_operation = matrix_for_operation[:, 0:column_to_remove]
    return matrix_for_operation

def display_matrix(matrix_to_display):
    np.savetxt(sys.stdout, matrix_to_display, fmt="%i")
    print("")

def main():
    # Problem 1
    matrix1 = create_matrix(3, 3)
    display_matrix(matrix1)

    # Problem 2
    matrix2 = add_operation(matrix1, 3)
    display_matrix(matrix2)

    # Problem 3
    matrix3 = remove_last_column(matrix2)
    display_matrix(matrix3)


if __name__ == "__main__":
    main()
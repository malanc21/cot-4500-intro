import unittest
import numpy as np
from src.main.intro_to_python import *

class TestMatrices(unittest.TestCase):
    def test_create_matrix_3x3(self):
        expected_matrix = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        matrix1 = create_matrix(3, 3)
        self.assertTrue(np.array_equal(matrix1, expected_matrix))

    def test_create_matrix_2x3(self):
        expected_matrix = np.array([[1, 0, 0], [0, 1, 0]])
        self.assertTrue(np.array_equal(create_matrix(2, 3), expected_matrix))

    def test_add_3(self):
        expected_matrix = np.array([[1, 3, 3], [3, 1, 3], [3, 3, 1]])
        test_matrix = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        self.assertTrue(np.array_equal(add_operation(test_matrix, 3), expected_matrix))

    def test_remove_last_column(self):
        expected_matrix = np.array([[1, 3], [3, 1], [3, 3]])
        test_matrix = np.array([[1, 3, 3], [3, 1, 3], [3, 3, 1]])
        self.assertTrue(np.array_equal(remove_last_column(test_matrix), expected_matrix))


if __name__ == '__main__':
    unittest.main()

from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        coll = 1
        n = len(matrix)
        m = len(matrix[0])


        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    if j != 0:
                        matrix[0][j] = 0
                    else:
                        coll = 0

        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for j in range(m):
                matrix[0][j] = 0

        if coll == 0:
            for i in range(n):
                matrix[i][0] = 0


def print_matrix(matrix):
    for row in matrix:
        print(row)
    print()


if __name__ == "__main__":
    matrix = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]

    print("Matrix before:")
    print_matrix(matrix)

    sol = Solution()
    sol.setZeroes(matrix)

    print("Matrix after:")
    print_matrix(matrix)

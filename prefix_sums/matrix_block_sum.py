"""
Given a m x n matrix mat and an integer k,
return a matrix answer where each answer[i][j] is the sum of all elements mat[r][c] for:

i - k <=  r <= i + k,
j - k <= c <= j + k, and
(r, c) is a valid position in the matrix.

i  - 1 <= r <= i + 1
j -  1 <= c <= j + 1

i
2 r 4
-1 c 1

1 2 3
4 5 6
7 8 9

Example 1:

Input: mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1
Output: [[12,21,16],[27,45,33],[24,39,28]]
Example 2:

Input: mat = [[1,2,3],[4,5,6],[7,8,9]], k = 2
Output: [[45,45,45],[45,45,45],[45,45,45]]
"""
from typing import List
from pprint import pprint


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:

        # # горизонтально
        # prefix_sums_rows = []
        # for row in mat:
        #     ps = [0]
        #     for сol in range(len(row)):
        #         ps.append(ps[-1] + row[сol])
        #     prefix_sums_rows.append(ps)

        # # вертикально
        # prefix_sums = [[0] * len(prefix_sums_rows[0]) for _ in range(len(prefix_sums_rows))]
        # for col in range(len(prefix_sums_rows[0])):
        #     ps = [0]
        #     for row in range(len(prefix_sums_rows)):
        #         ps.append(ps[-1] + prefix_sums_rows[row][col])
        #         prefix_sums[row][col] = ps[-1]

        m = len(mat[0])  # cols
        n = len(mat)     # rows
        p_sums = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n):
            for j in range(m):
                p_sums[i+1][j+1] = p_sums[i][j+1] + p_sums[i+1][j] - p_sums[i][j] + mat[i][j]

        result = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                r1 = max(0, i - k)
                c1 = max(0, j - k)

                r2 = min(n - 1, i + k)
                c2 = min(m - 1, j + k)

                result[i][j] = p_sums[r2 + 1][c2 + 1] - p_sums[r1][c2 + 1] - p_sums[r2 + 1][c1] + p_sums[r1][c1]

        return result





s = Solution()
# s.matrixBlockSum([[1,2,3],[4,5,6],[7,8,9]], 1)
s.matrixBlockSum(
    [
        [3, 1, 5, 4],
        [1, 2, 3, 2],
        [1, 6, 1, 9],
    ],
    1
)


# https://magma.com/d/N4QkUzpf7V

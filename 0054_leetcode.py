"""54. Spiral Matrix

link: https://leetcode.com/problems/spiral-matrix/

problem: Given an mxn matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def traverse(offset, result):
            n_rows, n_cols = len(matrix), len(matrix[0])

            # move right
            for j in range(offset, n_cols - offset):
                result.append(matrix[offset][j])

            # move down
            for i in range(offset + 1, n_rows - offset):
                result.append(matrix[i][n_cols - offset - 1])

            # move left if we have not already passed by this row as we moved to
            # the right (eg in a 3x4 matrix)
            if offset < n_rows - offset - 1:
                for j in range(offset + 1, n_cols - offset):
                    result.append(matrix[n_rows - offset - 1][n_cols - j - 1])

            # move up if we have not already passed by this column as we moved
            # down (eg in a 3x4 matrix)
            if offset < n_cols - offset - 1:
                for i in range(offset + 1, n_rows - offset - 1):
                    result.append(matrix[n_rows - i - 1][offset])

        result = []
        total_offset = min(len(matrix), len(matrix[0]))
        if total_offset % 2 == 1:
            total_offset = 1 + total_offset // 2
        else:
            total_offset = total_offset // 2
        for offset in range(total_offset):
            traverse(offset, result)
        return result

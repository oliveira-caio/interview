"""73. Set Matrix Zeroes

link: https://leetcode.com/problems/set-matrix-zeroes/

problem: Given an m x n integer matrix matrix, if an element is 0, set its
entire row and column to 0's.

You must do it in place.

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

Constraints:
m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-2^31 <= matrix[i][j] <= 2^31 - 1

Follow up:
A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""


# this is the O(m + n) space solution.
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = [], []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    rows.append(i)
                    cols.append(j)
        for row in rows:
            for j in range(len(matrix[row])):
                matrix[row][j] = 0
        for col in cols:
            for i in range(len(matrix)):
                matrix[i][col] = 0


# follow up (the idea of the constant space solution is using the first row and
# first column to mark if they should be zeroed or not):
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        is_col = False
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                is_col = True
            for j in range(1, len(matrix[i])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if matrix[0][0] == 0:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
        if is_col:
            for i in range(len(matrix)):
                matrix[i][0] = 0

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        def go_up(row, col, result):
            while row >= 0 and col < len(mat[0]):
                result.append(mat[row][col])
                row -= 1; col += 1
            return row, col
                
        def go_down(row, col, result):
            while row < len(mat) and col >= 0:
                result.append(mat[row][col])
                row += 1; col -= 1
            return row, col
        
        num_lines = len(mat) + len(mat[0]) - 1
        result = []
        row, col = 0, 0
        for i in range(num_lines):
            if i % 2:
                row, col = go_down(row, col, result)
                if row < len(mat):
                    col += 1
                else:
                    row -= 1; col += 2
            else:
                row, col = go_up(row, col, result)
                if col < len(mat[0]):
                    row += 1
                else:
                    col -= 1; row += 2
        return result

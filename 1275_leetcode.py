"""1275. Find Winner on a Tic Tac Toe Game

link: https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/

problem: Tic-tac-toe is played by two players A and B on a 3 x 3 grid. The rules
of Tic-Tac-Toe are:

- Players take turns placing characters into empty squares ' '.
- The first player A always places 'X' characters, while the second player B
always places 'O' characters.
- 'X' and 'O' characters are always placed into empty squares, never on filled
ones.
- The game ends when there are three of the same (non-empty) character filling
any row, column, or diagonal.
- The game also ends if all squares are non-empty.
- No more moves can be played if the game is over.

Given a 2D integer array moves where moves[i] = [rowi, coli] indicates that the
ith move will be played on grid[rowi][coli]. return the winner of the game if it
exists (A or B). In case the game ends in a draw return "Draw". If there are
still movements to play return "Pending".

You can assume that moves is valid (i.e., it follows the rules of Tic-Tac-Toe),
the grid is initially empty, and A will play first.

Example 1:
Input: moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
Output: "A"
Explanation: A wins, they always play first.

Example 2:
Input: moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
Output: "B"
Explanation: B wins.

Example 3:
Input: moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
Output: "Draw"
Explanation: The game ends in a draw since there are no moves to make.

Constraints:
1 <= moves.length <= 9
moves[i].length == 2
0 <= rowi, coli <= 2
There are no repeated elements on moves.
moves follow the rules of tic tac toe.
"""


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        def check_row(game):
            if [0, 0, 0] in game:
                return 'A'
            if [1, 1, 1] in game:
                return 'B'
            return False
        
        def check_col(game):
            for x in {0, 1}:
                for j in range(len(game)):
                    count = 0
                    for i in range(len(game)):
                        if game[i][j] == x:
                            count += 1
                    if count == 3:
                        return 'A' if x == 0 else 'B'
            return False
        
        def check_diag(game):
            for x in {0, 1}:
                count_m = count_s = 0
                for i in range(len(game)):
                    if game[i][i] == x:
                        count_m += 1
                    if game[i][-(i + 1)] == x:
                        count_s += 1
                if count_m == 3 or count_s == 3:
                    return 'A' if x == 0 else 'B'
            return False
        
        game = [[-1 for _ in range(3)] for _ in range(3)]
        
        for i, move in enumerate(moves):
            game[move[0]][move[1]] = 1 if i % 2 else 0
                
        row = check_row(game)
        col = check_col(game)
        diag = check_diag(game)
        
        if row or col or diag:
            return row or col or diag
        else:
            for row in game:
                if -1 in row:
                    return 'Pending'
            return 'Draw'

###########################################
# Let's Have Some Fun
# File Name: 348.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Fri Dec 28 20:33:59 2018
###########################################
#coding=utf-8
#!/usr/bin/python
'''
348. Design Tic-Tac-Toe
Design a Tic-tac-toe game that is played between two players on a n x n grid.
You may assume the following rules:
A move is guaranteed to be valid and is placed on an empty block.
Once a winning condition is reached, no more moves is allowed.
A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.

Example:
    Given n = 3, assume that player 1 is "X" and player 2 is "O" in the board.

    TicTacToe toe = new TicTacToe(3);

    toe.move(0, 0, 1); -> Returns 0 (no one wins)
    |X| | |
    | | | |    // Player 1 makes a move at (0, 0).
    | | | |

    toe.move(0, 2, 2); -> Returns 0 (no one wins)
    |X| |O|
    | | | |    // Player 2 makes a move at (0, 2).
    | | | |

    toe.move(2, 2, 1); -> Returns 0 (no one wins)
    |X| |O|
    | | | |    // Player 1 makes a move at (2, 2).
    | | |X|

    toe.move(1, 1, 2); -> Returns 0 (no one wins)
    |X| |O|
    | |O| |    // Player 2 makes a move at (1, 1).
    | | |X|

    toe.move(2, 0, 1); -> Returns 0 (no one wins)
    |X| |O|
    | |O| |    // Player 1 makes a move at (2, 0).
    |X| |X|

    toe.move(1, 0, 2); -> Returns 0 (no one wins)
    |X| |O|
    |O|O| |    // Player 2 makes a move at (1, 0).
    |X| |X|

    toe.move(2, 1, 1); -> Returns 1 (player 1 wins)
    |X| |O|
    |O|O| |    // Player 1 makes a move at (2, 1).
    |X|X|X|

Follow up:
    Could you do better than O(n2) per move() operation?
'''

# brutal method
class TicTacToe1(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.board = []
        for i in range(n):
            self.board.append([0] * n)
        self.n = n

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        self.board[row][col] = player

        # check in row
        tmp = self.board[row][-1]
        for i in range(self.n):
            if self.board[row][i] != tmp: break
        if i == self.n - 1: return player

        # check in col
        tmp = self.board[-1][col]
        for i in range(self.n):
            if self.board[i][col] != tmp: break
        if i == self.n - 1: return player

        # check in diagnal
        if row == col:
            tmp = self.board[-1][-1]
            for i in range(self.n):
                if self.board[i][i] != tmp: break
            if i == self.n - 1: return player

        if row + col == self.n - 1:
            tmp = self.board[-1][0]
            for i in range(self.n):
                if self.board[i][self.n - 1 - i] != tmp: break
            if i == self.n - 1: return player

        return 0

# O(1) move and O(n) space complexity
# if rowArr[row] is n or -n, then row-th is full, game end
# if colArr[col] is n or -n, then col-th is full, game end
class TicTacToe2(object):

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.rowArr = [0] * n
        self.colArr = [0] * n
        self.diag = 0
        self.revDiag = 0
        self.n = n

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        dt = {1:1, 2:-1}
        self.rowArr[row] += dt[player]
        self.colArr[col] += dt[player]
        self.diag += dt[player] if row == col else 0
        self.revDiag += dt[player] if row + col == self.n - 1 else 0
        return player if self.n in [abs(self.rowArr[row]), abs(self.colArr[col]), abs(self.diag), abs(self.revDiag)] else 0

if __name__ == '__main__':
    toe1 = TicTacToe1(3)
    print(toe1.move(0, 0, 1), end=',')
    print(toe1.move(0, 2, 2), end=',')
    print(toe1.move(2, 2, 1), end=',')
    print(toe1.move(1, 1, 2), end=',')
    print(toe1.move(2, 0, 1), end=',')
    print(toe1.move(1, 0, 2), end=',')
    print(toe1.move(2, 1, 1))

    toe2 = TicTacToe2(3)
    print(toe2.move(0, 0, 1), end=',')
    print(toe2.move(0, 2, 2), end=',')
    print(toe2.move(2, 2, 1), end=',')
    print(toe2.move(1, 1, 2), end=',')
    print(toe2.move(2, 0, 1), end=',')
    print(toe2.move(1, 0, 2), end=',')
    print(toe2.move(2, 1, 1))

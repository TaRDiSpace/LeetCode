class Solution(object):

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        def isValid(x, y):
            tmp = board[x][y]
            board[x][y] = 'T'
            # 同一列重复
            for i in range(9):
                if board[i][y] == tmp and i != x:
                    return False
            # 同一行重复
            for i in range(9):
                if board[x][i] == tmp and i != y:
                    return False
            # 九宫格内重复
            for i in range(3):
                for j in range(3):
                    if board[(x // 3) * 3 + i][(y // 3) * 3 + j] == tmp:
                        return False
            board[x][y] = tmp
            return True

        def solve(board):
            for i in range(9):
                for j in range(9):
                    # 格子为空
                    if board[i][j] == '.':
                        for k in '123456789':
                            board[i][j] = k
                            if isValid(i, j) and solve(board):
                                return True
                            # 验证不成功，格子重新为空
                            board[i][j] = '.'
                        return False
            return True

        solve(board)

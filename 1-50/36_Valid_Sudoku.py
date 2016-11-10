class Solution(object):

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        # 列判断
        for i in range(9):
            dic = {}
            for j in range(9):
                if board[i][j] != '.' and board[i][j] in dic:
                    return False
                elif board[i][j] != '.':
                    dic[board[i][j]] = True
                else:
                    pass
        # 行判断
        for i in range(9):
            dic = {}
            for j in range(9):
                if board[j][i] != '.' and board[j][i] in dic:
                    return False
                elif board[j][i] != '.':
                    dic[board[j][i]] = True
                else:
                    pass
        # 九宫格
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                dic = {}
                for x in range(3):
                    for y in range(3):
                        if board[i + x][j + y] != '.' and board[i + x][j + y] in dic:
                            return False
                        elif board[i + x][j + y] != '.':
                            dic[board[i + x][j + y]] = True
                        else:
                            pass
        return True

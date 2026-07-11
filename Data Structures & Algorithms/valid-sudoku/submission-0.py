class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0,9):
            mp=set()
            for j in range(0,9):
                if board[i][j]==".":
                    pass
                else:
                    if board[i][j] in mp:
                        return False
                    mp.add(board[i][j])
            
            m=set()
            for j in range(0,9):
                if board[j][i]==".":
                    pass
                else:
                    if board[j][i] in m:
                        return False
                    m.add(board[j][i])

            mm=set()
            x=(i%3)*3
            y=(i//3)*3
            for a in range(0,3):
                for b in range (0,3):
                    if board[x+a][y+b]!=".":
                        if board[x+a][y+b] in mm:
                            return False
                        mm.add(board[x+a][y+b])
        return True

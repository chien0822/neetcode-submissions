class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check橫
        for i in range(9):
            seen = []
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] not in seen:
                    seen.append(board[i][j])
                else:
                    return False
        #check縱
        for i in range(9):
            seen = []
            for j in range(9):
                if board[j][i] == '.':
                    continue
                if board[j][i] not in seen:
                    seen.append(board[j][i])
                else:
                    return False        
        #check九宮格
        for i in range(3):
            for j in range(3):
                seen = []
                for p in range(i*3, i*3+3):
                    for q in range(j*3, j*3+3):
                        if board[p][q] == '.':
                            continue
                        if board[p][q] not in seen:
                            seen.append(board[p][q])
                        else:
                            return False
        return True



        
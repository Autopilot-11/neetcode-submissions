import math
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        vert = {}
        hori = {}
        box = {}
        for i in range(9):
            for j in range(9):
                # fill the vertical dictionary
                # Different scenarios
                # 1: Repeat num
                # 2: Non-repeat or "."
                # 3: Clear
                if vert.get(board[i][j],None) is not None and board[i][j] != ".":
                    return False
                else:
                    vert[board[i][j]] = 1

            # Clear vert
            vert = {}

            # Check the numbers each row
            for k in range(9):
                
                key = str(k) + str(board[i][k])
                if hori.get(key, None) is not None and board[i][k] != ".":
                    return False
                else:
                    hori[key] = 1
                    
        
            # Check box
            for k in range(9):
                # Key function
                key = str(math.floor(i/3)) + str (math.floor(k/3)) + str(board[i][k])
                if box.get(key, None) is not None and board[i][k] != ".":
                    return False
                else:
                    box[key] = 1

        return True

            



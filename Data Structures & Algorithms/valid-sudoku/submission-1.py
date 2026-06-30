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

                key = str(j) + str(board[i][j])
                if hori.get(key, None) is not None and board[i][j] != ".":
                    return False
                else:
                    hori[key] = 1

                boxkey = str(math.floor(i/3)) + str (math.floor(j/3)) + str(board[i][j])
                if box.get(boxkey, None) is not None and board[i][j] != ".":
                    return False
                else:
                    box[boxkey] = 1

            # Clear vert
            vert = {}

        return True

            



class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # first lets solve row and cols
        # each row and col needs to have counter of 1 per digit

        for r in board:
            c = Counter(r)
            for char, v in c.items():
                if char!= '.' and v>1:
                    return False
        
        all_cols = list(zip(*board))

        for col in all_cols:
            c = Counter(col)
            for char, v in c.items():
                if char!= '.' and v>1:
                    return False

        # now 3 by 3
        subgrids = [
            [cell for row in board[i:i+3] for cell in row[k:k+3]]
            for i in range(0, 9, 3)
            for k in range(0, 9, 3)
            ]
        
        for g in subgrids:
            # print(subgrids)
            c = Counter(g)
            for char, v in c.items():
                if char!= '.' and v>1:
                    return False



        return True
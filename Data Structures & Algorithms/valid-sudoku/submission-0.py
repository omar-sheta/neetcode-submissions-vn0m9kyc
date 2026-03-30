class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = len(board)
        col = len(board[0])

        for row in board:
            c = Counter(row)
            for num, cnt in c.items():
                if num != "." and cnt>=2:
                    # print("row case caught")
                    return False
        
        # zip(*board) flips columns into rows
        for col in zip(*board):
            c = Counter(col)
            for num, cnt in c.items():
                if num != "." and cnt>=2:
                    # print("col case caught")
                    return False

        # 'board' is your 9x9 2D matrix
        for r in range(0, 9, 3):       # Top row of each 3x3 box
            for c in range(0, 9, 3):   # Left column of each 3x3 box
                # Slice 3 rows, then slice 3 columns from each of those rows
                subgrid = [row[c : c+3] for row in board[r : r+3]]
                # print(subgrid)
                # Now use your Counter logic on the subgrid
                # (Tip: Flatten it first if you want to count all 9 numbers at once)
                flat_grid = [num for row in subgrid for num in row]
                c = Counter(flat_grid)
                for num, cnt in c.items():
                    if num != "." and cnt>=2:
                        # print("3x3 case caught")
                        return False

        
        
        return True
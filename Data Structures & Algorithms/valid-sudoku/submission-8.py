class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = len(board)
        col = len(board[0])


        for r in board:
            c = Counter(r)
            for num, cnt in c.items():
                if cnt >= 2 and num != '.':
                    return False
        
        for col in zip(*board):
            # *board unpacks rows into individual arguments
            # zip pairs each item of each row together in order so flipping columns into rows
            c = Counter(col)
            for num, cnt in c.items():
                if cnt >= 2 and num != '.':
                    return False

        # 'board' is your 9x9 2D matrix
        for r in range(0, 9, 3):       # Top row of each 3x3 box
            for c in range(0, 9, 3):   # Left column of each 3x3 box
                # Slice 3 rows, then slice 3 columns from each of those rows
                # for each row in board from r0 to r2
                # get col c0 to c2 giving subgrid 00 to 22 because row is 1d now.
                subgrid = [row[c:c+3] for row in board[r:r+3]]

                # flatten this subgrid using list comprehension
                # for each row in the subgrid return each number in this row.
                flat_grid = [num for row in subgrid for num in row]
                c = Counter(flat_grid)
                for num, cnt in c.items():
                    if num != "." and cnt>=2:
                        # print("3x3 case caught")
                        return False
                


        return True




















        # for row in board:
        #     c = Counter(row)
        #     for num, cnt in c.items():
        #         if num != "." and cnt>=2:
        #             # print("row case caught")
        #             return False
        
        # # zip(*board) flips columns into rows
        # for col in zip(*board):
        #     c = Counter(col)
        #     for num, cnt in c.items():
        #         if num != "." and cnt>=2:
        #             # print("col case caught")
        #             return False

        # # 'board' is your 9x9 2D matrix
        # for r in range(0, 9, 3):       # Top row of each 3x3 box
        #     for c in range(0, 9, 3):   # Left column of each 3x3 box
        #         # Slice 3 rows, then slice 3 columns from each of those rows
        #         subgrid = [row[c : c+3] for row in board[r : r+3]]
        #         # print(subgrid)
        #         # Now use your Counter logic on the subgrid
        #         # (Tip: Flatten it first if you want to count all 9 numbers at once)
        #         flat_grid = [num for row in subgrid for num in row]
        #         c = Counter(flat_grid)
        #         for num, cnt in c.items():
        #             if num != "." and cnt>=2:
        #                 # print("3x3 case caught")
        #                 return False

        
        
        return True
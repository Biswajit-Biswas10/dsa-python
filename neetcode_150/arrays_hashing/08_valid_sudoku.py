

def valid_sudoku(board):

    seen = set()

    for r in range(0, 9):
        for c in range(0, 9):
            val = board[r][c]

            if val == ".":
                continue

            row_tuple = (val, "row", r)
            col_tuple = (val, "col", c)
            box_tuple = (val, "box", r//3, c//3)

            if row_tuple in seen or col_tuple in seen or box_tuple in seen:
                return False
            
            seen.add(row_tuple)
            seen.add(col_tuple)
            seen.add(box_tuple)
    
    return True
                
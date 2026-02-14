"""
Problem Name: Valid Sudoku

Problem Description:
Determine if a 9x9 Sudoku board is valid. Only the filled cells need
to be validated according to the following rules:

1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the nine 3x3 sub-boxes must contain the digits 1-9 without repetition.

Note: A Sudoku board could be valid but is not necessarily solvable.
Only the filled cells need to be validated.

Example 1:
Input: board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
Output: True

Example 2:
Input: board (same as above but with board[0][0] = "8" instead of "5")
Output: False
Explanation: Two 8s in the top-left 3x3 box and column 0.

Approach:

Algorithm (Single Pass with HashSet):
1. Create a single set to track all seen values.
2. Iterate through every cell (row 0-8, column 0-8):
   - If the cell is ".", skip it (empty cell).
   - For each filled cell, create three unique tuples:
     a. Row check:  (value, "row", row_index)
     b. Col check:  (value, "col", col_index)
     c. Box check:  (value, "box", row_index // 3, col_index // 3)
   - If ANY of these tuples already exist in the set, the board is invalid.
   - Otherwise, add all three tuples to the set.
3. If we finish scanning all cells without a duplicate, the board is valid.

Why r//3 and c//3?
- Integer division by 3 maps rows 0-2 to box 0, rows 3-5 to box 1, rows 6-8 to box 2.
- Same logic for columns. This gives each 3x3 box a unique (row_group, col_group) ID.
- e.g. cell (4, 7) → box (4//3, 7//3) = box (1, 2)

Solution: Single Pass HashSet
- Time Complexity:  O(1) - always 81 cells (9x9 board)
- Space Complexity: O(1) - at most 81 * 3 = 243 tuples in the set
"""

from typing import List


def valid_sudoku(board: List[List[str]]) -> bool:
    """
    Determine if a 9x9 Sudoku board is valid.

    Uses a single set to store unique tuples representing
    row, column, and 3x3 box constraints. If a duplicate
    tuple is found, the board is invalid.
    e.g. "5" at row 0 → (5, "row", 0), (5, "col", 0), (5, "box", 0, 0)

    Args:
        board: 9x9 grid of strings ("1"-"9" or "." for empty)

    Returns:
        bool: True if the board is valid, False otherwise
    """
    # Single set to track all row, column, and box entries
    seen = set()

    # Scan every cell in the 9x9 board
    for r in range(0, 9):
        for c in range(0, 9):
            val = board[r][c]

            # Skip empty cells
            if val == ".":
                continue

            # Create unique tuples for row, column, and box checks
            # e.g. val="5", r=0, c=1 → ("5","row",0), ("5","col",1), ("5","box",0,0)
            row_tuple = (val, "row", r)
            col_tuple = (val, "col", c)
            box_tuple = (val, "box", r // 3, c // 3)

            # If any tuple already exists → duplicate found → invalid board
            if row_tuple in seen or col_tuple in seen or box_tuple in seen:
                return False

            # Record all three constraints for this cell
            seen.add(row_tuple)
            seen.add(col_tuple)
            seen.add(box_tuple)

    # No duplicates found → board is valid
    return True


## Test Cases
def test_valid_sudoku():
    """Test cases for valid_sudoku function."""

    # Test 1: Valid Sudoku board
    valid_board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    assert valid_sudoku(valid_board) == True, "Should return True for valid board"
    print("✓ Test 1 passed: Valid Sudoku board")

    # Test 2: Invalid board - duplicate in column and box
    invalid_board = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    assert valid_sudoku(invalid_board) == False, "Should return False for duplicate 8 in col 0"
    print("✓ Test 2 passed: Duplicate in column and box")

    # Test 3: Invalid board - duplicate in row
    row_dup_board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "5"],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    assert valid_sudoku(row_dup_board) == False, "Should return False for duplicate 5 in row 0"
    print("✓ Test 3 passed: Duplicate in row")

    # Test 4: Invalid board - duplicate in 3x3 box
    box_dup_board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", "5", "1", "9", ".", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    assert valid_sudoku(box_dup_board) == False, "Should return False for duplicate 5 in top-left box"
    print("✓ Test 4 passed: Duplicate in 3x3 box")

    # Test 5: Empty board (all dots)
    empty_board = [["." for _ in range(9)] for _ in range(9)]
    assert valid_sudoku(empty_board) == True, "Should return True for empty board"
    print("✓ Test 5 passed: Empty board")

    # Test 6: Minimal valid board - single element
    minimal_board = [["." for _ in range(9)] for _ in range(9)]
    minimal_board[0][0] = "1"
    assert valid_sudoku(minimal_board) == True, "Should return True for single element board"
    print("✓ Test 6 passed: Single element board")

    print("\n✅ All tests passed!")


# Run the tests
if __name__ == "__main__":
    test_valid_sudoku()


# Quick demo
print(valid_sudoku([
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]))

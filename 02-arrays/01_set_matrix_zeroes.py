"""
Problem: Given an m x n integer matrix, if an element is 0, 
set its entire row and column to 0's. Must do it in place.

Pattern: Array / Matrix Manipulation

Approach:
    - If any element/cell in the first row and/or first column is 0, set fRow and fCol to TRUE.
    - Scan the complete matrix row-wise by ignoring the first row and first column, and set 0 
    in the first element of the particular row and column where 0 is found.
    - Check every row's first element, starting from the second row. If it is 0, 
    then set all values in that row to 0.
    - Check every column's first element, starting from the second column. If it is 0, then set 
    all values in that column to 0.
    - If fRow is TRUE, set entire first row to 0. If fCol is TRUE, set entire first column to 0.


Time Complexity: O(m × n) – I scan the matrix multiple times with constant passes.
Where, m and n are the dimensions of the matrix. 
Space Complexity: O(1) – Only using two boolean flags, modifying matrix in-place.
I have used no extra memory space.
"""


from typing import List

def set_to_zeros(matrix: List[List[int]]) -> None:
    """
    Modify the matrix in-place to set entire rows and columns to 0
    wherever a 0 appears in the original matrix.
    
    The algorithm uses the first row and column as markers to track
    which rows and columns should be zeroed, achieving O(1) space complexity.

    Args:
        matrix: 2D list of integers (m x n matrix)

    Returns:
        None: Modifies the matrix in-place
    """
    # Get dimensions of the matrix
    rows = len(matrix)
    cols = len(matrix[0])

    # Step 1: Flags to track if first row or first column have zeros
    # These flags preserve information about original zeros in first row/column
    fRow = False  # Does first row contain a zero?
    fCol = False  # Does first column contain a zero?

    # Step 2: Check if first row has any zeros
    for j in range(cols):
        if matrix[0][j] == 0:
            fRow = True
            break

    # Step 3: Check if first column has any zeros
    for i in range(rows):
        if matrix[i][0] == 0:
            fCol = True
            break

    # Step 4: Use first row and first column as markers
    # Scan the matrix (excluding first row and column)
    # When we find a 0, mark its row and column in the first row/column
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j] == 0:
                matrix[i][0] = 0  # Mark the row (first column)
                matrix[0][j] = 0  # Mark the column (first row)

    # Step 5: Set matrix cells to zero based on markers
    # Process rows and columns starting from index 1
    for i in range(1, rows):
        for j in range(1, cols):
            # If either the row marker or column marker is 0, set cell to 0
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    # Step 6: Handle first row if it originally had zeros
    if fRow:
        for j in range(cols):
            matrix[0][j] = 0

    # Step 7: Handle first column if it originally had zeros
    if fCol:
        for i in range(rows):
            matrix[i][0] = 0


# ────────────────────────────────────────────────
# Demonstration / Manual Tests
# ────────────────────────────────────────────────
if __name__ == "__main__":
    # Test case 1: Standard case with zeros in middle
    matrix1 = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]
    print("Test Case 1: Zeros in the middle")
    print(f"Input:")
    for row in matrix1:
        print(f"  {row}")
    set_to_zeros(matrix1)
    print(f"Output:")
    for row in matrix1:
        print(f"  {row}")
    print()
    print("-" * 50)

    # Test case 2: Multiple zeros
    matrix2 = [
        [0, 1, 2, 0],
        [3, 4, 5, 2],
        [1, 3, 1, 5]
    ]
    print("Test Case 2: Multiple zeros")
    print(f"Input:")
    for row in matrix2:
        print(f"  {row}")
    set_to_zeros(matrix2)
    print(f"Output:")
    for row in matrix2:
        print(f"  {row}")
    print()
    print("-" * 50)

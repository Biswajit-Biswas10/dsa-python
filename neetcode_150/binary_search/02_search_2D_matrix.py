"""
Problem Name: Search 2D Matrix

Problem Description:

You are given an m x n 2-D integer array matrix and an integer target.
* Each row in matrix is sorted in non-decreasing order.
* The first integer of every row is greater than the last integer of the previous row.

Return true if target exists within matrix or false otherwise.
Your solution must run in O(log(m * n)) time.

Example 1:
Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10
Output: true
Explanation: 10 is found in the second row.

Example 2:
Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 15
Output: false
Explanation: 15 does not exist in the matrix.

Constraints:
- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 100
- -10^4 <= matrix[i][j], target <= 10^4

Approach:

Algorithm (Two Binary Searches — Row then Column):
1. If the matrix is empty, return False (nothing to search).
2. Set m = number of rows, n = number of columns.
3. Binary search on ROWS to find which row could contain the target:
   - Initialise two pointers: top = 0, bottom = m - 1.
   - Loop while top <= bottom:
     - Calculate mid_row = (top + bottom) // 2.
     - If target < first column of mid_row → move bottom = mid_row - 1
         → target must be in an earlier row.
     - If target > last column of mid_row → move top = mid_row + 1
         → target must be in a later row.
     - Otherwise, target falls within this row → break.
   - If top > bottom after the loop, no valid row exists. Return False.
4. Binary search on COLUMNS within the found row:
   - Initialise two pointers: left = 0, right = n - 1.
   - Loop while left <= right:
     - Calculate mid = (left + right) // 2.
     - MATCH    (matrix[mid_row][mid] == target): Return True — target found.
     - TOO LOW  (matrix[mid_row][mid] < target):  Set left = mid + 1
         → discard left half, target must be in right half.
     - TOO HIGH (matrix[mid_row][mid] > target):  Set right = mid - 1
         → discard right half, target must be in left half.
5. If the loop ends without returning, the target does not exist.
   Return False.

Why Two Binary Searches work here:
- The matrix is fully sorted: each row is sorted AND the first element of every row is greater than the last element of the
  previous row. This makes the entire matrix a single sorted sequence spread across rows.
- The first binary search eliminates rows — O(log m).
- The second binary search eliminates columns — O(log n).
- Combined: O(log m + log n) = O(log(m * n)).

Visualisation:
    matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]],  target = 10

    ROW SEARCH:
    Step 1:  top=0  bottom=2 → mid_row=1 → row=[10,11,12,13]
             10 >= 10 and 10 <= 13 → target is in row 1 → break

    COLUMN SEARCH (within row 1: [10, 11, 12, 13]):
    Step 1:  left=0  right=3 → mid=1 → matrix[1][1]=11 > 10 → right=0
    Step 2:  left=0  right=0 → mid=0 → matrix[1][0]=10 == 10 → Return True ✓

Solution: Two Binary Searches (Row then Column)
- Time Complexity:  O(log(m * n)) - O(log m) for row + O(log n) for column
- Space Complexity: O(1) - only pointer variables (top, bottom, left, right, mid_row, mid)
"""

from typing import List


def search_matrix(matrix: List[List[int]], target: int) -> bool:
    # base case: empty matrix has nothing to search
    if not matrix:
        return False

    m = len(matrix)  # rows
    n = len(matrix[0]) # columns

    # --- Binary Search on ROWS ---
    top = 0
    bottom = m - 1

    while top <= bottom:
        mid_row = (top + bottom) // 2

        if target < matrix[mid_row][0]:
            # target smaller than first column → search earlier rows
            bottom = mid_row - 1
        elif target > matrix[mid_row][n - 1]:
            # target larger than last column → search later rows
            top = mid_row + 1
        else:
            # target falls within this row's range
            break

    # no valid row contains the target
    if top > bottom:
        return False

    # --- Binary Search on COLUMNS within mid_row ---
    left = 0
    right = n - 1

    while left <= right:
        mid = (left + right) // 2

        if matrix[mid_row][mid] == target:
            # target found → return True
            return True
        elif matrix[mid_row][mid] < target:
            # mid value too low → discard left half
            left = mid + 1
        else:
            # mid value too high → discard right half
            right = mid - 1

    # search space exhausted → target does not exist
    return False


## Test Cases
def test_search_matrix():
    """Test cases for search_matrix function."""

    # Test 1: Target exists in the matrix
    result = search_matrix([[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]], 10)
    assert result == True, f"Expected True, got {result}"
    print("✓ Test 1 passed: Target exists — found 10 in row 1")

    # Test 2: Target does not exist in the matrix
    result = search_matrix([[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]], 15)
    assert result == False, f"Expected False, got {result}"
    print("✓ Test 2 passed: Target missing — 15 not in matrix")

    # Test 3: Single element matrix — found
    result = search_matrix([[5]], 5)
    assert result == True, f"Expected True, got {result}"
    print("✓ Test 3 passed: Single element found — [[5]], target 5")

    # Test 4: Target larger than all elements
    result = search_matrix([[1, 3, 5], [7, 9, 11]], 20)
    assert result == False, f"Expected False, got {result}"
    print("✓ Test 4 passed: Target above range — 20 not in matrix")

    print("\n✅ All tests passed!")


# Run the tests
if __name__ == "__main__":
    test_search_matrix()


print(search_matrix([[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]], 10))
# Output: True

print(search_matrix([[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]], 15))
# Output: False

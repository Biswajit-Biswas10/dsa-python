"""
Problem: Given an integer array `nums` sorted in non-decreasing order, 
return an array of the squares of each number sorted in non-decreasing order.
Pattern: Two Pointers

Approach:
- Since the array is sorted, the largest squares will be at either end
  (most negative or most positive numbers)
- Use two pointers: one at the start (left-start from 0) and one at the end (right-till end n-1)
- Compare the squares of elements at both pointers
- Place the larger square at the current position in the result array
- Fill the result array from right to left (end to start) with the largest squares first
- Move the pointer that had the larger square inward
- Continue until all elements are processed

Time Complexity: O(n) – Iterate through the array exactly once using the while loop
Space Complexity: O(n) – Create a 'result' array of size n to store the output
"""



from typing import List

def sorted_squares(nums: List[int]) -> int:
    """
    Return a sorted array of the squares of the elements in nums.
    
    The input array nums is sorted in non-decreasing order.
    We produce the squares in non-decreasing order without using extra sorting.

    Args:
        nums: Sorted array of integers (non-decreasing order)

    Returns:
        List of squares in sorted (non-decreasing) order
    """
    # Get the length of input array
    n = len(nums)
    # Create a result array filled with zeros, same size as input
    # This will store our final sorted squares
    result = [0] * n
    # Initialize left pointer at the beginning of array (index 0)
    left = 0
    # Initialize right pointer at the end of array (index n-1)
    right = len(nums) - 1
    # Position to fill in result array, starting from the end
    # We fill from right to left(end to start) because we're finding largest squares first
    pos = n - 1


    # Continue until both pointers meet (all elements processed)
    while left <= right:
        # Calculate square of element at left pointer
        left_square = nums[left] ** 2
        # Calculate square of element at right pointer
        right_square = nums[right] ** 2
        # Compare which square is larger
        # We want to place the larger square at the current position
        if left_square > right_square:
            # Left square is bigger, so put it in result array
            result[pos] = left_square
            # Move left pointer one step to the right
            left += 1
        else:
            # Right square is bigger or equal, so put it in result array
            result[pos] = right_square
             # Move right pointer one step to the left
            right -= 1
        # Move to next position in result array (moving left)
        pos -= 1
    # Return the result array with all squared values in sorted order
    return result


# ────────────────────────────────────────────────
# Demonstration / Manual Tests
# ────────────────────────────────────────────────
if __name__ == "__main__":
    # Test case 1: Mix of negative and positive numbers
    nums1 = [-4, -1, 0, 3, 10]
    print(f"Input: {nums1}")
    print(f"Output: {sorted_squares(nums1)}")
    print()
    print("-" * 50)

    # Test case 3: All negative numbers
    nums3 = [-5, -4, -3, -2, -1]
    print(f"Input: {nums3}")
    print(f"Output: {sorted_squares(nums3)}")
    print()
    print("-" * 50)

    # Test case 4: All positive numbers
    nums4 = [1, 2, 3, 4, 5]
    print(f"Input: {nums4}")
    print(f"Output: {sorted_squares(nums4)}")
    print()

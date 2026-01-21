"""
Problem: 03_Remove Element
Pattern: Two Pointers
Approach:
- Use pointer k to mark where to place the next valid element
- Use pointer j to scan through the entire array
- When we find an element that is not equal to val, copy it to position k
- Increment k after each copy
- At the end, k equals the count of valid elements
Time: O(n) - Where n is the length of the array.This is because we iterate over nums only once.
Space: O(1) - Constant extra space (in-place modification). No additional
data structure required regardless of the input size.
"""
from typing import List


def remove_element(nums: List[int], val: int) -> int:
    """
    Remove all occurrences of val in-place and return new length.

    Args:
        nums (List[int]): Input list of integers to modify
        val (int): Value to remove from the list

    Returns:
        int: Number of elements not equal to val
    """
    # Initialize k to track the position for non-val elements
    k = 0

    # Iterate through all elements in the array
    for j in range(len(nums)):
        # If the current element is not equal to val, keep it
        if nums[j] != val:
            # Copy current element to position k (overwrite elements)
            nums[k] = nums[j]
            # Move k pointer forward to next available position
            k += 1

    # Return the count of elements not equal to val
    return k


# ────────────────────────────────────────────────
# Demonstration / Manual Tests
# ────────────────────────────────────────────────
def main() -> None:
    """
    Run manual test cases for the removeElement function.
    """
    nums_arr = [[5, 8, 8, 5, 3],
                [50, 49, 48, 47, 46, 45],
                [0, 0, 0, 0, 1, 0, 0, 0, 0],
                [10, 20, 30, 40, 50],
                [0, 50]]
    val_arr = [5, 48, 0, 25, 0]

    for i in range(len(nums_arr)):
        print(i + 1, ".\tnums: ", nums_arr[i], sep = "")
        print("\tval: ", val_arr[i], sep = "")
        print("\tk:", remove_element(nums_arr[i], val_arr[i]))
        print("-"*100)


if __name__ == "__main__":
    main()
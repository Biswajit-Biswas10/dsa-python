"""
Problem: 04_Remove Duplicates from Sorted Array
Pattern: Two Pointers
Approach:
- Use pointer i to track the last unique element position (start at 0)
- Use pointer j to scan through the array (start at 1)
- When nums[j] is different from nums[i], move i forward and copy nums[j] to nums[i]
- Return i + 1 (count of unique elements)
Time: O(n) - Where n is the length of the array. This is because we iterate over nums only once.
Space: O(1) - Constant extra space (in-place modification). No additional
data structure required regardless of the input size.
"""

from typing import List


def remove_duplicates(nums: List[int]) -> int:
    """
    Remove duplicates from sorted array in-place and return new length.

    Args:
        nums (List[int]): Sorted input list of integers to modify

    Returns:
        int: Number of unique elements
    """
    # Handle edge case: empty or single element array
    if len(nums) <= 1:
        return len(nums)

    # i tracks the position where the next unique element should be placed.
    i = 0

    # Start j from index 1 and iterate through the list to find unique elements.
    for j in range(1, len(nums)):
        # If the current element is different from the last unique element found:
        if nums[j] != nums[i]:
            i += 1                   # Move i forward to store the new unique element
            nums[i] = nums[j]        # Place the unique element in its correct position

    # Return the count of unique elements (index i + 1 because i is zero-based)
    return i + 1


# ────────────────────────────────────────────────
# Demonstration / Manual Tests
# ────────────────────────────────────────────────
def main():
    """
    Run manual test cases for the remove_duplicates function.
    """
    test_cases = [
        [1, 1, 2, 2, 3],
        [-1, -1, 0, 0, 1, 1, 2],
        [5, 5, 5, 5],
        [1, 2, 3, 4],
        [0, 1, 1]
    ]

    for idx, nums in enumerate(test_cases):
        print(idx + 1, ".\tnums:", nums, sep="")
        # print("\tnums:", nums, sep=" ")
        arr = nums.copy()  # because function modifies in-place
        k = remove_duplicates(arr)
        print("\tUnique Count (k):", k)
        print("\tArray After Removing Duplicates:", arr[:k])
        print("-" * 55)

# Run tests
if __name__ == "__main__":
    main()

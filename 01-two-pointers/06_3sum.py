"""
Problem: Given an integer array nums, return all unique triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Pattern: Two Pointers

Approach:
- Sort the array to enable the two-pointer technique
- For each element, use two pointers to find pairs that sum to its negative
- Skip duplicate values to avoid duplicate triplets in the result
- Left pointer starts right after the current element
- Right pointer starts at the end of the array
- If sum < 0, move left pointer forward (increases sum)
- If sum > 0, move right pointer backward (decreases sum)
- If sum == 0, add triplet to result and move both pointers while skipping duplicates

Time Complexity: O(n²) - Sorting the array takes O(n log n)
# The nested iteration takes O(n²)

Space Complexity: O(1) - the algorithm’s space complexity is constant O(1)
# Apart from the space used by the built-in sorting algorithm
"""


from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    """
    Find all unique triplets in the array that sum to zero.
    
    The function uses a two-pointer approach after sorting to efficiently
    find all combinations without duplicates.

    Args:
        nums: List of integers
        
    Returns:
        List of lists containing all unique triplets that sum to zero
    """
    # Initialize result array to store all valid triplets
    result = []

    # Get the length of the input array
    n = len(nums)

    # Step-1: Sort the input array in ascending order
    # This enables the two-pointer technique and helps skip duplicates
    nums.sort()

    # Step-2: Iterate over the array
    # We only need to iterate until n - 2 because we need at least 3 elements
    for i in range(n - 2):
        # Optimization: If current number is greater than 0, break
        # Since array is sorted, all remaining numbers are positive
        # No triplet can sum to zero with all positive numbers
        if nums[i] > 0:
            break


        # Step-3: Skip duplicate values for the first element
        # This prevents duplicate triplets in the result
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # Step-4: Use two pointers to find triplets
        # Low pointer starts right after current element (index i + 1)
        low = i + 1
        # High pointer starts at the end of array (index n - 1)
        high = n - 1

        # Two-pointer approach to find pairs that sum to -nums[i]
        while low < high:
            # Calculate the sum of current triplet
            current_sum = nums[i] + nums[low] + nums[high]

            # Step-5a: If sum is less than 0, move low pointer forward
            # This increases the sum since array is sorted
            if current_sum < 0:
                low += 1

            # Step-5b: If sum is greater than 0, move high pointer backward
            # This decreases the sum since array is sorted
            elif current_sum > 0:
                high -= 1

            # Step-6: Sum equals 0, we found a valid triplet
            else:
                # Add the triplet to result array
                result.append([nums[i], nums[low], nums[high]])

                # Move low pointer forward and skip duplicates
                low += 1
                while low < high and nums[low] == nums[low - 1]:
                    low += 1

                # Move high pointer backward and skip duplicates
                high -= 1
                while low < high and nums[high] == nums[high + 1]:
                    high -= 1

    # Step-7: Return the result array containing all unique triplets
    return result


# ────────────────────────────────────────────────
# Demonstration / Manual Tests
# ────────────────────────────────────────────────
if __name__ == "__main__":
    # Test case-1: Standard case with multiple triplets
    nums1 = [-1, 0, 1, 2, -1, -4]
    print(f"Input: {nums1}")
    print(f"Output: {three_sum(nums1)}")
    print(f"Expected: [[-1, -1, 2], [-1, 0, 1]]")
    print()
    print("-" * 50)

    # Test case-2: No triplets sum to zero
    nums2 = [0, 1, 1]
    print(f"Input: {nums2}")
    print(f"Output: {three_sum(nums2)}")
    print(f"Expected: []")
    print()
    print("-" * 50)

    # Test case-3: All zeros
    nums3 = [0, 0, 0]
    print(f"Input: {nums3}")
    print(f"Output: {three_sum(nums3)}")
    print(f"Expected: [[0, 0, 0]]")
    print()
    print("-" * 50)

    # Test case-4: Array with duplicates
    nums4 = [-2, 0, 1, 1, 2]
    print(f"Input: {nums4}")
    print(f"Output: {three_sum(nums4)}")
    print(f"Expected: [[-2, 0, 2], [-2, 1, 1]]")
    print()
    print("-" * 50)

    # Test case-5: All negative numbers
    nums5 = [-5, -4, -3, -2, -1]
    print(f"Input: {nums5}")
    print(f"Output: {three_sum(nums5)}")
    print(f"Expected: []")
    print()

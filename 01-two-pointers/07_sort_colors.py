"""
Problem: Given an array with n objects colored 0 (red), 1 (white), or 2 (blue), sort them in-place
so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
I use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
Pattern: Two Pointers (Dutch National Flag Algorithm)

Approach:
- Use three pointers: low (for 0s), mid (current element), and high (for 2s)
- Partition the array into three sections: [0...low-1] for 0s, [low...mid-1] for 1s, [high+1...n-1] for 2s
- When mid encounters 0, swap with low and move both pointers forward
- When mid encounters 1, just move mid pointer forward
- When mid encounters 2, swap with high and move high pointer backward
- Continue until mid exceeds high

Time Complexity: O(n) - Single pass through the array
# Traverse the array once with the mid pointer

Space Complexity: O(1) - In-place sorting with constant extra space
# Only using three pointer variables
"""


from typing import List


def sort_colors(colors: List[int]) -> List[int]:
    """
    Sort an array of 0s, 1s, and 2s in-place using the Dutch National Flag algorithm.
    
    The function uses a three-pointer approach to partition the array in a single pass,
    ensuring all 0s come first, followed by 1s, then 2s.

    Args:
        colors: List of integers containing only 0, 1, and 2
        
    Returns:
        The same list sorted in-place with all 0s, 1s, and 2s grouped together
    """
    # Initialize three pointers low/start, mid/current, and high/end
    low= 0
    mid = 0
    high = len(colors) - 1

    # Iterate through the list until the current/mid pointer exceeds the end/high pointer
    while mid <= high:
        if colors[mid] == 0:
            # If the mid/current element is 0 (red), swap it with the element at the low/start pointer
            # This ensures the red element is placed at the beginning of the array
            colors[low], colors[mid] = colors[mid], colors[low]
            # Move both the low and mid pointers one position forward.
            mid += 1
            low += 1

        elif colors[mid] == 1:
            # If the mid/current is 1 (white), just move the current/mid pointer one position forward
            mid += 1

        else:
            # If the current element is 2 (blue), swap it with the element at the end/high pointer
            # This pushes the blue element to the end of the array
            colors[mid], colors[high] = colors[high], colors[mid]
            # Move the end/high pointer one position backward
            high -= 1
    return colors


 #────────────────────────────────────────────────
# Demonstration / Manual Tests
# ────────────────────────────────────────────────
if __name__ == "__main__":
    # Test case-1: Standard case with mixed colors
    colors1 = [2, 0, 2, 1, 1, 0]
    print(f"Input: {colors1}")
    print(f"Output: {sort_colors(colors1.copy())}")
    print(f"Expected: [0, 0, 1, 1, 2, 2]")
    print()
    print("-" * 50)

    # Test case-2: Already sorted array
    colors2 = [0, 0, 1, 1, 2, 2]
    print(f"Input: {colors2}")
    print(f"Output: {sort_colors(colors2.copy())}")
    print(f"Expected: [0, 0, 1, 1, 2, 2]")
    print()
    print("-" * 50)

    # Test case-3: Reverse sorted array
    colors3 = [2, 2, 1, 1, 0, 0]
    print(f"Input: {colors3}")
    print(f"Output: {sort_colors(colors3.copy())}")
    print(f"Expected: [0, 0, 1, 1, 2, 2]")
    print()
    print("-" * 50)

    # Test case-4: All same color (all reds)
    colors4 = [0, 0, 0, 0]
    print(f"Input: {colors4}")
    print(f"Output: {sort_colors(colors4.copy())}")
    print(f"Expected: [0, 0, 0, 0]")
    print()
    print("-" * 50)

    # Test case-5: All same color (all blues)
    colors5 = [2, 2, 2, 2]
    print(f"Input: {colors5}")
    print(f"Output: {sort_colors(colors5.copy())}")
    print(f"Expected: [2, 2, 2, 2]")
    print()
    print("-" * 50)

    # Test case-6: Single element
    colors6 = [1]
    print(f"Input: {colors6}")
    print(f"Output: {sort_colors(colors6.copy())}")
    print(f"Expected: [1]")
    print()
    print("-" * 50)

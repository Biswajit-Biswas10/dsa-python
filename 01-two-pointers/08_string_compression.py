"""
Problem: Given an array of characters, compress it in-place using run-length encoding.
The compressed length must always be smaller than or equal to the original array.
After compressing, return the new length of the array.

Pattern: Two Pointers (Read-Write Pointers)

Approach:
- Use two pointers: read_pos (to scan the array) and write_pos (to write compressed data)
- Scan from left to right, counting consecutive occurrences of each character
- For each group of consecutive characters:
  * Write the character once at write_pos
  * If count > 1, write each digit of the count after the character
- Continue until all characters are processed
- Return write_pos as the new length of the compressed array

Time Complexity: O(n) - Single pass through the array
# where n is the length of the input array
# Traverse each character exactly once with the read pointer

Space Complexity: O(1) - In-place compression with constant extra space
# Only using two pointer variables and a count variable
"""


from typing import List


def compress(chars: List[str]) -> int:
    """
    Compress a character array in-place using run-length encoding.

    The function uses a two-pointer approach to scan and write the compressed
    representation in a single pass, modifying the input array directly.

    Args:
        chars: List of characters to compress in-place

    Returns: 
        int: Length of the compressed array
    
    Example:
        Input: ['a','a','b','b','c','c','c']
        Output: 6, 
        Modified chars: ['a','2','b','2','c','3']
    """
    # Edge case: empty or single character array
    # No compression needed for arrays with 0 or 1 elements
    if len(chars) <= 1:
        return len(chars)

    # Initialize read_pos pointer to scan through the original array
    # This pointer traverses the array to identify consecutive character groups
    read_pos = 0

    # Initialize write_pos pointer to track where to write compressed data
    # This pointer marks the position for the next character or digit to be written
    write_pos = 0

    # Iterate through the entire array until all characters are processed
    while read_pos < len(chars):
        # Store the current character being compressed
        # This is the first character of the current consecutive group
        current_char = chars[read_pos]

        # Count consecutive occurrences of current_char
        # Initialize count to track how many times current_char repeats
        count = 0
        while read_pos < len(chars) and chars[read_pos] == current_char:
            read_pos += 1
            count += 1

        # Write the character once at write_pos
        # Every group is represented by at least the character itself
        chars[write_pos] = current_char
        write_pos += 1

        # If count > 1, write the count's digits after the character
        # Single occurrences don't need a count (implicit count of 1)
        if count > 1:
            # Convert count to string to get individual digits
            # This handles multi-digit counts (e.g., 12 becomes '1', '2')
            count_str = str(count)

            # Write each digit of the count sequentially
            # For count=12, this writes '1' then '2'
            for digit in count_str:
                chars[write_pos] = digit
                write_pos += 1

    # Return the length of the compressed array
    # Elements at indices >= write_pos are disregarded
    return write_pos


#────────────────────────────────────────────────
# Demonstration / Manual Tests
#────────────────────────────────────────────────
if __name__ == "__main__":
    # Test case-1: Standard case with consecutive duplicates
    chars1 = ['a', 'a', 'b', 'b', 'c', 'c', 'c']
    original1 = chars1.copy()
    result1 = compress(chars1)
    print(f"Input: {original1}")
    print(f"Output: {chars1[:result1]} | Length: {result1}")
    print(f"Expected: ['a', '2', 'b', '2', 'c', '3'] | Length: 6")
    print()
    print("-" * 50)

    # Test case-2: No consecutive duplicates (no compression)
    chars2 = ['a', 'b', 'c']
    original2 = chars2.copy()
    result2 = compress(chars2)
    print(f"Input: {original2}")
    print(f"Output: {chars2[:result2]} | Length: {result2}")
    print(f"Expected: ['a', 'b', 'c'] | Length: 3")
    print()
    print("-" * 50)

    # Test case-3: All same characters
    chars3 = ['a', 'a', 'a', 'a', 'a', 'a']
    original3 = chars3.copy()
    result3 = compress(chars3)
    print(f"Input: {original3}")
    print(f"Output: {chars3[:result3]} | Length: {result3}")
    print(f"Expected: ['a', '6'] | Length: 2")
    print()
    print("-" * 50)

    # Test case-4: Mixed pattern with single and multiple occurrences
    chars4 = ['a', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b']
    original4 = chars4.copy()
    result4 = compress(chars4)
    print(f"Input: {original4}")
    print(f"Output: {chars4[:result4]} | Length: {result4}")
    print(f"Expected: ['a', 'b', '1', '2'] | Length: 4")
    print()
    print("-" * 50)

    # Test case-5: Single character
    chars5 = ['a']
    original5 = chars5.copy()
    result5 = compress(chars5)
    print(f"Input: {original5}")
    print(f"Output: {chars5[:result5]} | Length: {result5}")
    print(f"Expected: ['a'] | Length: 1")
    print()
    print("-" * 50)

    # Test case-6: Two consecutive same characters
    chars6 = ['a', 'a']
    original6 = chars6.copy()
    result6 = compress(chars6)
    print(f"Input: {original6}")
    print(f"Output: {chars6[:result6]} | Length: {result6}")
    print(f"Expected: ['a', '2'] | Length: 2")
    print()
    print("-" * 50)

"""
Problem Name: Encode and Decode Strings

Problem Description:
Design an algorithm to encode a list of strings to a single string.
The encoded string is then sent over the network and is decoded back
to the original list of strings.

Machine 1 (sender) has the encode function.
Machine 2 (receiver) has the decode function.
strs2 in Machine 2 should be the same as strs in Machine 1.

Example 1:
Input: ["Hello", "World"]
Encoded: "5#Hello5#World"
Output: ["Hello", "World"]

Example 2:
Input: [""]
Encoded: "0#"
Output: [""]

Example 3:
Input: ["He#llo", "Wor#ld"]
Encoded: "6#He#llo6#Wor#ld"
Output: ["He#llo", "Wor#ld"]

Approach:

Algorithm (Encode):
1. Initialize an empty result string
2. For each word in the input list:
   - Calculate the length of the word
   - Append length + "#" + word to the result
   - e.g. "Hello" becomes "5#Hello"
3. Return the encoded result string

Algorithm (Decode):
1. Initialize an empty result list and a pointer i = 0
2. While i < length of encoded string:
   - Step A: Find the "#" separator starting from position i
   - Step B: Extract the length number from s[i:j]
   - Step C: Extract the actual word using the length
   - Step D: Append the word to result and move the pointer
3. Return the decoded list

Solution: Length-Prefixed Encoding
- Time Complexity: O(n) - where n is the total length of all strings
- Space Complexity: O(n) - storing the encoded/decoded output
"""

from typing import List


def encode(strs: List[str]) -> str:
    """
    Encode a list of strings into a single string.

    Each string is prefixed with its length and a '#' separator.
    e.g. ["Hello", "World"] -> "5#Hello5#World"

    Args:
        strs: List of strings to encode

    Returns:
        str: Encoded single string
    """
    # Initialize empty result string
    if len(strs) < 1:
        return ""
    result = ""

    # For each word, append: length + "#" + word
    # e.g. "Hello" -> "5#Hello", "" -> "0#"
    for word in strs:
        result += str(len(word)) + "#" + word

    return result


def decode(strs: str) -> List[str]:
    """
    Decode a single encoded string back into a list of strings.

    Reads length prefix to know exactly how many characters
    to extract for each word.
    e.g. "5#Hello5#World" -> ["Hello", "World"]

    Args:
        strs: Encoded string to decode

    Returns:
        List[str]: Decoded list of original strings
    """
    # Initialize result list and pointer
    result = []
    i = 0

    # Process until pointer reaches end of string
    while i < len(strs):

        # Step-A: Find the '#' separator starting from position i
        # e.g. "5#Hello..." with i=0, finds '#' at j=1
        j = strs.index("#", i)

        # Step-B: Read the length number
        # Slice from i to j, convert string to integer
        # e.g. strs[0:1] = "5" -> length = 5
        length = int(strs[i:j])

        # Step-C: Extract the actual word
        # Start right after '#', read exactly 'length' characters
        # e.g. strs[2:7] = "Hello"
        start = j + 1
        end = j + 1 + length
        word = strs[start:end]

        # Step-D: Save the word and move pointer forward
        # Pointer moves to the start of the next encoded segment
        result.append(word)
        i = j + 1 + length

    return result




## Test Cases
def test_encode_decode():
    """Test cases for encode and decode functions."""

    # Test 1: Edge case - empty list
    assert decode(encode([])) == [], "Empty list should return []"
    print("✓ Test 1 passed: Empty list")

    # Test 2: Edge case - single empty string
    assert decode(encode([""])) == [""], "[''] should encode and decode back"
    print("✓ Test 2 passed: Single empty string")

    # Test 3: Basic case
    result = decode(encode(["Hello", "World"]))
    assert result == ["Hello", "World"], "Should return ['Hello', 'World']"
    print("✓ Test 3 passed: Basic case")

    # Test 4: Single element repeated
    result = decode(encode(["7", "7"]))
    assert result == ["7", "7"], "Should return ['7', '7']"
    print("✓ Test 4 passed: Single element repeated")

    # Test 5: Strings containing '#' separator
    result = decode(encode(["a#b", "c"]))
    assert result == ["a#b", "c"], "Should handle strings with '#' inside"
    print("✓ Test 5 passed: Strings containing '#'")

    # Test 6: Multiple empty strings
    result = decode(encode(["", "", ""]))
    assert result == ["", "", ""], "Should handle multiple empty strings"
    print("✓ Test 6 passed: Multiple empty strings")

    # Test 7: Strings with spaces
    result = decode(encode(["Hello World", "Foo Bar"]))
    assert result == ["Hello World", "Foo Bar"], "Should handle spaces"
    print("✓ Test 7 passed: Strings with spaces")

    # Test 8: Strings that look like the encoding format
    result = decode(encode(["12#abc", "0#", "#"]))
    assert result == ["12#abc", "0#", "#"], "Should handle tricky strings"
    print("✓ Test 8 passed: Tricky strings resembling encoding format")

    # Test 9: Long string
    result = decode(encode(["abcdefghij" * 40]))
    assert result == ["abcdefghij" * 40], "Should handle long strings"
    print("✓ Test 9 passed: Long string (400 chars)")

    print("\n✅ All tests passed!")


# Run the tests
if __name__ == "__main__":
    test_encode_decode()



print(decode(encode(["Hello", "World"])))
# ['Hello', 'World']

print(decode(encode([""])))
# ['']

print(decode(encode(["He#llo", "Wor#ld"])))
# ['He#llo', 'Wor#ld']

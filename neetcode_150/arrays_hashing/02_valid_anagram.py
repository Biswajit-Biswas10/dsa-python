"""
Problem Name: Valid Anagram

Problem Description:
Given two strings 's' and 't', return 'true' if 't' is an anagram of 's', 
and 'false' otherwise.

An anagram is a word or phrase formed by rearranging the letters of a different 
word or phrase, using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Example 3:
Input: s = "ratrace", t = "carrace"
Output: false

Approach

Algorithm:
1. Handle edge case: if lengths differ, they cannot be anagrams, and return false.
2. Use a hash map to count character frequencies in the first string
3. Iterate through the second string:
   - Decrement the count for each character
   - If count goes negative, character appears more in 't' than 's', return 'false'
4. If I complete the iteration without issues, return 'true'

Solution: Hash Map (Character Frequency Counter)
- Time Complexity: O(n) - where n is the length of the strings
- Space Complexity: O(k) - where k is the number of unique characters in lowercase english letter.  
    (at most 26 for lowercase letters)
"""


def valid_anagram(s: str, t: str) -> bool:
    """
    Check if two strings are valid anagrams of each other.
    
    Args:
        s: First string
        t: Second string
        
    Returns:
        bool: True if 't' is an anagram of 's', False otherwise
    """
    # Handle edge case
    # Anagrams must have the same length
    if len(s) != len(t):
        return False

    # Use a hash map to count character frequencies
    char_map = {}

    # Count frequency of each character in the first string 's'
    for char in s:
        char_map[char] = char_map.get(char, 0) + 1

    # Decrement frequency for each character in the second string 's'
    for char in t:
        char_map[char] = char_map.get(char, 0) - 1
        # If count goes negative, 't' has more of this character than 's'
        if char_map[char] < 0:
            return False

    return True


## Test Cases
def test_valid_anagram():
    """Test cases for valid_anagram function."""

    # Test 1: Empty strings
    assert valid_anagram("", "") == True, "Empty strings should return True"
    print("✓ Test 1 passed: Empty strings")

    # Test 2: Single character - valid anagram
    assert valid_anagram("a", "a") == True, "Same single character should return True"
    print("✓ Test 2 passed: Single character - valid")

    # Test 3: Single character - invalid anagram
    assert valid_anagram("a", "b") == False, "Different single characters should return False"
    print("✓ Test 3 passed: Single character - invalid")

    # Test 4: Valid anagram (TRUE case)
    assert valid_anagram("anagram", "nagaram") == True, "Valid anagram should return True"
    print("✓ Test 4 passed: Valid anagram")

    # Test 5: Invalid anagram - same length (FALSE case)
    assert valid_anagram("rat", "car") == False, "Invalid anagram should return False"
    print("✓ Test 5 passed: Invalid anagram - same length")

    # Test 6: Invalid anagram - different length (FALSE case)
    assert valid_anagram("ratrace", "carrace") == False, "Different lengths should return False"
    print(" Test 6 passed: Invalid anagram - partial match")

    # Additional test cases
    assert valid_anagram("listen", "silent") == True
    assert valid_anagram("hello", "world") == False
    assert valid_anagram("aabbcc", "abcabc") == True

    print("\n✅ All tests passed!")


# Run the tests
if __name__ == "__main__":
    test_valid_anagram()


print(valid_anagram("anagram", "nagaram"))  # True
print(valid_anagram("rat", "car"))          # False
print(valid_anagram("ratrace", "carrace"))  # False

# Exercise 1

"""
You are given a string "allowed" consisting of distinct characters and an array of strings "words". A string is consistent if all characters in the string appear in the string allowed.
Return the number of consistent strings in the array "words".

Example 1:
Input:
	allowed = "ab"
	words = ["ad", "bd", "aaab", "baa", "badab"]
Output: 2
Explanation: Strings "aaab" and "baa" are consistent because they only contain characters 'a' and 'b'. The strings which contain "d" are not consistent because "d" is not allowed.

Example 2:
Input:
    allowed = "abc"
    words = ["a", "b", "c", "ab", "ac", "bc", "abc"]
Output: 7
Explanation: All strings are consistent.

Example 3:
Input:
    allowed = "cad"
    words = ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"]
Output: 4
Explanation: Strings "cc", "acd", "ac", and "d" are consistent. The strings which contain "b" are not consistent because "b" is not allowed.

Reference: https://leetcode.com/problems/count-the-number-of-consistent-strings/description/
"""
from typing import List

# : str means that the variable "allowed" is expected to be a string
# : List[str] means that the variable "words" is expected to be a list of strings
# : int means that the function is expected to return an integer
def countConsistentStrings(allowed: str, words: List[str]) -> int:
    # TODO your code here
    return


# Test cases

# Test case 1
allowed = "ab"
words = ["ad", "bd", "aaab", "baa", "badab"]
output = countConsistentStrings(allowed, words)
print(f"Output: {output}, expected: 2")
# assert checks that the output of your code matches the expected output, in this case 2
assert output == 2

# Test case 2
allowed = "abc"
words = ["a", "b", "c", "ab", "ac", "bc", "abc"]
output = countConsistentStrings(allowed, words)
print(f"Output: {output}, expected: 7")
assert output == 7

# Test case 3
allowed = "cad"
words = ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"]
output = countConsistentStrings(allowed, words)
print(f"Output: {output}, expected: 4")
assert output == 4

# you can add more test cases

# Example exercise

"""

You are given a list of strings words and a character x.
Return an array of indices representing the words that contain the character x.

Example 1:
Input:
	words = ["leet","code"]
	x = "e"
Output: [0,1]
Explanation: "e" occurs in both words: "leet", and "code". Hence, we return indices 0 and 1.

Example 2:
Input:
	words = ["abc","bcd","aaaa","cbc"]
	x = "a"
Output: [0,2]
Explanation: "a" occurs in "abc", and "aaaa". Hence, we return indices 0 and 2.

Example 3:
Input:
	words = ["abc","bcd","aaaa","cbc"]
	x = "z"
Output: []
Explanation: "z" does not occur in any of the words. Hence, we return an empty array.

Reference: https://leetcode.com/problems/find-words-containing-character/
"""
from typing import List

# : List[str] means the variable "words" is expected to be a list of strings
# : str means the variable "x" is expected to be a string
# : List[int] means the function is expected to return a list of integers
def findWordsContaining(words: List[str], x: str) -> List[int]:
	# TODO your code here
	idx = 0
	output = []
    
for word in words:
    if x in word:
        output.append(idx)
output: List[int]

	return output


# Test cases

# Test case 1
words = ["leet", "code"]
x = "e"
output = findWordsContaining(words, x)
print(f"Output: {output}, expected: [0,1]")
assert output == [0, 1]

# Test case 2
words = ["abc", "bcd", "aaaa", "cbc"]
x = "a"
output = findWordsContaining(words, x)
print(f"Output: {output}, expected: [0,2]")
assert output == [0, 2]

# Test case 3
words = ["abc", "bcd", "aaaa", "cbc"]
x = "z"
output = findWordsContaining(words, x)
print(f"Output: {output}, expected: []")
assert output == []

# Test case 4
words = ["beach", ""]

# you can add more test cases

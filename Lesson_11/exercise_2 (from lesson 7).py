# Exercise 2

"""
You are given an array of dictionaries, where each item describes the type, color, and name of the ith item.
You are also given a rule represented by two strings, ruleKey and ruleValue. This matches an item if one of the following is true:
1. ruleKey == "type" and ruleValue is equal to the type of the item.
2. ruleKey == "color" and ruleValue is equal to the color of the item.
3. ruleKey == "name" and ruleValue is equal to the name of the item.

Return the number of items that match the given rule.

Example 1:

Input:
	items = [
		{
			"type": "phone",
			"color": "blue",
			"name": "pixel"
		},
		{
			"type": "computer",
			"color": "silver",
			"name": "lenovo"
		},
		{
			"type": "phone",
			"color": "gold",
			"name": "iphone"
		}
	]
	ruleKey = "color",
	ruleValue = "silver"
Output: 1
Explanation: There is only one item matching the given rule, which is ["computer","silver","lenovo"].

Example 2:

Input:
	items = [
		{
			"type": "phone",
			"color": "blue",
			"name": "pixel"
		},
		{
			"type": "computer",
			"color": "silver",
			"name": "phone"
		},
		{
			"type": "phone",
			"color": "gold",
			"name": "iphone"
		}
	]
	ruleKey = "type",
	ruleValue = "phone"
Output: 2
Explanation: There are only two items matching the given rule, which are ["phone","blue","pixel"] and ["phone","gold","iphone"]. Note that the item ["computer","silver","phone"] does not match.

Reference: https://leetcode.com/problems/count-items-matching-a-rule/description/
"""
from typing import List, Dict

# : str means that the variable is expected to be a string
# : List[Dict[str]] means that the variable is expected to be a list of dictionaries of strings
# : int means that the function is expected to return an integer
def countMatches(items: List[Dict[str]], ruleKey: str, ruleValue: str) -> int:
	# TODO your code here
	return

# Test cases

# Test case 1
items = [
	{
		"type": "phone",
		"color": "blue",
		"name": "pixel"
	},
	{
		"type": "computer",
		"color": "silver",
		"name": "lenovo"
	},
	{
		"type": "phone",
		"color": "gold",
		"name": "iphone"
	}
]

ruleKey = "color"
ruleValue = "silver"
output = countMatches(items, ruleKey, ruleValue)
print(f"Output: {output}, expected: 1")
assert output == 1

# Test case 2
ruleKey = "type"
ruleValue = "phone"
output = countMatches(items, ruleKey, ruleValue)
print(f"Output: {output}, expected: 2")
assert output == 2

# Test case 3
ruleKey = "color"
ruleValue = "white"
output = countMatches(items, ruleKey, ruleValue)
print(f"Output: {output}, expected: 0")
assert output == 0

# you can add more test cases

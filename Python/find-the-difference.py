# Time:  O(n)
# Space: O(1)

# Given two strings s and t which consist of only lowercase letters.
#
# String t is generated by random shuffling string s
# and then add one more letter at a random position.
#
# Find the letter that was added in t.
#
# Example:
#
# Input:
# s = "abcd"
# t = "abcde"
#
# Output:
# e
#
# Explanation:
# 'e' is the letter that was added.

from operator import xor

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        return chr(reduce(xor, map(ord, s), 0) ^ reduce(xor, map(ord, t), 0))

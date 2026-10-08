# LeetCode 242 / NeetCode 150: Valid Anagram (NeetCode name: Is Anagram)
# Difficulty: Easy
# Topic: Arrays & Hashing
# Approach: Fixed-size frequency array of 26 letters, one array for both strings
# Time Complexity: O(n)
# Space Complexity: O(1) because the array size is fixed at 26
# Reference: https://leetcode.com/problems/valid-anagram/
# Credit: Solution written with the help of Claude (Anthropic).


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Two strings of different lengths can never be anagrams,
        # so we reject them immediately and avoid any extra work.
        if len(s) != len(t):
            return False

        # One slot per lowercase letter: index 0 is 'a', index 25 is 'z'.
        # A single array is enough because we add for s and subtract for t.
        counts = [0] * 26

        # Walk both strings together, since we already know the lengths match.
        for a, b in zip(s, t):
            # Add one for the letter from s.
            counts[ord(a) - ord("a")] += 1

            # Subtract one for the letter from t.
            counts[ord(b) - ord("a")] -= 1

        # If every slot returned to zero, each letter appeared the same
        # number of times in both strings, so they are anagrams.
        # Any non-zero slot means one string has a letter the other lacks.
        return not any(counts)

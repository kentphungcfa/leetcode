# LeetCode 217 / NeetCode 150: Contains Duplicate
# Difficulty: Easy
# Topic: Arrays & Hashing
# Approach: Single pass with a hash set
# Time Complexity: O(n)
# Space Complexity: O(n)
# Reference: https://leetcode.com/problems/contains-duplicate/
# Credit: Solution written with the help of Claude (Anthropic).

from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # A set stores each value we have already seen.
        # Membership checks and inserts on a set are O(1) on average.
        seen = set()

        # Scan the list once, from left to right.
        for num in nums:
            # If this value is already in the set, it appeared earlier,
            # so we can stop right away without reading the rest of the list.
            if num in seen:
                return True

            # Otherwise remember it so a later copy can be detected.
            seen.add(num)

        # We finished the scan without meeting any repeat, so all values are distinct.
        return False

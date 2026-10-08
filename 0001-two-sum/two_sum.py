# LeetCode 1 / NeetCode 150: Two Sum (Two Integer Sum)
# Difficulty: Easy
# Topic: Arrays & Hashing
# Approach: Single pass with a hash map from value to index
# Time Complexity: O(n)
# Space Complexity: O(n)
# Reference: https://leetcode.com/problems/two-sum/
# Credit: Solution written with the help of Claude (Anthropic).

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Map each value we have already visited to its index.
        # Lookups and inserts on a dict are O(1) on average.
        seen = {}

        # Scan the list once, from left to right, keeping track of the index.
        for i, num in enumerate(nums):
            # The partner we need so that num + partner == target.
            complement = target - num

            # If the partner was seen earlier, we have the answer.
            # The earlier index is always smaller than i, so the order is correct.
            if complement in seen:
                return [seen[complement], i]

            # Otherwise remember this value and its index for later elements.
            # We store it only after the check so an element never pairs with itself.
            seen[num] = i

        # The problem guarantees exactly one valid pair, so this line is never reached.
        # It is kept so the function always returns a list.
        return []

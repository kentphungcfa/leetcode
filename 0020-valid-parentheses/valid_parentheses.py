# LeetCode 20 / NeetCode 150: Valid Parentheses
# Difficulty: Easy
# Topic: Stack
# Approach: Single pass with a stack
# Time Complexity: O(n)
# Space Complexity: O(n)
# Reference: https://leetcode.com/problems/valid-parentheses/
# Credit: Solution written with the help of Claude (Anthropic).


class Solution:
    def isValid(self, s: str) -> bool:
        # Map each closing bracket to the opening bracket it must match.
        # Keying on the closing bracket lets us look up the expected partner in O(1).
        pairs = {")": "(", "]": "[", "}": "{"}

        # The stack holds opening brackets that are still waiting for a match.
        # The top of the stack is always the most recent unmatched opener.
        stack = []

        # Scan the string once, from left to right.
        for char in s:
            # Case 1: the character is a closing bracket.
            if char in pairs:
                # If the stack is empty, there is nothing to close, so it is invalid.
                # Otherwise pop the latest opener and check it is the right type.
                if not stack or stack.pop() != pairs[char]:
                    return False

            # Case 2: the character is an opening bracket, so wait for its partner.
            else:
                stack.append(char)

        # After the scan, a valid string leaves no unmatched openers behind.
        return not stack

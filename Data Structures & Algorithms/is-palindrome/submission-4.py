class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            # skip non-alphanumeric characters from left
            while l < r and not s[l].isalnum():
                l += 1
            # skip non-alphanumeric characters from right
            while r > l and not s[r].isalnum():
                r -= 1
            # if characters at left and right don't match,
            # not a palindrome
            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1

        return True

        # time complexity: O(n)
        # space complexity: O(1)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""

        for c in s:
            if c.isalnum():
                newStr += c.lower()
        

        return newStr == newStr[::-1]

        # time complexity: O(n)
        # space complexity: O(n)
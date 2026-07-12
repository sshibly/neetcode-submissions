class Solution:
    def firstUniqChar(self, s: str) -> int:

        count = Counter(s)

        for i, c in enumerate(s):
            if count[c] == 1:
                return i
        
        return -1

        # time complexity: O(n)
        # space complexity: O(1)
        #   - since we have at most 26 characters

        
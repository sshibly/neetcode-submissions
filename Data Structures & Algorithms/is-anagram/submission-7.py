from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS = Counter(s)
        countT = Counter(t)
        
        return countS == countT

    # time complexity: O(n) 
    # space complexity: O(n)

        
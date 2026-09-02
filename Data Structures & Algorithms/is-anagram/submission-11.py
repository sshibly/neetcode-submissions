from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS = {}
        countT = {}

        for i in range(len(s)):
            countS[s[i]] = countS.get(s[i], 0) + 1
            countT[t[i]] = countT.get(t[i], 0) + 1
        
        return countS == countT

    # time complexity: O(n + m) 
    # space complexity: O(1) bc we at most have 26 diff characters
    # - n is length of s 
    # - m is length of t
    

        
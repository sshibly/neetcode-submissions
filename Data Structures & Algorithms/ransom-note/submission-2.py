class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        countR = Counter(ransomNote)
        countM = Counter(magazine)

        for k in countR:
            if countR[k] > countM[k]:
                return False
        

        return True

        # time complexity: O(n + m)
        # space complexity: O(1) at most 26 characters
        

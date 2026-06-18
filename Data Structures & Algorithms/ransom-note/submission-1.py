class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        # map letter to count {a:2}
        freqR = defaultdict(int) 
        freqM = defaultdict(int)

        for c in ransomNote:
            freqR[c] += 1
        
        for c in magazine:
            freqM[c] += 1

        for k in freqR:
            if freqR[k] > freqM[k]:
                return False
        
        return True

        # time complexity: O(n + m)
        # space complexity: (1) since at most we have 26 characters
        # n is number of characters in ransomNote
        # m is number of characters in magazine






            
        
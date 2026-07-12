class Solution:
    def scoreOfString(self, s: str) -> int:
        i = 0
        j = 1
        score = 0

        while j < len(s):
            score += abs(ord(s[j]) - ord(s[i]))
            j += 1
            i += 1
        
        return score

        
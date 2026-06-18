class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0 
        longest = 0

        # s="pwwkew"
        #       l
        #         r
        for r in range(len(s)):
            # charset = {k,e}
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r]) # charset = {k,e, w}
            longest = max(longest, r - l + 1) # 3
        return longest 
            



        
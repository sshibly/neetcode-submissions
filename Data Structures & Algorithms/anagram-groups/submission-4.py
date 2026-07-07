from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # maps frequency count to list of anagrams
        hashmap = defaultdict(list) # {(1,0,1...):[act, cat],(1,0,0..):[hat]}

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c)- ord('a')] += 1
            hashmap[tuple(count)].append(s)
        
        return list(hashmap.values())

        # time complexity: O(m * n)
        # space complexity:O(m * n )
        # m is number of strings
        # n is the length of the string
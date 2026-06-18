from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        map = defaultdict(list)

        for s in strs:
            sorted_word = "".join(sorted(s))
            map[sorted_word].append(s)
        
        return list(map.values())
  


        
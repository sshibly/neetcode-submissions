from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        map = defaultdict(list)

        for s in strs:
            word_list = list(s)
            word_list.sort()
            sorted_word = "".join(word_list)
            map[sorted_word].append(s)
        
        res = []

        for val in map.values():
            res.append(val)
        
        return res
  


        
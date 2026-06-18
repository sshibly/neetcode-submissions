from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        map = defaultdict(list)

        # map = {sorted word: [words], sorted word: [words]}
        for word in strs: 
            sorted_word = "".join(sorted(word))
            if sorted_word in map:
                map[sorted_word].append(word)
            else: 
                map[sorted_word].append(word)
        
        for val in map.values():
            result.append(val)

        return result 




            

        
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set("aeiou")

        res = []

        for start, end in queries:
            cnt = 0
            for i in range(start, end + 1):
                if words[i][0] in vowels and words[i][-1] in vowels:
                    cnt += 1
            res.append(cnt)     
        
        return res

        # time complexity: O(n * m)
        # space complexity: O(m)
        # n is number of words, m is number of queries
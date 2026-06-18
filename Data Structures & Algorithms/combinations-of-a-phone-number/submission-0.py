class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return [] 
        digitsToChar = {
            "2": "abc", 
            "3": "def",
            "4": "ghi", 
            "5": "jkl",    
            "6": "mno", 
            "7": "pqrs",
            "8": "tuv", 
            "9": "wxyz",                              
        }
        # curr: current string we're building
        def backtrack(curr, i):
            # we mapped every single digit
            if len(curr) == len(digits):
                ans.append("".join(curr))
                return
            
            for c in digitsToChar[digits[i]]:
                curr.append(c)
                backtrack(curr, i + 1)
                curr.pop()
        
        ans = []
        backtrack([], 0)
        return ans



        
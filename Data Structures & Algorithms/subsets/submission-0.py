class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(curr, i):
            # check if index out of bounds
            if i > len(nums):
                return
            
            # every node is an answer
            ans.append(curr[:])

            # start iterating over elements at i
            for j in range(i, len(nums)):
                curr.append(nums[j])
                # only consider elements after current index
                backtrack(curr, j + 1)
                curr.pop()


        ans = []
        backtrack([], 0)
        return ans



        
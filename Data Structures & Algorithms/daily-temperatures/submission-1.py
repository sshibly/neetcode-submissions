class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # pair: [temp, index]

        #                 0, 1, 2, 3, 4, 5, 6
        #          res = [1, 4, 1, 2, 1, 0, 0]
        # temperatures = [30,38,30,36,35,40,28]
        #                                      ^
        # stack = [[40,5], [28,6]]
        for i, t in enumerate(temperatures): # i = 5
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop() # stackT=38 , stackInd=1
                res[stackInd] = (i - stackInd)
            stack.append([t, i])
        return res

        # time complexity: O(n)
        # space complexity: O()




        
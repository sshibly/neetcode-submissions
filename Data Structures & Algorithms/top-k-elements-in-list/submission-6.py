class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count the occurences of each value
        count = {} 
        
        # array that will be same size as input array
        freq = []
        for i in range(len(nums)+1):
                            # 0 , 1 , 2,  3
            freq.append([]) #[[], [], [], []]

        # build the freq map
        for n in nums: 
            # {num:count, num:count}
            count[n] = count.get(n, 0) + 1

        # loop over count map and populate freq array
        for n, c in count.items():
            # the count is going to be the index of freq
            freq[c].append(n) # this number n occurs c number of times
        
        res = []
        # loop through freq array in descending order
        for i in range(len(freq)-1, 0, -1):
            # loop through the list of the index
            for n in freq[i]: 
                res.append(n)
                if len(res) == k:
                    return res
        

        # time complexity: O(n)
        # space complexity: O(n)
        

        

        

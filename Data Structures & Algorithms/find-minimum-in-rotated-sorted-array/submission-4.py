class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]

        l = 0
        r = len(nums) - 1

        while l <= r:
            
            # check if current array is already sorted
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            mid = (l + r) // 2
            res = min(res, nums[mid])

            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        
        return res

        # time complexity: O(log n)
        # space complexity: O(1)
        
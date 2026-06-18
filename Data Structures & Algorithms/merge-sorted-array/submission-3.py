class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # last index nums1
        last = m + n - 1

        # merge in reverse order
        # nums1 = [2, 2, 2, 3, 5, 6], m = 3
        #       m  l
        # nums2 = [1, 5, 6], n = 3
        #          n
        while m > 0 and n > 0: # m = -1, n = 1
            if nums1[m-1] > nums2[n-1]:
                nums1[last] = nums1[m-1]
                m -= 1
            else:
                nums1[last] = nums2[n-1]
                n -= 1
            last -= 1
        
        # fill nums1 with leftover nums2 elements
        # nums1 = [1, 2, 2, 3, 5, 6], m = 3
        #     m  l
        # nums2 = [1, 5, 6], n = 3
        #        n
        while n > 0: # n = -1
            nums1[last] = nums2[n-1]
            n -= 1
            last -= 1

        # time complexity: O(m + n)
        # space complexity: O(1)
        # m is the number of elements intialized in nums1
        # n is number of elements in nums2

            


        
class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        l = 0 # write pointer - build compressed array 
        r = 0 # read pointer - scan through repeated groups

        while r < n:
            curr_char = chars[r]
            count = 0 # counts repeated characters

            while r < n and curr_char == chars[r]:
                r += 1
                count += 1

            # write curr_char and count
            chars[l] = curr_char
            l += 1

            if count > 1:
                for x in str(count):
                    chars[l] = x
                    l += 1
        
        return l

        # time complexity: O(n)
        # space complexity: O(1)
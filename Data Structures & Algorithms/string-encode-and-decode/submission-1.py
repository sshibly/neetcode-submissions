class Solution:
    # ["neet", "co#de"] -> "4#neet5#co#de"
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        # "4#neet5#co#de"
        #               i
        #         j
        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            word = str(s[j + 1:j + 1 + length])
            res.append(word)
            i = j + 1 + length

        return res

        # Time complexity: O(n)
        # Space complexity O(m + n) for each function





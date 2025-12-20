from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs)
        s0 = strs[0]
        end = len(s0)
        lth = len(strs)
        while len(s0) >= 0:
            tmp_count = len([x for x in strs if x.startswith(s0[:end])])
            if tmp_count == lth:
                return s0[:end]
            else:
                end -= 1


if __name__ == '__main__':
    # strs = ["ab", "a"]
    strs = ["flower","flow","flight"]
    Solution().longestCommonPrefix(strs)

"""
5. 最长回文子串
给你一个字符串 s，找到 s 中最长的回文子串。

如果字符串的反序与原始字符串相同，则该字符串称为回文字符串。



示例 1：

输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
示例 2：

输入：s = "cbbd"
输出："bb"


提示：

1 <= s.length <= 1000
s 仅由数字和英文字母组成
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        lth = len(s)
        if lth == 1:
            return s
        # 指定index
        left = right = 0
        hash_dict = {}
        while right < lth:
            if s[left: right+1] == s[right+1: left][::-1]:
                hash_dict[len(s[left: right+1])] = s[left: right+1]
                right += 1
            else:
                left += 1

if __name__ == '__main__':
    s = "babad"
    Solution().longestPalindrome(s)

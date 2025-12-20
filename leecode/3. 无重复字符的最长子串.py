"""
给定一个字符串 s ，请你找出其中不含有重复字符的最长子串的长度。
示例1:
输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:
输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:
输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是"wke"，所以其长度为 3。
    请注意，你的答案必须是 子串 的长度，"pwke"是一个子序列，不是子串。

提示：
0 <= s.length <= 5 * 104
s由英文字母、数字、符号和空格组成

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/longest-substring-without-repeating-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        lth = len(s)
        if len(s) <2:
            return lth
        out = set()
        max_lth = 0
        while right < lth:
            if s[right] not in out:
                out.add(s[right])
                max_lth = max(max_lth, right - left +1)
                right += 1
            else:
                out.remove(s[left])
                left += 1
        return max_lth


if __name__ == '__main__':
    s = "abcabcbb"
    # s = "bbbb"
    s = "pwwkew"
    # s = "au"
    # s = "a"
    rsp = Solution().lengthOfLongestSubstring(s)
    print("结果为：\n", rsp)

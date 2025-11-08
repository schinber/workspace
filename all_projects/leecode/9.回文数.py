class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x == 0:
            return True
        strs = str(x)
        if strs == strs[::-1]:
            return True
        return False

if __name__ == '__main__':
    xx = 121
    Solution().isPalindrome(xx)
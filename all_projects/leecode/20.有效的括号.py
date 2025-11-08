class Solution:
    def isValid(self, s: str) -> bool:
        kuohao_dict = {")": "(", "}": "{", "]": "["}
        stack = []
        for item in s:
            if item in kuohao_dict:
                if not stack and kuohao_dict.get(item) != stack.pop():
                    return False

            else:
                stack.append(item)

        if not stack:
            return True


if __name__ == '__main__':
    xx = "()"
    content = Solution().isValid(xx)
    print(content)

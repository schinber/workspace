def back_track(digits, index, path):
    word_list = ["0", "0", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv",
                 "wxyz"]
    # 如果是空字符串直接返回空列表
    if digits == "":
        return []
    # 保存结果列表
    result = []
    # 输入的digits的长度，作为回溯函数返回的判断条件
    lenth = len(digits)

    # 回溯函数（path当前路径，默认为""）
    def back_track(digits, index, path):  # 3
        # 如果目前path的长度和digits的长度相等，说明已经遍历完一趟，返回结果列表
        if len(path) == lenth:
            # 加入result列表
            result.append(path)
            # 返回
            return
        # 遍历当前索引的数字对应的英文列表
        for word in word_list[int(digits[index])]:
            # 路径加上当前字母
            path = path + word
            # 递归下一个数字对应的英文列表
            back_track(digits, index + 1, path)
            # 撤销当前字母
            path = path[:-1]


if __name__ == '__main__':
    digits = 23
    back_track(digits, 0, "")

# 作者：gracy
# 链接：https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/solution/hui-su-suan-fa-xiang-xi-zhu-shi-ji-chu-j-5x7b/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

# -*- coding: utf-8 -*-
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    输入：l1 = [2,4,3], l2 = [5,6,4]
    输出：[7,0,8]
    解释：342 + 465 = 807.
    """

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = tree = ListNode
        val = tmp = 0
        while tmp or l1 or l2:
            val = tmp
            if l1:
                val = l1.val + val
                l1 = l1.next
            if l2:
                val = l2.val + val
                l2 = l2.next
            tmp = val // 10
            val = val % 10
            tree.next = ListNode(val)
            tree = tree.next
        return head.next


if __name__ == '__main__':
    l1 = [2, 4, 3]
    l2 = [5, 6, 4]
    Solution.addTwoNumbers(l1, l2)

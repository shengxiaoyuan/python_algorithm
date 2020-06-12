"""
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
k 是一个正整数，它的值小于或等于链表的长度。
如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

示例：
给你这个链表：1->2->3->4->5
当 k = 2 时，应当返回: 2->1->4->3->5
当 k = 3 时，应当返回: 3->2->1->4->5
说明：
你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
"""
from com.algorithm.listode import *
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # 1.正向遍历k个元素
        # 2.将k个元素reverse
        # 3.最后的判断是否后置
        i = 0
        ptr1 = head
        tmp = None
        kBegin, kEnd = None, None
        groupBegin, groupEnd = None, None
        while ptr1:
            if ptr1 and not kBegin:
                kBegin = ptr1
                kEnd = ptr1
                ptr1 = ptr1.next
            else:
                tmp = ptr1.next
                ptr1.next = kBegin
                kBegin = ptr1
                ptr1 = tmp
            i = i + 1
            if i % k == 0:
                if not groupBegin:
                    groupBegin = kBegin
                    groupEnd = kEnd
                    kBegin, kEnd = None, None
                else:
                    groupEnd.next = kBegin
                    groupEnd = kEnd
                    #最后阶段的next一定清空,容易形成死循环
                    groupEnd.next=None
                    kBegin, kEnd = None, None
        # 处理最后微端是否需要再次翻转
        if i % k != 0:
            ptr1 = kBegin
            kBegin = None
            while ptr1:
                if ptr1 and not kBegin:
                    kBegin = ptr1
                    kEnd = ptr1
                    ptr1 = ptr1.next
                else:
                    tmp = ptr1.next
                    ptr1.next = kBegin
                    kBegin = ptr1
                    ptr1 = tmp
            groupEnd.next = kBegin
        return groupBegin
if __name__ == '__main__':
    # printListNode(Solution().reverseKGroup(array_2_list([1, 2, 3, 4, 5]), 2))
    printListNode(Solution().reverseKGroup(array_2_list([1, 2, 3, 4, 5,7,8,11,15]), 4))
    # printListNode(Solution().reverseKGroup(array_2_list([1, 2, 3,4]), 2))

# Definition for singly-linked list.
from com.algorithm.listode import ListNode


class Solution(object):
    def mergeTwoLists(self, node1:ListNode,node2:ListNode) ->ListNode :
        if not node1:
            return node2
        if not node2:
            return node1
        head ,tail=None,None
        while  node1 or node2 :
            if node1 and node2:
                if node1.val <= node2.val:
                    if not head:
                        head=node1
                        tail=node1
                    else:
                        tail.next=node1
                        tail=node1
                    node1=node1.next
                    continue
                else :
                    if not head:
                        head=node2
                        tail=node2
                    else:
                        tail.next=node2
                        tail=node2
                    node2=node2.next
                    continue
            if node1:
                tail.next=node1
                break
            if node2:
                tail.next=node2
                break
        return head
    def mergeKList(self,lists,start,end):
        if start==end:
            return lists[start]
        mid=(start+end)//2
        left = self.mergeKList(lists, start, mid)
        right = self.mergeKList(lists, min(mid + 1, end), end)
        return self.mergeTwoLists(left,right)


if __name__ == '__main__':
    node1 =ListNode(1)
    node1.ap(5).ap(8).ap(12).ap(17).ap(21).ap(205)
    node2  =ListNode(1)
    node2.ap(2).ap(3).ap(14).ap(34).ap(45).ap(100)
    node3  =ListNode(8)
    node3.ap(15).ap(35).ap(201)
    node4  =ListNode(4)
    node4.ap(7).ap(28).ap(467)
    # resultNode = Solution().mergeTwoLists(node1,node2)
    aaa=[node1,node2,node3,node4]
    resultNode = Solution().mergeKList(aaa,0,len(aaa)-1)
    while resultNode:
        print(resultNode.val)
        resultNode=resultNode.next


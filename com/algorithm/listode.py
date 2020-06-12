class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def ap(self,newval):
        list_node = ListNode(newval)
        self.next=list_node
        return  list_node
def array_2_list(array)->ListNode :
    """
    :param array:  [int]
    :return: ListNode
    """
    head=None
    tail=None
    for attr in array:
        if not head:
            head=ListNode(attr)
            tail=head
        else:
            _node=ListNode(attr)
            tail.next=_node
            tail=_node
    return head
def printListNode(head:ListNode):
    while head:
        print(head.val,end=" ")
        head=head.next
    print()
if __name__ == '__main__':
    printListNode(array_2_list([1,4,5,8,2,8]))
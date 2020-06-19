from com.algorithm.tree_node import *
from queue import  Queue
def convert(array:list)->'TreeNode':
    tmpQueue=Queue()
    flag=0
    parent:'TreeNode'=None
    root:'TreeNode'=None
    for i in array:
        nodei=TreeNode(i)
        if not root :
            root=nodei
        if flag==0:
            parent= None  if tmpQueue.empty() else  tmpQueue.get()
            if parent:
                if i!=None:
                    parent.left=nodei
                flag=1
        else:
            if i:
                parent.right=nodei
            flag=0
        tmpQueue.put(nodei)
    return root
def prePrint(node:'TreeNode'):
    if not node:
        return
    print(node.val,end=" ")
    prePrint(node.left)
    prePrint(node.right)
def midPrint(node:'TreeNode'):
    if not node:
        return
    midPrint(node.left)
    print(node.val,end=" ")
    midPrint(node.right)
def postPrint(node:'TreeNode'):
    if not node:
        return
    postPrint(node.left)
    postPrint(node.right)
    print(node.val,end=" ")

if __name__ == '__main__':
    array=[3,5,1,6,2,0,8,None,None,7,4]
    prePrint(convert(array))
    print()
    midPrint(convert(array))
    print()
    postPrint(convert(array))
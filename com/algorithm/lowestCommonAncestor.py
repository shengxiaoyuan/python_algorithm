"""
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]

https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/
示例 1:

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出: 3
解释: 节点 5 和节点 1 的最近公共祖先是节点 3。
示例 2:

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出: 5
解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。
 

说明:

所有节点的值都是唯一的。
p、q 为不同节点且均存在于给定的二叉树中。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


"""
from com.algorithm.tree_node import TreeNode
import com.algorithm.array2Tree as array2Tree
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return
        #很精妙,包括了p q  互为父子的情况
        if root.val==p.val or q.val==root.val:
            return root
        _left=self.lowestCommonAncestor(root.left,p,q)
        _right=self.lowestCommonAncestor(root.right,p,q)
        if _left and _right :
            return root
        if  _left:
            return _left
        if _right:
            return _right
        return
if __name__ == '__main__':
    array=[3,5,1,6,2,0,8,None,None,7,4]
    root=array2Tree.convert(array)
    parent=Solution().lowestCommonAncestor(root,TreeNode(5),TreeNode(1))
    if parent:
        print(parent.val)
    else:
        print("not find")
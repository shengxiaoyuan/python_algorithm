"""
https://leetcode-cn.com/problems/edit-distance/
编辑距离
"""
class Solution(object):

    def minDistance(self, word1, word2):
        l1=len(word1)
        l2=len(word2)
        table=[[0]*l2  for _ in range(l1)]
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        def dp(i,j):
            if i==-1:
                return j+1
            if j==-1:
                return  i+1
            if table[i][j]!=0:
                return table[i][j]
            if word1[i]==word2[j]:
                count=dp(i-1,j-1)
                table[i][j]=count
            else:
                count=min(dp(i,j-1)+1,#插入
                    dp(i-1,j)+1,#删除
                    dp(i-1,j-1)+1# 替换
                    )
                table[i][j]=count
            return table[i][j]
        return dp(l1-1,l2-1)
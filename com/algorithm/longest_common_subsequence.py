##递归方式
def longestCommonSubsequence_1 (str1,str2)->int:
    def dp (i,j):
        if i <0 or j <0:
            return 0
        ##选择 (== or !=),
        if str1[i]==str2[j]:
            #状态转移
            return 1+dp(i-1,j-1)
        else:
            #状态转移
            return max(dp(i-1,j),dp(i,j-1))
    #进行步骤拆分
    return dp(len(str1)-1,len(str2)-1)
def longestCommonSubsequence_2 (str1,str2)->int:
    m,n=len(str1),len(str2)
    dp=[[0]*(n+1) for _ in range(m+1)]
    #步骤拆分
    for i in range(1,m+1):
        for j in range(1,n+1):
            ##选择及状态转移
            if str1[i-1]==str2[j-1]:
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    return dp[i][j]
if __name__ == '__main__':
    # a=[[0 for _ in range(4)] for _ in range(3)]
    # a[2][1]=5
    # print(a)
    str1='akdjkjd'
    str2='lkijhgtssasaddddd'
    print(longestCommonSubsequence_2(str1,str2))

"""
最长的合法括号
"""
class Solution:
    def longestValidParentheses1(self, str1: str) -> int:
        a = []
        count = 0
        maxlength = 0
        i = 0
        while i < len(str1):
            if str1[i] == '(':
                a.append("(")
            if str1[i] == ")":
                j = len(a) - 1
                if j >= 0:
                    val = a[j]
                    matched = False
                    while j >= 0:
                        if a[j] == "(":
                            a.pop(j)
                            a.append("@")
                            matched = True
                            break
                        else:
                            j -= 1
                    if not matched:
                        a.append(")")
                else:
                    maxlength = max(count, maxlength)
                    count = 0
                    a.clear()
            i += 1
        # 后续处理
        if len(a) > 0:
            count = 0
            for ele in a:
                if ele == "@":
                    count += 1
                else:
                    maxlength = max(count, maxlength)
                    count = 0
        maxlength = max(count, maxlength)
        return maxlength * 2

    def longestValidParentheses(self, str1: str) -> int:
        stack=[]
        maxLength=0
        #stack.append(-1)
        for i in range(len(str1)):
            if str1[i]=="(":
                stack.append(i)
            else:
                if len(stack)>0 and str1[stack[len(stack)-1]]=="(":
                    stack.pop(len(stack)-1)
                    length=i-stack[len(stack)-1] if len(stack)>0 else i+1
                    maxLength=max(maxLength,length)
                else:
                    stack.append(i)
        return maxLength
    def longestValidParentheses2(self, str1: str) -> int:
        left,right=0,0
        maxLength=0
        for i in range(len(str1)):
            if str1[i]=="(":
                left+=1
            else:
                right+=1
            if left==right:
                maxLength=max(maxLength,2*right)
            elif right> left:
                left=right=0

        left=0
        right=0
        for i in range(len(str1)-1,-1,-1):
            if str1[i]=="(":
                left+=1
            else:
                right+=1
            if left==right:
                maxLength=max(maxLength,2*left)
            elif left> right:
                left=right=0
        return maxLength
if __name__ == '__main__':
    # print(Solution().longestValidParentheses("()(()"))
    #print(Solution().longestValidParentheses(")()())()()("))
   # print(Solution().longestValidParentheses("()()"))
   # print(1243)
    # for i in range(10,0,-1):
    #     print(i)
    print(Solution().longestValidParentheses2("(()"))
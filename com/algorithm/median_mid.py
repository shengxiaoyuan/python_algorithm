import sys
from com.algorithm.median_k import midk
from com.algorithm.quick_sort import quickSort


class Solution(object):
    def findMedianSortedArrays(self, a, b):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(a) > len(b):
            self.findMedianSortedArrays(b, a)
        la = len(a)
        lb = len(b)
        begin = 0
        end = la
        old = (la + lb) % 2 == 1
        maxleft = sys.maxsize
        minright = -sys.maxsize + 1
        while begin <= end:
            i = (begin + end) // 2
            j = (len(b) + len(a)+1) // 2 - i
            if i > 0 and j < lb and a[i - 1] > b[j]:
                end = i-1
            elif j > 0 and i < la and b[j - 1] > a[i]:
                begin =i+ 1
            else:
                if i == 0:
                    maxleft = b[j - 1]
                elif j == 0:
                    maxleft = a[i - 1]
                else:
                    maxleft = a[i - 1] if a[i - 1] > b[j - 1] else b[j - 1]
                if i == la:
                    minright = b[j]
                elif j == lb:
                    minright = a[i]
                else:
                    minright = a[i] if a[i] < b[j] else b[j]
                if old:
                    #左边比右边多一个元素
                    return maxleft
                else:
                    #左右相等,两边各取一个
                    return (maxleft + minright) / 2
        return 0.0


if __name__ == '__main__':
    a1 = [1, 4, 5, 7, 9, 14,16]
    a2 = [10, 13, 15, 17, 20, 23, 25, 28, 55, 67]
    a3=a1+a2
    print(Solution().findMedianSortedArrays(a1, a2))
    quickSort(a3,0,len(a3)-1)
    print(a3)
    print(midk(a1,a2,(len(a3)+1)//2))


def mergeSort(arry, begin, end):
    if begin == end:
        return [arry[begin]]
    part = int((begin + end) / 2)
    aa = mergeSort(arry, begin, part)
    bb = mergeSort(arry, part + 1, end)
    return merge(aa,bb)


def merge(aa,bb):
    i = 0
    j = 0
    end1=len(aa)-1
    end2=len(bb)-1
    tmpArray = []
    pos = 0;
    while i <= end1 and j <= end2:
        if aa[i] < bb[j]:
            tmpArray.append(aa[i])
            i += 1
        else:
            tmpArray.append(bb[j])
            j += 1
    while i <= end1:
        tmpArray.append(aa[i])
        i += 1
    while j <= end2:
        tmpArray.append(bb[j])
        j += 1
    return tmpArray


if __name__ == '__main__':
    array = [10, 4, 2, 6, 100,200,0,5,2,4, 30, 20, 14]
    print(mergeSort(array, 0, len(array) - 1))

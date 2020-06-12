"""
array: shuzu
begin
end
"""


def quickSort(array, begin, end):
    if begin == end:
        return
    part = divide(array, begin, end)
    quickSort(array, begin, max(begin,part - 1))
    quickSort(array, min(part + 1,end), end)
    ##fen


def divide(array, begin, end):
    i = begin
    j = begin + 1
    tmp = array[begin]
    while j <= end:
        if array[j] > tmp:
            j = j + 1
            continue
        i = i + 1
        itr_tmp = array[i]
        array[i] = array[j]
        array[j] = itr_tmp
        j = j + 1
    # switch
    itr_tmp = array[i]
    array[i] = tmp
    array[begin] = itr_tmp
    return i


if __name__ == '__main__':
    array = [10, 5, 3, 2, 15, 11, 1, 1000, 34, 12, 2, 5]
    quickSort(array, 0, len(array) - 1)
    print(array)

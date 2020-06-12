def repeatQuery(array, start, end, target) -> (int, int):
    if start == end:
        if array[start] == target:
            return start, end
        else:
            return (-1, -1)
    mid = (start + end) // 2
    _start = mid
    _end = mid
    if array[mid] == target:
        left_tuple = repeatQuery(array, start, max(start, mid - 1), target)
        right_tuple = repeatQuery(array, min(mid + 1, end), end, target)
        # merge
        if left_tuple[0] != -1 and left_tuple[0] < mid:
            _start = left_tuple[0]
        if right_tuple[1] != -1 and right_tuple[1] > mid:
            _end = right_tuple[1]
        return (_start, _end)
    else:
        if array[mid] > target:
            return repeatQuery(array, start, max(start, mid - 1), target)
        else:
            return repeatQuery(array, min(mid + 1, end), end, target)


if __name__ == '__main__':
    array = [1, 3, 4, 4, 4, 4, 5, 6]
    print(repeatQuery(array, 0, len(array) - 1, 8))

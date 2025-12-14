def bubble_sort_ultimate(arr):
    """
    顶级优化冒泡排序（工程极限）
    """
    left, right = 0, len(arr) - 1

    while left < right:
        last_right = left
        last_left = right
        swapped = False

        # 从左往右冒泡（最大值右移）
        for i in range(left, right):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
                last_right = i

        right = last_right

        # 从右往左冒泡（最小值左移）
        for i in range(right, left, -1):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                swapped = True
                last_left = i

        left = last_left

        if not swapped:
            break


if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]
    print("原始数据:", data)
    print("排序结果:", bubble_sort_ultimate(data))

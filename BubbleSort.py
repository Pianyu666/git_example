def bubble_sort(arr):
    """
    冒泡排序（记录最后交换位置优化）
    """
    arr = arr.copy()
    n = len(arr)

    while n > 1:
        last_swap = 0
        for i in range(1, n):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                last_swap = i
        n = last_swap  # 下一轮只需遍历到最后交换的位置

    return arr



if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]
    print("原始数据:", data)
    print("排序结果:", bubble_sort(data))

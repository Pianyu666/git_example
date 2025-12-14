def bubble_sort(arr):
    """
    冒泡排序
    :param arr: 待排序的列表
    :return: 排序后的新列表
    """
    n = len(arr)
    arr = arr.copy()  # 不修改原列表

    for i in range(n):
        # 提前结束优化：如果一轮中没有发生交换，说明已经有序
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

    return arr


if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]
    print("原始数据:", data)
    print("排序结果:", bubble_sort(data))

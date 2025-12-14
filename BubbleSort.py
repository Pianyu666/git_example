def bubble_sort_inplace(arr):
    """
    原地冒泡排序
    """
    arr = arr.copy()
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break



if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]
    print("原始数据:", data)
    print("排序结果:", bubble_sort_inplace(data))

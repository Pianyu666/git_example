def cocktail_sort(arr):
    """
    鸡尾酒排序（双向冒泡）
    """
    arr = arr.copy()
    left, right = 0, len(arr) - 1

    while left < right:
        swapped = False

        for i in range(left, right):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        right -= 1

        for i in range(right, left, -1):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                swapped = True
        left += 1

        if not swapped:
            break

    return arr

if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]
    print("原始数据:", data)
    print("排序结果:", cocktail_sort(data))

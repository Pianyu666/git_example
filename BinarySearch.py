from typing import List

def binary_search(arr: List[int], target: int) -> int:
    """
    二分查找（要求数组已排序）
    :param arr: 已排序的列表
    :param target: 要查找的目标值
    :return: 目标值的索引，不存在则返回 -1
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


if __name__ == "__main__":
    data = [1, 3, 5, 7, 9, 11, 13, 15]
    target = 7

    index = binary_search(data, target)
    if index != -1:
        print(f"找到 {target}，索引为 {index}")
    else:
        print(f"未找到 {target}")

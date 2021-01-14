def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] < target:
        return binary_search(array, target, mid + 1, end)
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)


if __name__ == "__main__":
    n, target = map(int, input().split())
    array = list(map(int, input().split()))

    result = binary_search(array, target, 0, len(array) - 1)
    if not result:
        print("No Answer")
    else:
        print(f"The Value find in {result + 1}")

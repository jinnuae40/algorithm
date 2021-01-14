# 1,5,2,3,6
# 바뀐게 바뀌기 전보다 클 수 있기 때문에 mid를 제외할 수 없어
# pivot은 고정이야 값을 넣은거니까 배열의 주소가 아니라
def quick_sort(arr):
    def sort(low, high):
        if low > high:
            return
        mid = partition(low, high)
        partition(low, mid - 1)
        partition(mid, high)

    def partition(low, high):
        pivot = arr[(low + high) // 2]
        while low <= high:
            while arr[low] < pivot:
                low += 1
            while arr[high] > pivot:
                high -= 1
            if low <= high:
                arr[low], arr[high] = arr[high], arr[low]
                low, high = low + 1, high - 1
        return low
    sort(0, len(arr) - 1)


if __name__ == "__main__":
    arr = [1, 5, 2, 3]
    quick_sort(arr)
    print(arr)

def quick_sort(arr):
    """Use Quick sort to sort an array in ascending order."""

    if len(arr) <= 1:
        return arr

    pivot = arr[0]

    lesser_than_pivot = []
    greater_than_pivot = []

    for value in arr[1:]:
        if value <= pivot:
            lesser_than_pivot.append(value)
        else:
            greater_than_pivot.append(value)

    return quick_sort(lesser_than_pivot) + [pivot] + quick_sort(greater_than_pivot)


given_list = [23, 45, 12, 90, 34, 55, 76, 32, 82, 31, 10, 89]
sorted_list = quick_sort(given_list)
print(sorted_list)


def verify_sorted(arr):
    if len(arr) <= 1:
        return True
    return arr[1] > arr[0] and verify_sorted(arr[2:])


print(verify_sorted(sorted_list))

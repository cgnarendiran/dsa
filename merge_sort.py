def merge_sort(arr):
    """Sort a given array in ascending order."""
    # divide
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left, right = arr[:mid], arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    """Merge the sorted arrays."""
    merged_list = []

    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged_list.append(left[left_index])
            left_index += 1
        else:
            merged_list.append(right[right_index])
            right_index += 1

    merged_list += left[left_index:]
    merged_list += right[right_index:]

    return merged_list


given_list = [23, 45, 12, 90, 34, 55, 76, 32, 82, 31, 10, 89]
sorted_list = merge_sort(given_list)
print(sorted_list)


def verify_sorted(arr):
    if len(arr) <= 1:
        return True
    return arr[1] > arr[0] and verify_sorted(arr[2:])


print(verify_sorted(sorted_list))

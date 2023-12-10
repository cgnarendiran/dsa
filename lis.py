def lis(arr, current_index):
    """Get the length of the longest icreasing subsequence."""

    if current_index == 0:
        return 1

    lis_list = []

    for lower_index in range(current_index - 1, -1, -1):
        if arr[lower_index] < arr[current_index]:
            lis_list.append(lis(arr, lower_index))

    if lis_list:
        return 1 + max(lis_list)
    else:
        return 1


arr = [50, 3, 10, 7, 40, 80, 2, 3, 4, 5, 6, 7, 8, 40, 50, 70]

print("LIS: ", lis(arr, len(arr) - 1))

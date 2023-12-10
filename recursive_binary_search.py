def recursive_binary_search(input_list, target, first, last):
    """Recursive binary search algo."""

    # stopping condition
    if first > last:
        return None

    midpoint = (first + last) // 2

    if input_list[midpoint] == target:
        return midpoint
    if input_list[midpoint] > target:
        return recursive_binary_search(input_list, target, first, midpoint - 1)
    return recursive_binary_search(input_list, target, midpoint + 1, last)


input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 8

result = recursive_binary_search(input_list, target, 0, len(input_list) - 1)

print("Target is at index: ", result)

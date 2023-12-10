def binary_search(input_list, target):
    """Iterative binary search algo."""
    first = 0
    last = len(input_list) - 1

    while first <= last:
        midpoint = (first + last) // 2
        if input_list[midpoint] == target:
            return midpoint
        if input_list[midpoint] > target:
            last = midpoint - 1
        else:
            first = midpoint + 1

    return None


input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 8

result = binary_search(input_list, target)

print("Target is at index: ", result)

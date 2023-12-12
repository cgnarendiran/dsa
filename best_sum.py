def how_sum(target_sum, numbers, memo=None):
    """Return the combination of numbers that yield the target sum if it's possible o/w return None."""

    if memo is None:
        memo = {}

    if target_sum == 0:
        return []
    if target_sum < 0:
        return None
    
    if target_sum in memo:
        return memo[target_sum]
    
    shortest_result = None
    for num in numbers:
        result = how_sum(target_sum - num, numbers, memo)
        if result is not None:
            result = result + [num]
            if shortest_result is None:
                shortest_result = result
                continue
            if len(result) < len(shortest_result):
                shortest_result = result

    memo[target_sum] = shortest_result
    return shortest_result


print(how_sum(7, [2, 3]))
print(how_sum(7, [5, 3, 4, 7]))
print(how_sum(7, [2, 4]))
print(how_sum(8, [2, 3, 5]))
print(how_sum(300, [7, 14]))
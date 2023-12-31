def can_sum(target_sum, numbers, memo=None):
    """Check if it's possible to get the target sum from the array."""

    if memo is None:
        memo = {}
    
    if target_sum == 0:
        return True
    if target_sum < 0:
        return False
    
    if target_sum in memo:
        return memo[target_sum]
    
    for num in numbers:
        if can_sum(target_sum - num, numbers, memo) is True:
            memo[target_sum] = True
            return True
    
    memo[target_sum] = False
    return False


print(can_sum(7, [2, 3]))
print(can_sum(7, [5, 3, 4, 7]))
print(can_sum(7, [2, 4]))
print(can_sum(8, [2, 3, 5]))
print(can_sum(300, [7, 14]))
def can_construct(target, strings):
    """Check if the target is possible to obtain by using the strings."""

    if target == '':
        return True
    
    if memo is None:
        memo = {}

    if target in memo:
        return memo[target]
    
    for string in strings:
        if target.startswith(string):
            stripped_target = target.lstrip(string)
            if can_construct(stripped_target, strings):
                memo[target] = True
                return True
    
    memo[target] = False
    return False


print(can_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
print(can_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
print(can_construct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))
print(can_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee']))
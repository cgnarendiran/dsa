def djb2(key):
    # Start from an arbitrary large prime
    hash_value = 5381

    # Bit-shift and sum value for each character
    for char in key:
        hash_value = (hash_value << 5) + hash_value + ord(char)

    return hash_value


hash_value = djb2("example1")
print(hash_value)

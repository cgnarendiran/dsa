def boyer_moore_search(text, pattern):
    """
    Boyer-Moore string search algorithm implementation.
    
    :param text: The text to search within
    :param pattern: The pattern to search for
    :return: The index of the first occurrence of the pattern in the text, or -1 if not found
    """
    def build_bad_char_table(pattern):
        """
        Builds the bad character table. This table is a dictionary where each character in the pattern
        is mapped to its rightmost occurrence in the pattern, measured from the right end of the pattern.
        If a character is not in the pattern, it is mapped to -1.
        """
        bad_char = {}
        for i in range(len(pattern)):
            bad_char[pattern[i]] = i
        return bad_char

    # Lengths of pattern and text
    m = len(pattern)
    n = len(text)

    # Build the bad character table
    bad_char = build_bad_char_table(pattern)

    s = 0  # s is the shift of the pattern with respect to text
    while(s <= n - m):
        j = m - 1

        # Keep reducing index j of pattern while characters of pattern and text are matching
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1

        # If the pattern is present at the current shift, return the index
        if j < 0:
            return s

            # Shift the pattern so that the bad character in text aligns with the last occurrence of it in pattern
            # The max function is used to make sure that we get a positive shift
            # If the character is not in the bad character table, we use -1
            s += (m - bad_char.get(text[s + m], -1))
        else:
            # Shift the pattern so that the bad character in text aligns with the last occurrence of it in pattern
            s += max(1, j - bad_char.get(text[s + j], -1))
    
    return -1  # Pattern not found

# Example usage
text = "ABAAABCDBBABCDDEBCABC"
pattern = "ABC"

# Function call
index = boyer_moore_search(text, pattern)
index

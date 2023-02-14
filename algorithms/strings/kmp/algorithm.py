def compute_longest_prefix_suffix(pattern):
    lps = [0] * len(pattern)

    j, i = 0, 1
    while i < len(pattern):
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
            i += 1

        else:
            if j != 0:
                j = lps[j-1]
            else:
                # lps[i] = 0
                i += 1
    return lps


def find_pattern_in_text(text, pattern):
    lps = compute_longest_prefix_suffix(pattern)

    i = j = 0
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1

        if j == len(pattern):
            print('found a match', i-j)

        elif i < len(text) and text[i] != pattern[j]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1



pattern = 'aabaaac'
text = 'aabaaabaaac'

print(find_pattern_in_text(text, pattern))

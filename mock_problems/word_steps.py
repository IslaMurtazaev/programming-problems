# Given two strings s1 and s2, we will call (s1, s2) a "step" if you can form s2 by adding exactly one letter to s1 and possibly rearranging the letters of s1.

# For example:
# (OF, FOR) is a step
# (OF, IF) is not a step
# (OF, OCT) is not a step
# (ERA, EAR) is not a step
# (SHE, SHEEP) is not a step
# (TEE, TEST) is not a step

# Given a wordlist, produce an index
#    w -> {  w1 | (w, w1) is a step }
# that associates to each word all the words in the wordlist that are a step away from it.

counts = [
    "POINT,333858038",
    "NOT,4522732626",
    "INTO,1144226142",
    "ON,4594521081",
    "FOR,6545282031",
    "NOW,679337516",
    "ONE,2148983086",
    "BEHAVIOR,104177552",
    "WAITS,2911079",
    "PEOPLE,658716166",
    "HI,15453893",
    "FORM,352032932",
    "OF,30966074232",
    "THROUGH,647091198",
    "BETWEEN,744064796",
    "FOUR,262968583",
    "LEFT,306802162",
    "OFF,302535533",
    "FROM,3469207674",
    "NO,1400645478",
    "FORMS,136468034",
    "A,45916054218"
]

# index = step_index(wordlist)

# # Expected output (pseudocode, unordered):

# NO     : [ ONE, NOT, NOW ]
# INTO   : [ POINT ]
# LEFT   : []
# FORM   : [ FORMS ]
# ONE    : []
# FOUR   : []
# FOR    : [ FORM, FOUR, FROM ]
# FROM   : [ FORMS ]
# OFF    : []
# FORMS  : []
# NOT    : [ INTO ]
# OF     : [ FOR, OFF ]
# NOW    : []
# POINT  : []
# ON     : [ ONE, NOT, NOW ]

# Complexity analysis variables:
# n: The number of words in the word list.
# k: The maximum length of any word in the word list


# approach
# step 1: split the word in input
# for each word take a count of each letter (dict<word, dict<letter, freq>>)

"""
result = dict()
for each word:
    for each other word:
        check if counter(other word) has one  more char than counter(word):
            result[word].append(other word)



# NO     : [ ONE, NOT, NOW ]
NO = {N: 1, O: 1}
ONE = {N: 1, O: 1, E: 1}

def helper function to check if word1 exceeds word2 by 1 char
    exceeded_letter = False
    check freq of each letter:
        if freq matches:
            continue
        if letter in other word exceeds by 1 and not exceeded_letter:
            exceeded_letter = True
        else:
            return False


"""
import collections


def exceeds_by_1(word1, word2):
    # K
    count1 = collections.Counter(word1)
    count2 = collections.Counter(word2)

    exceeded = False
    for letter in count2.keys():
        if count1[letter] == count2[letter]:
            del count1[letter]
            continue

        if count2[letter] == count1[letter] + 1 and not exceeded:
            del count1[letter]
            exceeded = True
        else:
            return False

    return exceeded and len(count1.keys()) == 0


def build_word_steps(counts):
    # take just words
    words = []
    for count in counts:
        words.append(count.split(',')[0])

    result = dict()

    # TC = O(N ^ 2 * k)
    # SC = O(N ^ 2 * K)

    for word1 in words:
        result[word1] = []
        for word2 in words:
            if word1 == word2:
                continue

            if exceeds_by_1(word1, word2):
                result[word1].append(word2)

    return result


print(build_word_steps(counts))

# Start with 2 words, eg NO and POINT. A "ladder" is a set of "steps" that connects the words.

# For example, this is a ladder:

# NO -> NOT -> INTO -> POINT

# Write a function that takes 2 words, the index, and the 15-word wordlist and returns the "best" ladder that connects them, if any exists. The "best" ladder is the one that maximizes the sum of the occurrence counts of each word in the ladder, as found in the original download.

# ladder('NO', 'POINT', index, wordlist) -> ['NO', 'NOT', 'INTO', 'POINT']
# ladder('OF', 'FORMS', index, wordlist) -> [ 'OF', 'FOR', 'FROM', 'FORMS ]
# ladder('ON', 'LEFT', index, wordlist) -> None

# Complexity analysis variables:

# n: Number of words
# e: number of edges between words in index


"""
{'POINT': [], 'NOT': ['INTO'], 'INTO': ['POINT'], 'ON': ['NOT', 'NOW', 'ONE'], 'FOR': ['FORM', 'FOUR', 'FROM'], 'NOW': [], 'ONE': [], 'BEHAVIOR': [], 'WAITS': [], 'PEOPLE': [], 'HI': [], 'FORM': ['FORMS'], 'OF': ['FOR', 'OFF'], 'THROUGH': [], 'BETWEEN': [], 'FOUR': [], 'LEFT': [], 'OFF': [], 'FROM': ['FORMS'], 'NO': ['NOT', 'NOW', 'ONE'], 'FORMS': [], 'A': []}

NO -> POINT

               NO
            /  |.  \
    ['NOT', 'NOW', 'ONE']
      /\

Use dfs
BASE CASE IF WE REACH THE SAME LENGTH OF END word if we found the word we return max of children paths

"""

from math import inf


def build_ladder(src, dst, next_steps, occurence):
    if src == dst:
        return [dst], occurence[dst]
    if len(src) == len(dst):
        return [], -inf

    max_result = -inf
    best_path = []
    for next_step in next_steps[src]:
        path, occurence_sum = build_ladder(next_step, dst, next_steps, occurence)
        if occurence_sum + occurence[src] > max_result:
            max_result = occurence_sum + occurence[src]
            best_path = [src] + path

    return best_path, max_result


next_steps = build_word_steps(counts)

occurences = dict()
for count in counts:
    word, freq = count.split(',')
    occurences[word] = int(freq)

# print(next_steps, occurences)
# print()
# print(build_ladder("NO", "POINT", next_steps, occurences))
print(build_ladder("OF", "FORMS", next_steps, occurences))

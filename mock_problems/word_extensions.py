"""
Implement spell checking for words with extensions.
You have access to isInDict(s) function which returns whether the word is in the dictionary.
Return true if the full word is in the dictionary or if the shortened word is in the dictionary. Otherwise return false.
It’s guaranteed that no word in the dictionary contains extensions.

Example

Assume,
isInDict(“hello”) = true
isInDict(“abc”) = false

Then,
isValid(“hello”) -> true
isValid(“hellloooo”) -> true
isValid(“abc”) -> false
"""

"""
isInDict, there are no valid words with 3 same consecutive letters

"hello" => 0 extensions => return isInDict(“hello”)

"hellloooo" => remove 3+ consecutive letters => "helloo" => isInDict(any("helo", "heloo", "hello", "helloo"))

                             he
                             /\
                          l    ll
                         /\     /\
                        o oo   o  oo

TC = tree O(2^n) * copy of input O(n) => 2^n^2
SC = data stored in one branch O(n^2)
"""


def isInDict(word: str) -> bool:
    """dummy function to test"""
    print(word)
    return word in ["hello", "cat", "dog"]


def isValid(input: str) -> bool:
    """
    recursive function that starts at whole input

    find next extension:
        return isInDict(input with next extension = 1) or isInDict(input with next extension = 2)
    if no next extension:
        return isInDict(input)
    """

    for i in range(len(input)-2):
        # found an extension
        if input[i] == input[i+1] and input[i] == input[i+2]:
            start = i
            end = i + 2
            while end + 1 < len(input) and input[end] == input[end + 1]:
                end += 1

            return isValid(input[:start] + input[end:]) or isValid(input[:start+1] + input[end:])

    return isInDict(input)


assert isValid("hellloooo") is True
assert isValid("dddooooggg") is True
assert isValid("cccccaaaat") is True
assert isValid("caaatt") is False
assert isValid("dogggy") is False
assert isValid("ccaaaaat") is False

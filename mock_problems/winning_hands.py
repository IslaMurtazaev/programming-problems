"""
[1,1,2,3,4,5,5,5,6,6,6,9,9,9]

You win or lose

pair: 2,2
street: 3,3,3
sequences: 1,2,3

to win: 1 pair and 4 streets and/or sequences

1,1
2,3,4
5,5,5
6,6,6
9,9,9


Game where you receive 14 cards.
Want to know if you can win the game by making hands with the following possibilities.

pair: [11, 22...]
set: [111, 222, 333]
street: [123, 456, 789]

To win, you need 1 pair and 4 sets and/or streets.
And have to use all 14 cards.

[1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5] → [11, 123, 123, 444, 555]

counter {
    1: 4
    2: 2
    3: 2
    4: 3
    5: 3
}

use backtracking
take each key and use it as a pair:
    remaining values are sent to sets/streets recursion function -> that validates that all values can be used to build 4 triplets

triplet_builder(counter):
    use first value as set and triplet_builder(remaining part)
    use first value as street and triplet_builder(remaining part)
    return True if one of the above statements works else False
"""

from collections import Counter


def can_win(cards):
    counter = Counter(cards)

    for key, value in counter.items():
        if value < 2:
            continue

        counter[key] -= 2
        if check_triplets(counter):
            return True
        counter[key] += 2

    return False


def check_triplets(counter):
    if is_empty(counter):
        return True

    counter_copy = counter.copy()
    if remove_street(counter_copy) and check_triplets(counter_copy):
        return True

    counter_copy = counter.copy()
    if remove_set(counter_copy) and check_triplets(counter_copy):
        return True

    return False


def is_empty(counter):
    for value in counter.values():
        if value > 0:
            return False
    return True


def remove_street(counter):
    for key in counter.keys():
        has_street = all([counter[i] > 0 for i in range(key, key+3)])

        if has_street:
            for i in range(key, key+3):
                counter[i] -= 1
            return True

    return False


def remove_set(counter):
    for key, value in counter.items():
        if value >= 3:
            counter[key] -= 3
            return True
    return False


assert(can_win([1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5]))
assert(not can_win([1, 1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 4, 5]))
assert(can_win([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))
assert(can_win([1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 1]))
assert(can_win([1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 1]))
assert(can_win([1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2]))
assert(can_win([1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2]))
assert(can_win([1, 2, 3, 2, 3, 4, 3, 4, 5, 4, 5, 6, 6, 6]))
print('all test cases passed...')


"""
Questions and insights I expected to hear: 
Can we use one card in multiple combinations?
We should use all 14 cards to collect all combinations.
It looks like we can break down the problem into subproblems -> maybe use recursion here.
It's easier to start with 1 pair and then do recursive steps for 4 sets/streets.
We might have chosen the wrong pair, so we need some way to backtrack and choose another one.
"""

# We are building a word processor and we would like to implement a "reflow"
# functionality that also applies full justification to the text.

# Given an array containing lines of text and a new maximum width,
# re-flow the text to fit the new width. Each line should have the exact specified width.
# If any line is too short, insert '-' (as stand-ins for spaces) between words
# as equally as possible until it fits.

# Note: we are using '-' instead of spaces between words
# to make testing and visual verification of the results easier.


# n = number of words OR total characters

lines = ["The day began as still as the", "night abruptly lighted with", "brilliant flame"]

"""
clarification:
* dashes are added from left to right
* n >= shortest word


Algorithm
1. join all lines in input
2. split out words into lines of max length of n (with at least one space)
    * iterate thorough string and put fitting to N words into a new line
3. fill in gaps between words with dashes (from left to right)
    * calculate spaces for number of words in current line -> add dashes
"""


# implementation:
# def reflowAndJustify(lines, line_length):
#     # step1:
#     words = " ".join(lines).split()
#
#     # step 2:
#     lines = []
#     line = []
#     current_line_length = 0
#     for word in words:
#         # check if this word fits current line
#         if not line:
#             line.append(word)
#             current_line_length = len(word) + 1
#             continue
#
#         if current_line_length + len(word) > line_length:
#             lines.append(line.copy())
#             line = []
#             current_line_length = 0
#
#         line.append(word)
#         current_line_length += len(word) + 1
#
#     if line:
#         lines.append(line)
#
#     # step 3:
#     # first find the number of spaces between words and number of increased spaces
#     result = []
#     for line in lines:
#         # line = [The, day, began], line_length = 14
#         # number_of_chars = 11
#         # 14 - 11 = 3 number of dashes
#         # 3 / (number of words - 1)
#         # 3 / 2 = 1
#         # 3 % 2 = 1 (remainder that we need to distribute)
#         # The--day-began
#
#         # [word]
#         number_of_letters = sum(len(word) for word in line)  # 11
#         number_of_spaces = line_length - number_of_letters  # 3
#
#         if len(line) > 1:
#             space_length = number_of_spaces // (len(line) - 1)  # 14 / 1
#             left_spaces = number_of_spaces % len(line)  #
#
#         new_line = [line[0]]
#         for i in range(1, len(line) - 1):
#             new_line.append('-' * space_length)
#             if left_spaces > 1:
#                 new_line.append('-')
#                 left_spaces -= 1
#             new_line.append(line[i])
#
#         result.append(''.join(new_line))
#     return result



def reflowAndJustify(lines, line_length):
    """
    second attempt

    Algorithm
    1. join all lines in input
    2. split out words into lines of max length of n (with at least one space)
        * iterate thorough string and put fitting to N words into a new line
    3. fill in gaps between words with dashes (from left to right)
        * calculate spaces for number of words in current line -> add dashes
    """





lines = ["The day began as still as the",
         "night abruptly lighted with",
         "brilliant flame"]

# All Test Cases:
print(reflowAndJustify(lines, 24))
# reflowAndJustify(lines, 25)
# reflowAndJustify(lines, 26)
# reflowAndJustify(lines, 40)
# reflowAndJustify(lines, 14)

# reflowAndJustify(lines, 24) "reflow lines and justify to length 24" =>
# [ "The--day--began-as-still",
#   "as--the--night--abruptly",
#   "lighted--with--brilliant",
#   "flame" ] // <--- a single word on a line is not padded with spaces

# reflowAndJustify(lines, 25) "reflow lines and justify to length 25" =>
#         [ "The-day-began-as-still-as"
#           "the-----night----abruptly"
#           "lighted---with--brilliant"
#           "flame" ]

# reflowAndJustify(lines, 26) "reflow lines and justify to length 26" =>
#         [ "The--day-began-as-still-as",
#           "the-night-abruptly-lighted",
#           "with----brilliant----flame" ]

# reflowAndJustify(lines, 40) "reflow lines and justify to length 40" =>
#         [ "The--day--began--as--still--as-the-night",
#           "abruptly--lighted--with--brilliant-flame" ]

# reflowAndJustify(lines, 14) "reflow lines and justify to length 14" =>
#         ['The--day-began',
#          'as---still--as',
#          'the------night',
#          'abruptly',
#          'lighted---with',
#          'brilliant',
#          'flame']

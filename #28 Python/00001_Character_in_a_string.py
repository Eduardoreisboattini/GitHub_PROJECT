#Python
# Code to count the number of occurrences of a character in a string:
def count_char(string, char):
    count = 0
    for c in string:
        if c == char:
            count += 1
    return count
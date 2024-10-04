#Numbers from 1 to 10
# Example of using list comprehension to generate a list of even numbers from 1 to 10:
string = "the quick brown fox jumps over the lazy dog"
words = string.split()
word_freq = {}

for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

# Example output
print(word_freq) # Output: {'the': 2, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1}
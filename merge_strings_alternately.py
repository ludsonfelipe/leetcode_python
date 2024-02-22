# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.


# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"

# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"

def merge_words(word1, word2):
    lenght_w1 = len(word1)
    lenght_w2 = len(word2)

    min_word = min(word1, word2, key=len)
    max_word = max(word1, word2, key=len)

    out = ''

    print(min_word, max_word)
    if lenght_w1 != lenght_w2:
        for index in range(len(min_word)):
            out += word1[index]
            out += word2[index]
        diff = len(max_word)-len(min_word)
        out += max_word[-diff:]

    else:
        for index in range(len(word1)):
            out += word1[index]+word2[index]


word1 = "abcrxss"
word2 = "pqrs"

merge_words(word1, word2)

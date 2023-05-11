def countWords(words1: list[str], words2: list[str]) -> int:
    union = words1+words2
    for word in union:
        if union.count(word) > 2:
            try:
                words1.remove(word)
                words2.remove(word)
            except:
                continue

    return len(set(words1).intersection(set(words2)))


word1 = ['b', 'bbb', 'bbbb','b','a']
word2 = ['a','b','aaa']

print(countWords(words1 = word1, words2 = word2))
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


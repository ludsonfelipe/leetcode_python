def groupAnagrams(strs: list[str]) -> list[list[str]]:
    list_of_dicios = []

    for word in strs:
        size_word = len(word)
        dicio = {}
        for letter in word:
            dicio[letter] = word.count(letter)
        
        list_of_dicios.append((size_word, dicio))

    #for dicio in list_of_dicios:

    
    
    
#groupAnagrams(["eat","tea","tan","ate","nat","bat"])
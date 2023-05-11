def checkDistances(s: str, distance: list[int]) -> bool:
    unique_letters = [letter for letter in s]
    unique_letters = sorted(set(unique_letters))
    alphabet = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9, 'k':10, 'l':11, 'm':12, 'n':13, 'o':14, 'p':15, 'q':16, 'r':17, 's':18, 't':19, 'u':20, 'v':21, 'w':22, 'x':23, 'y':24, 'z':25}
    dicio = {}
    for letter in unique_letters:
        for n in range(s.count(letter)):
            first_index = s.index(letter)
            second_index = s.index(letter, first_index+1)
            dicio[letter]=(second_index-(first_index+1))
        
    for key, value in dicio.items():
        if distance[alphabet[key]] == dicio[key]:
            print(distance[alphabet[key]], dicio[key])
        else:
            print(distance[alphabet[key]], dicio[key])
            return False 
    return True



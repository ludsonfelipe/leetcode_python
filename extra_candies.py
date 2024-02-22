# Input: candies = [2,3,5,1,3], extraCandies = 3
# Output: [true,true,true,false,true]


candies = [2, 3, 5, 1, 3]
extraCandies = 3


def extracandies(candies, extraCandies):
    max_candy = max(candies)
    lista = []
    for candy in candies:
        if candy+extraCandies >= max_candy:
            lista.append(True)
        else:
            lista.append(False)
    return lista


extracandies(candies, extraCandies)

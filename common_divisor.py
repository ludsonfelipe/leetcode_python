from math import gcd

str1 = "ADADCCBBCBDCDDBABCBBADADCCBBCBDCDDBABCBBADADCCBBCBDCDDBABCBBADADCCBBCBDCDDBABCBBADADCCBBCBDCDDBABCBBADADCCBBCBDCDDBABCBBADADCCBBCBDCDDBABCBBADADCCBBCBDCDDBABCBBADADCCBBCBDCDDBABCBBADADCCBBCBDCDDBABCBBADADCCBBCBDCDDBABCBBADADCCBBCBDCDDBABCBBADADCCBBCBDCDDBABCBBADADCCBBCBDCDDBABCBBADADCCBBCBDCDDBABCBBADADCCBBCBDCDDBABCBBADADCCBBCBDCDDBABCBBADADCCBBCBDCDDBABCBB"
str2 = "ADADCCBBCBDCDDBABCBBADADCCBBCBDCDDBABCBBADADCCBBCBDCDDBABCBBADADCCBBCBDCDDBABCBBADADCCBBCBDCDDBABCBBADADCCBBCBDCDDBABCBBADADCCBBCBDCDDBABCBBADADCCBBCBDCDDBABCBBADADCCBBCBDCDDBABCBBADADCCBBCBDCDDBABCBBADADCCBBCBDCDDBABCBBADADCCBBCBDCDDBABCBBADADCCBBCBDCDDBABCBBADADCCBBCBDCDDBABCBBADADCCBBCBDCDDBABCBBADADCCBBCBDCDDBABCBBADADCCBBCBDCDDBABCBBADADCCBBCBDCDDBABCBBADADCCBBCBDCDDBABCBBADADCCBBCBDCDDBABCBBADADCCBBCBDCDDBABCBBADADCCBBCBDCDDBABCBBADADCCBBCBDCDDBABCBBADADCCBBCBDCDDBABCBBADADCCBBCBDCDDBABCBBADADCCBBCBDCDDBABCBBADADCCBBCBDCDDBABCBBADADCCBBCBDCDDBABCBBADADCCBBCBDCDDBABCBBADADCCBBCBDCDDBABCBBADADCCBBCBDCDDBABCBBADADCCBBCBDCDDBABCBB"


def gcdOfStrings(self, str1: str, str2: str) -> str:

    max_str = max(str1, str2, key=len)
    min_str = min(str1, str2, key=len)
    lenght_min = len(min_str)
    lenght_max = len(max_str)
    code = ''

    mult_ = lenght_max//lenght_min

    if str1 == str2:
        return str1
    elif len(str1) == len(str2) and str1 != str2:
        return ""
    elif set(str1) == set(str2) and len(set(str1)) == 1:
        n = gcd(len(str1), len(str2))
        return n*str1[0]
    elif min_str*mult_ == max_str:
        return min_str
    else:
        for letter in min_str:
            code += letter
            lenght_code = len(code)

            mult = lenght_min//lenght_code
            mult2 = lenght_max//lenght_code

            if code*mult == min_str and code*mult2 == max_str:
                n = gcd(mult, mult2)
                return code*n

            elif code == min_str and code*mult2 != max_str:
                return ""

            elif lenght_code == lenght_min and code != min_str:
                return ""


gcdOfStrings(str1, str2)

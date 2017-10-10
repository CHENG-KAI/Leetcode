def repeatedSubstringPattern(str):
    return str in (2 * str)[1:-1]
    
str = "12345"
repeatedSubstringPattern(str)

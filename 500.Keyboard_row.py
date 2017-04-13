def findWords(words):
    line1, line2,line3 = set("qwertyuiop"),set("asdfghjkl"),set("zxcvbnm")
    a = []
    for i in words:
        if set(i.lower()).issubset(line1) or set(i.lower()).issubset(line2) or set(i.lower()).issubset(line3):
            a.append(i)
    return a 
    
    
    
words = ["Hello", "Alaska", "Dad", "Peace"]
print findWords(words)
    

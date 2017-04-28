def mySqrt(x):
    
    x = x**0.5
    y = int(x)
    if x-y > 0:
        return False
    return True

print mySqrt(5)
            

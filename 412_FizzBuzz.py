def fizzBuzz(n):
    res = []
    for i in range(1,n+1):
        if i % 3 == 0:
            res.append("Fizz")
        elif i % 5 == 0:
            res.append("Buzz")
        elif i % 3 == 0 and i % 5 == 0:
            res.append("FizzBuzz")
        else:
            res.append(i)
    return res
n = 15
print fizzBuzz(n)

def even_fibonacci(n, a=1,b=2):
    
    if n == 1:
        return 0 
            
    elif n == 2:
        return 2

    else:
        i = 1
        even_sum = 2

        while i != n-1:
            i += 1
            c = a + b
            a = b
            b = c
            
            if c%2 == 0:
                even_sum += c
        
        return even_sum


assert even_fibonacci(10) == 44
assert even_fibonacci(1) == 0
assert even_fibonacci(2) == 2

print(even_fibonacci(4000))

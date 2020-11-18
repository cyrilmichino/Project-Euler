def sum_primes(n):
    
    summation = 0

    for a in range(2,n):  
        for i in range(2,a+1):
            if a%i == 0:
                if i != a:
                    break
                else:
                    summation += i

    return summation


assert sum_primes(10) == 17
assert sum_primes(100) == 1060
print(sum_primes(200000))


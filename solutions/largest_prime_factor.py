def largest_prime(n):
    "Output the largest prime factor of a number"
    
    i = 2
    while n != 1:
        for i in range(2,n+1):
            if n%i == 0:
                n = int(n/i)
                p = i
                break
            else:
                pass

    return p


#The following function is unncessary and only here to confirm if the previous function output is prime
def is_prime(n):
    "Determine if a number is a prime number or not"
    for i in range(2,n+1):
        if n%i == 0:
            if i != n:
                return "Not Prime"
            else:
                return "Prime"


assert largest_prime(13195) == 29
assert largest_prime(100) == 5
print(largest_prime(600851475143))
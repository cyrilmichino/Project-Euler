import math


def special_pythagorean(n):

    for a in range(1,n//2):
        
        for b in range(1,n//2):
            c = math.sqrt(a**2 + b**2)
            
            if a + b + c == n:
                
                return (a,b,c)

    return None


assert special_pythagorean(12) == (3,4,5)
assert special_pythagorean(30) == (5,12,13)
print(special_pythagorean(1000))

        
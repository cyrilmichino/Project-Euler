def largest_palindrome_product(digit_num):
    
    pals = list()

    for i in range(1,10**digit_num):
        for j in range(1,10**digit_num):
            n = (10**digit_num-i)*(10**digit_num-j)

            p = ""

            for i in range(1,len(str(n))+1):
                p = p +  str(n)[-i]

                if p == str(n):
                    pals.append(n)

    largest_pal = 0
    
    for _ in pals:
        if _ > largest_pal:
            largest_pal = _

    return largest_pal

    
assert largest_palindrome_product(3) == 90909
assert largest_palindrome_product(2) == 9009
print(largest_palindrome_product(1))
    
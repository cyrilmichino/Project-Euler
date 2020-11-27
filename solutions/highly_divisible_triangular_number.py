def triangle_numbers(divisors):
    nterm = 0
    i = 0
    count = []

    while len(count) != divisors:
        i += 1
        nterm += i

        for i in range(1,nterm + 1):
            if nterm%i == 0:
                count.append(i)

        return nterm

print(triangle_numbers(5))
def sum_multiples(n):
    multiple_sum = 0

    for i in range(1,n):
        if (i%3 == 0) or (i%5 == 0):
            multiple_sum += i

    return multiple_sum


assert sum_multiples(10) == 3 + 5 + 6 + 9
assert sum_multiples(20) == 3 + 5 + 6 + 9 + 10 + 12 + 15 + 18

print(sum_multiples(1000))
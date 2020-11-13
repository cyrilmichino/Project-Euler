def sum_square_difference(start, finish):

    square_sum = 0
    summation = 0

    for i in range(start, finish+1):
        summation += i
        square_sum += i**2

    return summation**2 - square_sum


assert sum_square_difference(1, 10) == 2640
assert sum_square_difference(1, 100) == 25164150
print(sum_square_difference(1, 1000))


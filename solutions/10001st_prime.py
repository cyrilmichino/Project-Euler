def get_prime(prime_index):
    "Get the nth prime number"

    number = 0
    prime = 0

    while prime_index != 0:
        number += 1

        for i in range(2,number+1):
            if number%i == 0:
                if i == number:
                    prime = number
                    prime_index -= 1

                else:
                    break

    return prime


assert get_prime(3) == 5
assert get_prime(1) == 2
assert get_prime(6) == 13
assert get_prime(10) == 29
print(get_prime(10001))
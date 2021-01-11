# A function that returns the number of prime numbers that exist up to and including a given number

def enter_number():
    number = input("Please enter your number:\n")
    num = int(number)
    return num


num = enter_number()


def count_primes(num):
    primes = [2]
    x = 3
    if num < 2:
        return 0
    while x <= num:
        for y in range(3, x, 2):
            if x % y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x += 2
    print(f'There are {len(primes)} prime numbers up to  {num} including:\n {primes}')


count_primes(num)

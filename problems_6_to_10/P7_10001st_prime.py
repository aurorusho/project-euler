'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

def is_prime(number : int) -> bool:
    i : int = 3
    sqroot : int = int(number ** 0.5)
    if number != 2 and number % 2 == 0:
        return False
    
    while i < sqroot + 1:
        if number % i == 0:
            return False
        i += 2
    return True

def main() -> None:
    i : int = 1
    prime_lst : list = []
    
    while len(prime_lst) < 10_001:
        if is_prime(i):
            prime_lst.append(i)
        i += 2

    print(prime_lst[-1])

if __name__ == '__main__':
    main()
'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''

def get_prime_factors(n : int) -> list:
    factor_lst : list = []
    n_sqroot = n ** 0.5
    
    # Converting number to odd in order to
    # avoid checking pair numbers later
    while n % 2 == 0:
        factor_lst.append(2)
        n /= 2
    
    i : int = 3
    # n = x1 * x2 * ...
    # if two "x" values where higher than the square
    # root of "n", the multiplication would 
    # be higher than "n"
    while i < (int(n_sqroot) + 1):
        while n % i == 0:
            factor_lst.append(i)
            n /= i
        # Not checking pair numbers
        i += 2

    if n > 1: factor_lst.append(int(n))

    return factor_lst


def main() -> None:
    n : int = 600851475143
    print(get_prime_factors(n)[-1])


if __name__ == '__main__':
    main()
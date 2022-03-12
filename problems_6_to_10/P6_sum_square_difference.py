'''
The sum of the squares of the first ten natural numbers is,
    1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
    3025 - 385 = 2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''
def main() -> None:
    sq_of_sum : int = 0
    sum_of_sq : int = 0
    for i in range(1, 100 + 1):
        sum_of_sq += i**2
        sq_of_sum += i 
    sq_of_sum **= 2
    
    print(sq_of_sum - sum_of_sq)

if __name__ == '__main__':
    main()
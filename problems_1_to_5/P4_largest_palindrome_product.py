'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''
def reverse_number(number : int) -> int:
    "Returns the reverse of a number"
    reverse : int = 0

    while number > 0:
        # Removes all columns of number except for the "ones column"
        last_digit : int = number % 10

        # On first iteration, starts the value with the
        # last digit of "number", on next iterations, converts
        # ones to tens, tens to hundreds, etc, and then
        # adds the new last digit of the remaining "number"
        reverse = (reverse * 10) + last_digit

        # Removes the last digit, and breaks loop if not more digits remaining
        number //= 10

    return reverse


def main() -> None:
    biggest_palondrome = 0
    for x1 in range(100, 999 + 1):
        for x2 in range(100, 999 + 1):
            multiplication = x1 * x2
            if multiplication < biggest_palondrome: continue
            if reverse_number(multiplication) == multiplication:
                biggest_palondrome = multiplication
    
    print(biggest_palondrome)


if __name__ == '__main__':
    main()
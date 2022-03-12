'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

def main() -> None:
    i : int = 2
    while True:
        for n in range(1, 20 + 1):
            if i % n != 0:
                break
        # If loop for ends without breaking
        else: break
        # Number should be pair, because n % 2 should be 0
        i += 2
    print(i)


if __name__ == '__main__':
    main()
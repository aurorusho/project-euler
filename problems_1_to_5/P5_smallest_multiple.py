'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

def main() -> None:
    top_number : int = 20
    i : int = top_number
    while True:
        for n in range(1, top_number):
            if i % n != 0:
                break
        # If loop for ends without breaking
        else: break
        i += top_number
    print(i)


if __name__ == '__main__':
    main()
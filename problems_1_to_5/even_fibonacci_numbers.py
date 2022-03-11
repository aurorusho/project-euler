first_term : int = 1
second_term : int = 2

amount : int = second_term

while True:
    current_term : int = first_term + second_term
    if current_term > 4_000_000:
        break
    first_term = second_term
    second_term = current_term

    if current_term % 2 == 0:
        amount += current_term

print(amount)
# 4613732
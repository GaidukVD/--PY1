import random
from collections import Counter

def get_unique_list_numbers() -> list[int]:
    i = 0
    rand_list = []
    while i < 15:
        n = random.randint(-10, 10)
        if n not in rand_list:
            rand_list.append(n)
            i += 1
    return (rand_list)


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))

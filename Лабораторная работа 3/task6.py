list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
max_ = list_numbers[0]
ind, ind_max = 0, 0
# TODO Оформить решение

for num in list_numbers:
    ind += 1
    if num > max_:
        max_ = num
        ind_max = ind - 1

list_numbers[-1], list_numbers[ind_max] = list_numbers[ind_max], list_numbers[-1]

print(list_numbers)

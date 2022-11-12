from random import randint
def get_unique_list_numbers() -> list[int]:
    uniq_num = []
    while len(uniq_num) != 15:
        ran_num = randint(-10, 10)
        if ran_num not in uniq_num:
            uniq_num.append(ran_num)
    return uniq_num

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))

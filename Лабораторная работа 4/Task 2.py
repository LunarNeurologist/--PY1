def get_count_char(str_):
    letter_dict = {}
    for letter in str_.lower():
        if letter.isalpha():
            if letter in letter_dict:
                letter_dict[letter] += 1
            else:
                letter_dict[letter] = 1
    return letter_dict

# TODO посчитать количество каждой буквы в строке в аргументе str_

def percent_letters(some_dict):
    dict_percent = {}
    sum_values = sum(some_dict.values())
    for key, value in some_dict.items():
        dict_percent[key] = value / sum_values * 100
    return dict_percent


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
print(percent_letters(get_count_char(main_str)))

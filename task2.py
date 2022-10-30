def get_count_char(str_):
    new_str = str_.lower()
    new_str = "".join(new_str.split())
    letter_dict = {}
    default_count = 0
    for i in new_str:
        if i.isalpha():
            letter_dict[i] = letter_dict.get(i, default_count) + 1
    return letter_dict


def get_count_proc(dict_):
    sum_ = 0
    letter_dict_proc = {}
    for i in dict_:
        sum_ += dict_.get(i)
        # letter_dict_proc[i] = letter_dict_proc.get(i)
    for n in dict_:
        letter_dict_proc[n] = dict_.get(n)/sum_
    return letter_dict_proc


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
main_dict = get_count_char(main_str)
print(get_count_proc(main_dict))

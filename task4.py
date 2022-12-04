import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(filename, new_line='\n', delimiter=',') -> list[dict]:
    with open(filename) as f_in:
        data = f_in.readlines()
        data = [line.rstrip() for line in data]

    lists_of_value = [val.split(delimiter) for val in data]

    headlines_list = lists_of_value[0]
    lists_dict = []
    for string in lists_of_value[1:]:
        dict_ = {headlines_list[wh]: string[wh] for wh in range(len(headlines_list))}
        lists_dict.append(dict_)

    return lists_dict


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))

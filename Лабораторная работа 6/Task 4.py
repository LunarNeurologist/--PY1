import json

INPUT_FILE = 'input.csv'

def csv_to_list_dict(filename, delimiter=',', new_line='\n', indent=4):
    with open(filename, 'r') as f:
        text = f.read().split(new_line)
    headers = text[0].split(delimiter)
    text = text[1:]
    json_list = []
    for row in text:
        if row == '':
            continue
        json_dict = {}
        for key, value in zip(headers, row.split(delimiter)):
            json_dict[key] = value
        json_list.append(json_dict)
    return json_list


print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))

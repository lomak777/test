import sys, json, re

tests_path = sys.argv[1]
values_path = sys.argv[2]

with open(tests_path, "r") as read_file:
    tests_data = read_file.readlines()

with open(values_path, "r") as read_file:
    values_data = json.load(read_file)
values_dict = {}

for i in values_data['values']:
    values_dict[i['id']] = i['value']

num = 0

for i in tests_data:
    if "id" in i:
        id = re.search(r'"id": (.+),', i)
        if id != None:

            if tests_data[num+2].strip() == "\"value\": \"\"":
                value_str = tests_data[num+2]
                value_str = value_str[:-2] + values_dict[int(id.group(1))] + '\",\n'
                tests_data[num+2] = value_str
            if tests_data[num+2].strip() == "\"value\": \"\",":
                value_str = tests_data[num+2]
                value_str = value_str[:-3] + values_dict[int(id.group(1))] + '\",\n'
                tests_data[num+2] = value_str
    num += 1

with open("report.json", "w") as file:
    file.writelines(tests_data)

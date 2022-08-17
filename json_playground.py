import json


def retrieve_sample_data():
    file = open('sample4.json', 'r')
    result = json.load(file)

    file.close()
    return result


def dump_dict_to_json(my_data):
    dumped_data = json.dumps(my_data)
    json.dump()
    file = open('my_dumped_data.json', 'w')
    file.write(dumped_data)
    file.close()
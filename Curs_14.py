import pprint

import json_playground

json_data = json_playground.retrieve_sample_data()
print(type(json_data))
print(json_data)

pprint.pp(json_data)

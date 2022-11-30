import json
import csv
import pandas as pd
import kafka
from kafka import KafkaProducer
from time import sleep
import requests

# with open('MOCK_DATA.csv', mode = 'r') as csvfile:
#     csvf = csv.DictReader(csvfile) 
#     list = []
#     for row in csvf:
#         list.append(row)
# csvfile.close()
# jsonString = json.dumps(list)
# empty_dict = {
#     "data" : {
#         "cred" : jsonString
#     }
# }
# print(empty_dict)
# for i in jsonString[][]:
#     print(i)
#     break

# >>> hashmap = {}
# >>> var1="hi"
# >>> 
# >>> hashmap[var1] = var2
# >>> hashmap
# {'yes': 'no', 'hi': 'bye'}

def producer():
    producer = KafkaProducer(
    bootstrap_servers=["localhost:9092"],api_version=(0, 10, 1),
    value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    with open('MOCK_DATA.csv', mode = 'r') as csvfile:
        csvf = csv.DictReader(csvfile) 
        list = []
        for row in csvf:
            list.append(row)
    csvfile.close()
    jsonString = json.dumps(list)
    empty_dict = {
        "data" : {
            "cred" : jsonString
        }
    }
    for i in range(120):
        producer.send('jsonAmit', empty_dict)
        sleep(5)
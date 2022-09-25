'''
1
Напишите классы сериализации контейнеров с данными Python в json, bin файлы.
Сами классы должны соответствовать общему интерфейсу (абстрактному базовому классу)
SerializationInterface.
'''

import pickle
import json

some_data_for_bin = {
    (1, 3.5): 'tuple',
    2: [1, 2, 3],
    'a': {'key': 'value'}
}

some_data_for_json = {'key': 'value', 2: [1, 2, 3], 'tuple': (5, 6), 'a': {'key': 'value'}}

file_name_for_bin = 'data_bin.bin'
file_name_for_json = 'data_json.json'

class SerializationInterface:

    def serialization_json(self):
        pass

    def serialization_bin(self):
        pass

class SerializationJson(SerializationInterface):

    def serialization_json(self):
        with open(file_name_for_json, "w") as fh:
            json.dump(some_data_for_json, fh)
        print("Calling func serialization_json")

class SerializationBin(SerializationInterface):

    def serialization_bin(self):
        with open(file_name_for_bin, "wb") as fh:
            pickle.dump(some_data_for_bin, fh)
        print("Calling func serialization_bin")


a = SerializationJson()
b = SerializationBin()

a.serialization_json()
b.serialization_bin()


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

    def serialization(self):
        pass

    def deserialization(self):
        pass

class SerializationJson(SerializationInterface):

    def serialization(self):
        with open(file_name_for_json, "w") as fh:
            json.dump(some_data_for_json, fh)
        print("Calling func serialization type file json")

    def deserialization(self):
        with open(file_name_for_json, "r") as fh:
            self.unpacked = json.load(fh)
        print("Calling func deserialization type file json")
        return self.unpacked

class SerializationBin(SerializationInterface):

    def serialization(self):
        with open(file_name_for_bin, "wb") as fh:
            pickle.dump(some_data_for_bin, fh)
        print("Calling func serialization type file bin")

    def deserialization(self):
        with open(file_name_for_bin, "rb") as fh:
            self.unpacked = pickle.load(fh)
        print("Calling func deserialization type file bin")
        return self.unpacked


a = SerializationJson()
b = SerializationBin()

a.serialization()
b.serialization()
print(a.deserialization())
print(b.deserialization())

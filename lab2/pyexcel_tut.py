import pyexcel 
from collections import OrderedDict

data = [
    OrderedDict({
        "name": "Hoa",
        "age": 18,
        "city": "Hanoi",
    }),
    OrderedDict({
        "name": "An",
        "age": 18,
        "city": "Hanoi",
    }),
    OrderedDict({
        "name": "Cam",
        "age": 11,
        "city": "Hanoi",
    })
]

pyexcel.save_as(records=data, dest_file_name="sample.xlsx")
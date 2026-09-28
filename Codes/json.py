import json

data = {
"name": "Zayed",
"class": 7,
"roll": 99,
"isPassed": False,

}

print(data)
print(type(data))

res = json. dumps (data)
print(res)
print(type(res))


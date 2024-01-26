import json


#with open('data.json', 'r') as file:
 #   data = json.load(file)

#print(data)

json ={
    "en":{
    "hello"
}
}

new_en_data = {
    "key1": "value1",
    "key2": "value2"
}



json["en"] = new_en_data
print(json)

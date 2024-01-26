import json

def translate (text,lang) :
    return "{} : translated to {}".format(text,lang)


with open('extracted_text.json', 'r') as f:
    json_data = json.load(f)


unique_en_key = {}

en_values = json_data["en"]

for  key in json_data["en"].keys():
   if(key not in json_data["fr"]) :
        unique_en_key[key]=json_data["en"][key]
   

with open('extracted_text.json', 'w') as f:
    for key in unique_en_key :
        for lang in json_data :
            if not lang == "en" :
                json_data[lang][key] = translate(json_data["en"][key],lang)

    f.write(json.dumps(json_data,indent=4)) 
from openai import OpenAI
import json

      
      
content=""

with open("key-gpt", "r", encoding="utf-8", errors='ignore') as file:
    key = file.read()



client = OpenAI(api_key=key)

with open("extracted_text.json", "r", encoding="utf-8", errors='ignore') as json_file:
    json_content = json.load(json_file)

    


stream = client.chat.completions.create(
    model="gpt-3.5-turbo",
   ## messages=[{"role": "user", "content": "translate to french : {}".format(json_content["en"])}],
    messages = [{"role" : "user", "content": "translate this to spanish : {} / the outpit must be a valid json format".format(json_content["en"])}] ,
    stream=True,
)
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        content+=chunk.choices[0].delta.content


print(content)


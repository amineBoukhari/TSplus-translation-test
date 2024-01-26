from bs4 import BeautifulSoup
import json
import sys


if len(sys.argv) > 1:
    currentFile = sys.argv[1]





#extract_all_text : extract text of given file 
def extract_all_text(currentFile):
    with open(currentFile, 'r', encoding='utf-8', errors='ignore') as file , open('extracted_text.json', 'r', encoding='utf-8', errors='ignore') as json_file :
        #html_content : our current page content 
        html_content = file.read()
        #soup : our current page content => array form
        soup = BeautifulSoup(html_content, 'html.parser')
        #json_content : content of the translation JSON filee => JSON FORMAT 
        json_content =json.load(json_file)
        json_content = json_content["en"]

    for key in json_content : 
        element =  soup.find( attrs={'data-id': key})
        if(element is not None) :
          element.string = f"{{t('{key}')}}"


    langs = ["fr","ES" ,"AR"]
    for lang in langs : 
      des = "{}/{}".format(lang,currentFile)
      with open(des, 'w', encoding='utf-8') as file:
        file.write(soup.prettify())


extract_all_text(currentFile)





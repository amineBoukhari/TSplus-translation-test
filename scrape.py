from bs4 import BeautifulSoup
import requests , json , os , sys
import html

# to translate text 
def translate (text,lang) :
    return "{} : translated to {}".format(text,lang)

def fill_other_lang () : 
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
# Function to read the current ID from the counter.txt file
def read_counter(filename):
    if os.path.exists(filename):
        try:
            with open(filename, 'r') as file:
                current_id = int(file.read())
        except ValueError:
            current_id = 0  # Handle invalid data in the file
    else:
        current_id = 0  # Handle the case when the file doesn't exist
    return current_id

# Function to update and write the new ID to the counter.txt file
def update_counter(filename, new_id):
    with open(filename, 'w') as file:
        file.write(str(new_id))


#extract input name file from  command-line arguments
if len(sys.argv) > 1:
    currentFile = sys.argv[1]

#extract_all_text : extract text of given file 
def extract_all_text(currentFile):
    id_counter = read_counter("counter.txt") 
    with open(currentFile, 'r', encoding='utf-8', errors='ignore') as file , open('extracted_text.json', 'r', encoding='utf-8', errors='ignore') as json_file :
        #html_content : our current page content 
        html_content = file.read()
        #soup : our current page content => array form
        soup = BeautifulSoup(html_content, 'html.parser')

        #json_content : content of the translation JSON filee => JSON FORMAT 
        json_content =json.load(json_file)
        # extracted_data : JSON file of new text (text without data_id)
        extracted_data = {}

        for tag in soup.find_all('p') :
            if not tag.has_attr('data-id') :
                extracted_data["p_{}".format(id_counter)] = tag.get_text().strip()
                tag['data-id'] = "p_{}".format(id_counter)
                id_counter+= 1 
            elif json_content["en"][tag['data-id']]  != tag.get_text().strip() :
                json_content["en"][tag['data-id']]  = tag.get_text().strip()
                for lang in json_content :
                    if lang != "en"  :
                        del json_content[lang][tag['data-id']]
                
                
        
        for tag in soup.find_all('h1') :
            if not tag.has_attr('data-id') :
                extracted_data["h1_{}".format(id_counter)] = tag.get_text().strip()
                tag['data-id'] = "h1_{}".format(id_counter)
                id_counter+= 1 
            elif json_content["en"][tag['data-id']] != tag.get_text().strip() :
                 json_content["en"][tag['data-id']]  = tag.get_text().strip()
                 for lang in json_content :
                    if lang != "en"  :
                        del json_content[lang][tag['data-id']]
        for tag in soup.find_all('h2') :
            if not tag.has_attr('data-id') :
                extracted_data["h2_{}".format(id_counter)] = tag.get_text().strip()
                tag['data-id'] = "h2_{}".format(id_counter)
                id_counter+= 1 
            elif json_content["en"][tag['data-id']]  != tag.get_text().strip() :
                 json_content["en"][tag['data-id']]  = tag.get_text().strip()
                 for lang in json_content :
                    if lang != "en"  :
                        del json_content[lang][tag['data-id']]


        for tag in soup.find_all('h3') :
            if not tag.has_attr('data-id') :
                extracted_data["h3_{}".format(id_counter)] = tag.get_text().strip()
                tag['data-id'] = "h3_{}".format(id_counter)
                id_counter+= 1 
            elif json_content["en"][tag['data-id']] != tag.get_text().strip() :
               json_content["en"][tag['data-id']]  = tag.get_text().strip()
               for lang in json_content :
                    if lang != "en"  :
                        del json_content[lang][tag['data-id']]


        for tag in soup.find_all('span') :
            if not tag.has_attr('data-id') :
                extracted_data["span_{}".format(id_counter)] = tag.get_text().strip()
                tag['data-id'] = "span_{}".format(id_counter)
                id_counter+= 1 
            elif json_content["en"][tag['data-id']] != tag.get_text().strip() :
               json_content["en"][tag['data-id']] = tag.get_text().strip()
               for lang in json_content :
                    if lang != "en"  :
                        del json_content[lang][tag['data-id']]

            
        #update counter 
        update_counter("counter.txt",id_counter)

    # or save to a file
    with open(currentFile, 'w', encoding='utf-8') as file:
        file.write(soup.prettify(formatter=None))



    mergedJSON = {**json_content["en"],**extracted_data}
    json_content["en"] = mergedJSON

    
    with open("extracted_text.json", "w") as file:
        file.write(json.dumps(json_content,indent=4)) 
        





extract_all_text(currentFile)
fill_other_lang()





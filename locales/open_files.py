

import json


def get_translation(current_language):
    # Get translation from json file
    with open(f"locales/{current_language}.json", encoding="utf-8") as f:
        translation = json.load(f)
    return translation
    
    
def get_manufacturers():
    # Get manufacturers from json file
    with open(f"locales/manufacturers.json", encoding="utf-8") as f:
        manufacturers = json.load(f)
    
    return [item['nome'] for item in manufacturers]

# print(get_manufacturers())
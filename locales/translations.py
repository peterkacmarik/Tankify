

import json


def get_translation(current_language):
    # Get translation from json file
    with open(f"locales/{current_language}.json", encoding="utf-8") as f:
        translation = json.load(f)
    return translation
    
    
# t = get_translation("en")
# print(t["senha"])
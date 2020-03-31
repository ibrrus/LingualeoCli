import requests
import urllib
import json

def first_connection_leo(login, password):
    url = "https://api.lingualeo.com/login"
    data = {
        "email": login,
        "password": password
    }
    response_obj = requests.post(url, data=data)
    return response_obj

def get_row_translates(session, word):
    url = "https://api.lingualeo.com/gettranslates?word=" + urllib.parse.quote_plus(word)
    try:
        r = session.get(url)
        result = json.loads(r.text)
        translate_all = result["translate"]
        print(translate_all)
        return translate_all
        # translate_one = translate_all[0]
        # return {
        #     "is_exist": translate_one["is_user"],
        #     "word": word,
        #     "tword": translate_one["value"]
        # }
    except Exception as e:
            return e

def add_word(session, word, tword):
    url = "https://api.lingualeo.com/addword"
    data = {
        "word": word,
        "tword": tword,
        "context": ""
    }
    print(url + "?" + urllib.parse.urlencode(data))
    input()
    session.post(url, data = data)
    # print(r.text)
# coding: utf-8

# Version 1.0
# 2020-03-30
# Pythonista 3.3
# IOS 13.3

import appex, console
import requests, urllib
import json
import pickle

COOKIES_FILE = 'leocookies' 

def main():
    if not appex.is_running_extension():
        print('This script is intended to be run from the sharing extension.')
        return
    text = appex.get_text().strip('* \n')
    if not text:
        print('No text input found.')
        return
        
    s = get_session()
    row_translates = get_row_translates(s, text)
    all_t = ""
    for t in row_translates:
        all_t += "- " + t["value"] + "\n"
    first_translate = row_translates[0]["value"]
    
    answer = console.alert(text, 
    '%s' % (all_t), 'Добавить в словарь', 'Отменить', hide_cancel_button=True)
    if (answer == 1):
        add_word(s, text, first_translate)
        console.alert("Слово добавлено", "", 'OK', hide_cancel_button=True)

def get_session():
    url = "https://api.lingualeo.com/api/login"
    s = requests.Session()
    try:
        s.cookies = load_cookies(COOKIES_FILE)
    except:
        print("Вы не авторизованы. Введите логин:")
        login = input()
        print("Введите пароль:")
        password = input()
        
        s.cookies = first_connection_leo(login, password).cookies
        save_cookies(s.cookies, COOKIES_FILE)
        print("Авторизация прошла успешно. Нажмите 'Done'")
    return s

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
        return translate_all
    except Exception as e:
            return e

def add_word(session, word, tword):
    url = "https://api.lingualeo.com/addword"
    data = {
        "word": word,
        "tword": tword,
        "context": ""
    }
    session.post(url, data = data)

def save_cookies(requests_cookiejar, filename):
    with open (filename, "wb") as f:
        pickle.dump(requests_cookiejar, f)

def load_cookies(filename):
    with open (filename, "rb") as f:
        return pickle.load(f)

if __name__ == '__main__':
    main()
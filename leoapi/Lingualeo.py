import requests
import urllib
import json
import Cookies

LOGIN_FILE = 'login.txt'
COOKIES_FILE = 'Cookies/cookies'

def get_session():
    url = "https://api.lingualeo.com/api/login"
    s = requests.Session()
    try:
        cookies = Cookies.load_cookies(COOKIES_FILE)
        #print("Вы авторизованы.")
        s.cookies = cookies
    except:
        with open(LOGIN_FILE, 'r') as login_data:
            Glogin = login_data.readline().rstrip('\n')
            Gpassword = login_data.readline().rstrip('\n')
        print("Вы не авторизованы. Введите логин:")
        input()
        login = Glogin
        print("Введите пароль:")
        input()
        password = Gpassword
        s.cookies = first_connection_leo(login, password).cookies
        Cookies.save_cookies(s.cookies, COOKIES_FILE)
        print("Перезапустите скрипт.")
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

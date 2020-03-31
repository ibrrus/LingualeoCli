# -*- coding: utf-8 -*-

import requests
import Cookies
import leoapi
import View

LOGIN_FILE = 'login.txt'
COOKIES_FILE = 'Cookies/cookies'

with open(LOGIN_FILE, 'r') as login_data:
    Glogin = login_data.readline().rstrip('\n')
    Gpassword = login_data.readline().rstrip('\n')

def main():
    url = "https://api.lingualeo.com/api/login"
    s = requests.Session()
    try:
        cookies = Cookies.load_cookies(COOKIES_FILE)
        print("Вы авторизованы.")
        s.cookies = cookies
        r = s.get(url)
        print(r.text)
    except:
        print("Вы не авторизованы. Введите логин:")
        input()
        login = Glogin
        print("Введите пароль:")
        input()
        password = Gpassword
        s.cookies = leoapi.first_connection_leo(login, password).cookies
        Cookies.save_cookies(s.cookies, COOKIES_FILE)
    print("Введите слово ('q' - для выхода):")
    word = input()
    while (word != "q"):
        row_translates = leoapi.get_row_translates(s, word)
        print("word - выберите перевод:")
        View.show_translate_variant(row_translates)
        num_translate = int(input())
        if num_translate in range (1, len (row_translates)):
            leoapi.add_word(s, word, row_translates[num_translate-1]["value"])
            print("Слово добавлено. Введите новое слово.")
        else:
            print("Перевод не выбран. Введите новое слово.")
        word = input()
if __name__ == '__main__':
    main()

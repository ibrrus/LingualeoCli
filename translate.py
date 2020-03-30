import requests
import Cookies
import leoapi

LOGIN_FILE = 'login.txt'
COOKIES_FILE = 'Cookies/cookies'

with open(LOGIN_FILE, 'r') as login_data:
    Glogin = login_data.readline().rstrip('\n')
    Gpassword = login_data.readline().rstrip('\n')

def main():
    url = "https://api.lingualeo.com/api/login"
    #TODO улучшить проверку авторизации
    s = requests.Session
    try:
        cookies = Cookies.load_cookies(COOKIES_FILE)
        print("Вы авторизованы.")
        r = requests.get(url, cookies = cookies)
        print(r.text)
    except:
        print("Вы не авторизованы. Введите логин:")
        input()
        login = Glogin
        print("Введите пароль:")
        input()
        password = Gpassword
        response_obj = leoapi.first_connection_leo(login, password)
        Cookies.save_cookies(response_obj.cookies, COOKIES_FILE)
    print("Введите слово:")
    word = input()

if __name__ == '__main__':
    main()

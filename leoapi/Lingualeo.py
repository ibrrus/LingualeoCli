import requests

def first_connection_leo(login, password):
    url = "https://api.lingualeo.com/login"
    data = {
        "email": login,
        "password": password
    }
    response_obj = requests.post(url, data=data)
    return response_obj

def get_translates(word):
    pass
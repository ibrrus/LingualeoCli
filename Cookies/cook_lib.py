import http.cookiejar
import pickle

def save_cookies(requests_cookiejar, filename):
    with open (filename, "wb") as f:
        pickle.dump(requests_cookiejar, f)

def load_cookies(filename):
    with open (filename, "rb") as f:
        return pickle.load(f)

def save_lwp(cookie, filename):
    lwp_cookiejar = http.cookiejar.LWPCookieJar()
    for c in cookie:
        args = dict(vars(c).items())
        args['rest'] = args['_rest']
        del args['_rest']
        c = http.cookiejar.Cookie(**args)
        lwp_cookiejar.set_cookie(c)
    lwp_cookiejar.save(filename, ignore_discard=True)
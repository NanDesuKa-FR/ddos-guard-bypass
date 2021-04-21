import requests

session = requests.Session()


def bypass_ddos_guard():
    response = session.post("https://check.ddos-guard.net/check.js")
    response.raise_for_status()
    for key, value in session.cookies.items():
        session.cookies.set_cookie(requests.cookies.create_cookie(key, value))


if __name__ == '__main__':
    bypass_ddos_guard()
    test = session.get("https://anidex.info/").text
    print(test)

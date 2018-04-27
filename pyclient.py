import requests
import sys

CURRENT_URL = "http://127.0.0.1:9080/"


def do_get(url, headers):
    try:
        request = requests.get(url, headers=headers)
    except requests.ConnectionError as ce:
        print(ce.message)
        sys.exit(1)
    print(request)
    if request.status_code != 200:
        print('Error with server')
    else:
        return request.json()


def main():
    result = do_get(CURRENT_URL, {'X-Server-Select': 'app1'})
    result = do_get(CURRENT_URL, {'X-Server-Select': 'app2'})

if __name__ == "__main__":
    main()
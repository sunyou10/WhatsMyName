import requests
from bs4 import BeautifulSoup
from pyfiglet import Figlet
from clint.textui import colored

f = Figlet(font='slant')
print(colored.white("---------------------------------------------------------------------------"))
print(f.renderText('Whats My Name'))
print(colored.white("----------------------------------------------------------KILLER WHALE _whs"))

proxies = {
    'http': 'socks5h://localhost:9050',
    'https': 'socks5h://localhost:9050'
}

# 전역 변수와 공톰 함수 입니다.
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "ko-KR,ko;q=0.9",
    "Cache-Control": "max-age=0",
    "Sec-Ch-Ua": "\"Chromium\";v=\"118\", \"Google Chrome\";v=\"118\", \"Not=A?Brand\";v=\"99\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"macOS\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
}
forum = []
errorForum = []


def userStatus(Bool, name):
    if Bool:
        forum.append(name)


def notSearch(name):
    errorForum.append(name)


def _0day(user):
    url = "https://0day.red/"
    name = '0Day'
    userUrl = url + 'User-' + user
    try:
        response = requests.get(userUrl, headers=headers)
        if response.status_code == 200:
            userStatus(True, name)
    except:
        notSearch(name)


def _1877(user):
    url = "https://1877.to/forums/"
    name = '1877'
    userUrl = url + user + '/'
    try:
        response = requests.get(userUrl, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        body = soup.body
        if body and 'data-template' in body.attrs:
            data_template_value = body['data-template']
            if data_template_value == 'member_view':
                userStatus(True, name)
            elif data_template_value == 'error':
                userStatus(False, name)
    except:
        notSearch(name)


def _0x00sec(user):
    url = "https://0x00sec.org/"
    name = '0x00sec'
    userUrl = url + 'u/' + user
    try:
        response = requests.get(userUrl, headers=headers)
        if response.status_code == 200:
            userStatus(True, name)
    except:
        notSearch(name)


def ramble(user):
    name = "ramble"
    url = (
            "http://rambleeeqrhty6s5jgefdfdtc6tfgg4jj6svr4jpgk4wjtg3qshwbaad.onion/user/"
            + user
    )
    proxies = {"http": "socks5h://localhost:9050", "https": "socks5h://localhost:9050"}
    try:
        response = requests.get(url, proxies=proxies)
        if response.status_code == 200:
            userStatus(True, name)
        else:
            pass
    except:
        notSearch(name)


def crackedIo(user):
    url = "https://cracked.io/"
    name = 'crackedIo'
    userUrl = url + user
    try:
        response = requests.get(userUrl, headers=headers)
        if response.status_code == 200:
            userStatus(True, name)
    except Exception as e:
        print(e)
        notSearch(name)


def infectedZone(user):
    url = "https://infected-zone.com"
    name = 'infected zone'
    try:
        response = requests.get(url, headers=headers)
        cookies = response.cookies
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        element = soup.find(id='XF')
        data_csrf = element['data-csrf']
        url = 'https://infected-zone.com/index.php?members/find&&_xfRequestUri=%2Fforum%2F&_xfWithData=1&_xfToken=' + data_csrf + '&_xfResponseType=json&q=' + user
        response = requests.get(url, headers=headers, cookies=cookies)
        json_data = response.json()
        for item in json_data['results']:
            id_value = item['id']
            if id_value.lower() == user.lower():
                forum.append(name)
    except Exception as e:
        notSearch(name)
        # print(e)


if __name__ == '__main__':
    user = input(colored.blue("USER NAME:"))

    crackedIo(user)
    _0day(user)
    _0x00sec(user)
    _1877(user)
    ramble(user)
    infectedZone(user)

    print(colored.green("\n>>> DETECTED: "))
    for i in forum:
        print("\t" + i)

    print(colored.red("\n>>> unknown: ", errorForum))
    for i in errorForum:
        print("\t" + i)

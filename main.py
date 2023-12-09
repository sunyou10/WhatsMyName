import requests
from selenium import webdriver
import json
from bs4 import BeautifulSoup
from urllib.parse import urlencode, urljoin
import time

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


# 여기서 부터 작성하세요

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


def breachForums(user):
    name = 'breachForums'
    url = 'http://breachedu76kdyavc6szj6ppbplfqoz3pgrk3zw57my4vybgblpfeayd.onion'
    try:
        response = requests.get(url, headers=headers, proxies=proxies)
        cookies = response.cookies
        url = 'http://breachedu76kdyavc6szj6ppbplfqoz3pgrk3zw57my4vybgblpfeayd.onion/User-'
        userUrl = url + user
        response = requests.get(userUrl, headers=headers, proxies=proxies, cookies=cookies)
        if response.text.find('The member you specified is either') == -1:
            userStatus(True, name)
    except Exception as e:
        print(e)
        notSearch(name)


def bestCardingWorld(user):
    name = 'BestCardingWorld'
    url = "http://bestteermb42clir6ux7xm76d4jjodh3fpahjqgbddbmfrgp4skg2wqd.onion/search.php?keywords=&terms=all&sc=1&sf=all&sr=posts&sk=t&sd=d&st=0&ch=300&t=0&submit=Search&author="
    try:
        userUrl = url + user
        response = requests.post(userUrl, headers=headers, proxies=proxies)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.select_one('div.search:nth-child(4) > div:nth-child(1) > dl:nth-child(1)')
        if title != None:
            userStatus(True, name)
    except Exception as e:
        print(e)
        notSearch(name)


def patchedto(user):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome()

    # patched.to 시작
    name = 'patched.to'
    url = "https://patched.to/xmlhttp.php?action=get_users&query="
    userUrl = url + user
    try:
        driver.get(userUrl)
        info = driver.find_element("xpath", '/ html / body / pre')
        for item in info:
            id_value = item['id']
            if id_value.lower() == user.lower():
                forum.append(name)
    except:
        driver.quit()
        notSearch(name)


def bhcforums(user):
    query_params = {
        'action': 'get_users',
        'query': user,
    }
    url = "https://bhcforums.cc/xmlhttp.php"
    name = 'bhcforums.cc'
    query_string = urlencode(query_params)
    userUrl = f"{url}?{query_string}"

    try:
        response = requests.get(userUrl, headers=headers)
        if response.status_code == 200:
            json_data = response.json()

            found = False
            for user_info in json_data:
                if 'id' in user_info and user_info['id'] == f"{user}":
                    userStatus(True, name)
                    found = True
                    break
    except:
        notSearch(name)


def enclavecc(user):
    query_params = {
        'q': user,
        'type': 'core_members',
        'joinedDate': 'any',
        'group[4]': '1',
        'group[19]': '1',
        'group[9]': '1',
        'group[12]': '1',
        'group[22]': '1',
        'group[6]': '1',
        'group[3]': '1',
        'group[7]': '1',
        'group[18]': '1',
        'group[23]': '1',
        'group[20]': '1',
        'group[21]': '1',
        'group[14]': '1',
        'group[15]': '1',
        'group[16]': '1',
        'group[10]': '1',
    }
    url = "https://www.enclave.cc/index.php"
    name = 'enclave.cc'
    query_string = urlencode(query_params)
    userUrl = f"{url}?/search/&{query_string}"

    try:
        print(userUrl)
        response = requests.get(userUrl, headers=headers)
        if 'There were no results for your search. Try broadening your criteria or choosing a different content area.' in response.text:
            notSearch(name)
        elif response.status_code == 200:
            userStatus(True, name)
    except:
        print('enclave.cc error')
    time.sleep(2)


def hack5(user):
    url = 'https://forums.hak5.org/search/'
    name = 'hack5'
    userUrl = url + '?&q=' + user + '&type=core_members&quick=1&joinedDate=any&group[10]=1&'
    try:
        print(userUrl)
        response = requests.get(userUrl, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        if 'Found 0 results' not in soup.text:
            userStatus(True, name)
    except Exception as e:
        print(e)
        notSearch(name)


def hostingforums(user):
    url = "https://hostingforums.net/u/"
    name = 'hostingforums'
    userUrl = url + user
    try:
        response = requests.get(userUrl, headers=headers)
        if response.status_code == 200:
            userStatus(True, name)
    except:
        notSearch(name)


def landzdown(user):
    url = "https://www.landzdown.com/index.php?action=mlist;sa=search"
    name = 'landzdown'
    payload = {
        'search': user,
        'fields[]': 'name',
        'submit': 'Search'
    }
    try:
        print(url)
        response = requests.post(url, headers=headers, data=payload)
        if response.status_code == 200:
            userStatus(True, name)
    except:
        notSearch(name)


def nullbb(user):
    query_params = {
        'action': 'get_users',
        'query': user,
    }
    url = "https://nulledbb.com/xmlhttp.php"
    name = 'nullBB.com'
    query_string = urlencode(query_params)
    userUrl = f"{url}?{query_string}"

    try:
        print(userUrl)
        response = requests.get(userUrl, headers=headers)
        if response.status_code == 200:
            json_data = response.json()

            found = False
            for user_info in json_data:
                if 'id' in user_info and user_info['id'] == f"{user}":
                    userStatus(True, name)
                    found = True
                    break

    except:
        notSearch(name)


def R0CREW(user):
    from bs4 import BeautifulSoup
    url = 'https://forum.reverse4you.org/'
    name = 'R0CREW'
    userUrl = url + 'u/' + user + '/summary'
    try:
        response = requests.get(userUrl, headers=headers)
        if response.status_code == 200:
            userStatus(True, name)
    except:
        notSearch(name)


def searchRedSecurity(user):
    url = "https://redsecurity.info/cc/xmlhttp.php?action=get_users"
    timestamp = int(time.time() * 1000)  # 현재 시간을 밀리초로 변환
    payload = {
        "query": user,
        "_": timestamp
    }

    response = requests.post(url, data=payload, headers=headers)

    if response.status_code == 200:
        result = response.json()
        userStatus(True, user)  # 성공한 경우 포럼에 추가
    else:
        notSearch(user)  # 실패한 경우 에러 포럼에 추가


def rootme(user):
    from bs4 import BeautifulSoup
    url = 'https://www.root-me.org/?page=recherche&lang=fr&recherche='
    name = 'rootme'
    userUrl = url + user
    try:
        response = requests.get(userUrl, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        if 'Aucun résultat pour ' not in soup.text:
            userStatus(True, name)
    except:
        notSearch(name)


def use_ip(user):
    url = "https://www.use-ip.co.uk/forum/search/583378/?c%5Busers%5D="
    name = 'use_ip'
    userUrl = url + user + "&o=relevance"
    try:
        print(userUrl)
        response = requests.get(userUrl, headers=headers)
        if response.status_code == 200:
            userStatus(True, name)
    except:
        notSearch(name)


def searchWasm(user):
    url = "https://wasm.in/index.php?members/find"
    payload = {
        "q": user,
        "_xfRequestUri": "/",
        "_xfNoRedirect": 1,
        "_xfResponseType": "json"
    }

    response = requests.post(url, data=payload, headers=headers)

    if response.status_code == 200:
        result = response.json()
        userStatus(True, user)  # 성공한 경우 포럼에 추가
    else:
        notSearch(user)  # 실패한 경우 에러 포럼에 추가


def wilderssecurity(user):
    url = "https://www.wilderssecurity.com/search/search"
    name = 'wilderssecurity'
    payload = {
        "keywords": "",
        "users": user,
        "date": "",
        "_xfToken": ""}
    try:
        response = requests.post(url, headers=headers, data=payload)
        if 'The following members could not be found' not in response.text:
            userStatus(True, name)
    except:
        notSearch(name)


def Wjunction(user):
    url = "https://www.wjunction.com/search/2724922/?c[users]={}&o=relevance"
    name = "Wjunction"
    userUrl = url.format(user)
    try:
        print(userUrl)
        response = requests.get(userUrl, headers=headers)
        if response.status_code == 200:
            userStatus(True, name)
    except:
        notSearch(name)


def dark2web(user):
    url = "https://web-2.gate2dark.top"
    name = 'dark2web'
    try:
        response = requests.get(url, headers=headers)
        cookies = response.cookies
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        element = soup.find(id='XF')
        data_csrf = element['data-csrf']
        url = 'https://web-2.gate2dark.top/index.php?members/find&_xfRequestUri=%2Fmembers%2F&_xfWithData=1&_xfResponseType=json&_xfToken=' + data_csrf + '&q=' + user
        response = requests.post(url, headers=headers, cookies=cookies)
        json_data = response.json()
        for item in json_data['results']:
            id_value = item['id']
            if id_value.lower() == user.lower():
                forum.append(name)
    except Exception as e:
        notSearch(name)
        print(e)


def bdfClub(user):
    url = "https://bdfclub.com"
    name = 'BDF CLUB'
    try:
        response = requests.get(url, headers=headers)
        cookies = response.cookies
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        element = soup.find(id='XF')
        data_csrf = element['data-csrf']
        url = 'https://bdfclub.com/index.php?members/find&_xfRequestUri=%2Fmembers%2F&_xfWithData=1&_xfResponseType=json&_xfToken=' + data_csrf + '&q=' + user
        response = requests.post(url, headers=headers, cookies=cookies)
        json_data = response.json()
        for item in json_data['results']:
            id_value = item['id']
            if id_value.lower() == user.lower():
                forum.append(name)
    except Exception as e:
        notSearch(name)
        print(e)


def megatop(user):
    url = 'https://megatop.biz/forum/'
    name = 'megatop'
    try:
        response = requests.get(url, headers=headers)
        cookies = response.cookies
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        element = soup.find(id='XF')
        data_csrf = element['data-csrf']
        url = 'https://megatop.biz/index.php?members/find&&_xfRequestUri=%2Fforum%2F&_xfWithData=1&_xfToken=' + data_csrf + '&_xfResponseType=json&q=' + user
        response = requests.get(url, headers=headers, cookies=cookies)
        json_data = response.json()
        for item in json_data['results']:
            id_value = item['id']
            if id_value.lower() == user.lower():
                forum.append(name)
    except Exception as e:
        notSearch(name)
        print(e)


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
        print(e)


if __name__ == '__main__':
    user = input('유저명 : ')
    #    crackedIo(user)
    #    breachForums(user)
    #    patchedto(user)
    #    bestCardingWorld(user)
    _0day(user)
    _0x00sec(user)
    _1877(user)
    ramble(user)
    #    bhcforums(user) 수정필요
    #    enclavecc(user) 수정필요
    #    hack5(user)    수정필요
    #    hostingforums(user)
    #    landzdown(user) 수정필요
    #    nullbb(user)   수정필요
    #    R0CREW(user)
    #    searchRedSecurity(user) 수정필요
    #    rootme(user)   수정필요
    #    use_ip(user)   수정필요
    #    searchWasm(user) 수정필요
    #    wilderssecurity(user)
    #    Wjunction(user) 수정필요
    #    dark2web(user)
    #    bdfClub(user)
    #    megatop(user)
    infectedZone(user)

    print(forum)
    print(errorForum)

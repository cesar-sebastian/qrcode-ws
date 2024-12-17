import requests


def login(sss_user:str , sss_pass: str) -> bool:

    url = "https://seguro.sssalud.gob.ar/login.php?opc=bus650&user=RNOS&cat=consultas"
    payload = f'_user_name_={sss_user}&_pass_word_={sss_pass}&submitbtn=Ingresar'
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://seguro.sssalud.gob.ar',
        'referer': 'https://seguro.sssalud.gob.ar/login.php?opc=bus650&user=RNOS&cat=consultas',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    }

    try:
        with requests.Session() as session:
            response = session.post(url, headers=headers, data=payload, timeout=10)
            response.raise_for_status()

            if "El Usuario o la Clave son incorrectos." in response.text:
                return False
            
            return True
    except requests.exceptions.RequestException as e:
        return False


def data(cuil: str):

    url = "https://seguro.sssalud.gob.ar/indexss.php?opc=bus650&user=RNOS&cat=consultas"

    payload = f'pagina_consulta=&cuil_b={cuil}&nro_doc=&B1=Consultar'
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'es-ES,es;q=0.9',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'PHPSESSID=9uqcqquu8b1mqgl07c79tooeu7; cookiesession1=22F5AEF613U8ISLRA6J0MUTPB0VB1F20; cookiesession4=dPuRsGxQRwE0mPYa3/11Qj/MtyfoYkkEv2QrwtfZezY3orLIlQTOd9XCS+nRkneyJM3YUBPEkIRYH9nsL34cocA+55vHgAVJ/j+/87VRLdC7RlT90gbCzGrpQY0bWlUNQmVjtI+x2qDMo63utkPNHH3jf/Acm5Qa/e/H/ONiBpsWtmgIPHwLdvm4dNU9zVtL8wAS+fdydLc=',
        'origin': 'https://seguro.sssalud.gob.ar',
        'priority': 'u=0, i',
        'referer': 'https://seguro.sssalud.gob.ar/indexss.php?opc=bus650&user=RNOS&cat=consultas',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    }

    try:
        with requests.Session() as session:
            response = session.post(url, headers=headers, data=payload, timeout=10)
            response.raise_for_status()  # Raise an error for HTTP issues
            texto = response.text
            inicio = texto.index("Fecha de actualización")
            fin = texto.index("<a href='https://seguro.sssalud.gob.ar/indexss.php")
            return texto[inicio:fin]
    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")
        return ''

def scrap(user, password, cuit) -> str:
    dataScrap = data(cuit)
    
    if dataScrap != '':
        return dataScrap
    
    dataLogin = login(user, password)
    
    if not dataLogin:
        raise Exception('Error login')

    return data(cuit)
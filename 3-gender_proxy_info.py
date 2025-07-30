import json
import requests
from tenacity import retry, wait_fixed, stop_after_attempt
from concurrent.futures import ThreadPoolExecutor, as_completed


def get_country_list() -> list:
    """
    :return: [{code:str,name:str},...]
    """
    with open('country.json', 'r', encoding='utf8') as f:
        data = json.load(f)
    return data


@retry(stop=stop_after_attempt(10), wait=wait_fixed(1))
def get_proxy_info(proxy: str):
    """"""
    proxies = {
        'http': f'socks5h://{proxy}',
        'https': f'socks5h://{proxy}',
    }
    response = requests.get('https://api.ipapi.is/', proxies=proxies)
    print(response.text)
    data = response.json()
    location = data['location']
    # 名称
    name = location['country_code']
    # 纬度
    latitude = location['latitude']
    # 经度
    longitude = location['longitude']
    # 时区
    timezone = location['timezone']
    return name, timezone, latitude, longitude


def handle_thread(country: dict):
    """"""
    code = country['code']
    name = country['name']

    try:
        # _, timezone, latitude, longitude = get_proxy_info(f'4119739-bb9bbdf7:4c26ebbb-{code}@gate.hk.domoproxy.info:1000')
        # ipidea
        # _, timezone, latitude, longitude = get_proxy_info(f'NF321321-zone-custom-region-{code}:NF321321@17083eb925263312.gtz.as.ipidea.online:2333')
        # ipmars
        _, timezone, latitude, longitude = get_proxy_info(f'mKokLOnKgQ-zone-mars-region-{code}:88549607@as.63a8d56b23858374.ipmars.vip:4900')
    except Exception:
        timezone = ''
        latitude = ''
        longitude = ''

    return {
        'name': name,
        'code': code,
        'url': f'https://raw.githubusercontent.com/heisiyyds999/clash-conf/refs/heads/master/proxys-b/{code}.yaml',
        'timezone': timezone,
        'longitude': longitude,
        'latitude': latitude
    }


def main():
    """"""
    country_list = get_country_list()
    with ThreadPoolExecutor(max_workers=10) as executor:
        results = [executor.submit(handle_thread, country)
                   for country in country_list]
        result = [result.result() for result in results]
        result = sorted(result, key=lambda x: x["code"])
        with open('result.json', 'w', encoding='utf8') as fp:
            json.dump(result, fp, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    main()

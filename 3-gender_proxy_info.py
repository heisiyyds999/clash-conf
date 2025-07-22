import json
import requests
from tenacity import retry, wait_fixed, stop_after_attempt
from concurrent.futures import ThreadPoolExecutor, as_completed


def get_country_list() -> list:
    """
    :return: [{code:str,name:str},...]
    """
    with open('proxy_country.json', 'r', encoding='utf8') as f:
        data = json.load(f)
    return [{'code': item['name'], 'name': item['cnname']} for item in data]


def get_proxy_info(proxy: str):
    """"""
    proxies = {
        'http': f'socks5h://{proxy}',
        'https': f'socks5h://{proxy}',
    }
    response = requests.get('https://api.ipapi.is/', proxies=proxies)
    data = response.json()
    location = data['location']
    # 名称
    name = location['country_code']
    # 经度
    latitude = location['latitude']
    # 纬度
    longitude = location['longitude']
    # 时区
    timezone = location['timezone']
    return name, timezone, latitude, longitude


def handle_thread(country: dict):
    """"""
    code = country['code']
    name = country['name']

    _, timezone, latitude, longitude = get_proxy_info(f'4119739-bb9bbdf7:4c26ebbb-US@gate.hk.domoproxy.info:1000')

    template = f'{name}@@@@{code}'
    print(template)
    return template


def main():
    """"""
    country_list = get_country_list()
    with ThreadPoolExecutor(max_workers=10) as executor:
        results = [executor.submit(handle_thread, country) for country in country_list]
        result = [result.result() for result in results]
        print(result)


if __name__ == '__main__':
    main()

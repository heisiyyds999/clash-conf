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


def handle_thread():
    """"""


def main():
    """"""
    country_list = get_country_list()
    # for country in country_list:
    #     print(country)
    # t = get_proxy_info(f'4119739-bb9bbdf7:4c26ebbb-US@gate.hk.domoproxy.info:1000')


if __name__ == '__main__':
    main()

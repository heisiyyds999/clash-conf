import json
import requests
from tenacity import retry, stop_after_attempt, wait_fixed
from concurrent.futures import ThreadPoolExecutor, as_completed


@retry(reraise=True, stop=stop_after_attempt(3), wait=wait_fixed(0))
def get_ip(proxy: str):
    """"""
    proxies = {
        'http': 'socks5h://' + proxy,   # 注意使用 socks5h 支持域名解析
        'https': 'socks5h://' + proxy
    }
    # response = requests.get('https://realip.cc/', proxies=proxies)
    response = requests.get('https://api.ipapi.is/', proxies=proxies)
    data = response.json()
    return data


def handle_thread(item):
    """"""
    code = item['name']
    name = item['cnname']
    # proxy = f'NF321321-zone-custom-region-hk:NF321321@17083eb925263312.gtz.as.ipidea.online:2333'
    proxy = f'4119739-bb9bbdf7:4c26ebbb-{code}@gate.hk.domoproxy.info:1000'
    try:
        data = get_ip(proxy)
        # 时区
        time_zone = data['time_zone']
        # 经度
        longitude = data['longitude']
        # 纬度
        latitude = data['latitude']
        template = f'{name}@@@@{code}@@@@https://raw.githubusercontent.com/heisiyyds999/clash-conf/refs/heads/master/proxys/{code}.yaml@@@@{time_zone}@@@@English@@@@{latitude}@@@@{longitude}'
    except Exception as e:
        template = f'{name}@@@@{code}@@@@https://raw.githubusercontent.com/heisiyyds999/clash-conf/refs/heads/master/proxys/{code}.yaml'
    return template


def main():
    """"""
    # with open('country.json', 'r', encoding='utf8') as fp:
    #     data = json.load(fp)

    with open('proxy_country.json', 'r', encoding='utf8') as fp:
        data = json.load(fp)

    with ThreadPoolExecutor(10) as exec:
        tasks = [exec.submit(handle_thread, (item)) for item in data]
        for future in as_completed(tasks):
            print(future.result())


if __name__ == '__main__':
    main()

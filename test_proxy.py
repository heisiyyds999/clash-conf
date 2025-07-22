import json
import requests


proxy = 'NF321321-zone-custom-region-hk:NF321321@17083eb925263312.gtz.as.ipidea.online:2333'
proxies = {
    'http':f'socks5h://{proxy}',
    'https':f'socks5h://{proxy}',
}
response = requests.get('https://api.ipapi.is/', proxies=proxies)
print(response.text)

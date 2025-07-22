import json


def main():
    """"""
    with open('proxy_country.json', encoding='utf8') as f:
        data = json.load(f)
    country_list = [{'code': item['name'], 'name': item['cnname']} for item in data]

    with open('country_list.json', 'w', encoding='utf8') as f:
        json.dump(country_list, f, ensure_ascii=False)


if __name__ == '__main__':
    main()

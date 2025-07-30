import json


def main():
    """"""
    # domo
    # with open('domo.json', encoding='utf8') as f:
    #     data = json.load(f)
    # country_list = [{'code': item['name'], 'name': item['cnname']}
    #                 for item in data]

    # ipidea
    country = []
    with open('ipidea.json', encoding='utf8') as f:
        data = json.load(f)
    for a in data['ret_data']['country']:
        if a['list']:
            for b in a['list']:
                country.append(b)
    
    with open('country.json', 'w', encoding='utf8') as f:
        json.dump(country, f, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    main()

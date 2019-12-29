# -*- coding: UTF-8 -*-
import requests
import bs4
import json
import MainUtil

resources_file_path = '/resources/airplane/airportNameList.ini'
scratch_url_old = 'https://data.variflight.com/profiles/profilesapi/search'
scratch_url = 'https://data.variflight.com/analytics/codeapi/initialList'
get_city_url = 'https://data.variflight.com/profiles/Airports/%s'


# 传入查找网页的url和旧数据，然后本方法会比对原数据中是否有新的条目，如果有则不加入，如果没有则重新加入，最后返回新数据
def scratch_airport_name(scratch_url, old_airports):
    new_airports = []
    data = requests.get(scratch_url).text
    all_airport_json = json.loads(data)['data']
    for airport_by_word in all_airport_json.values():
        for airport in airport_by_word:
            if airport['fn'] not in old_airports:
                get_city_uri = get_city_url % airport['id']
                print(get_city_uri)
                data2 = requests.get(get_city_uri).text
                soup = bs4.BeautifulSoup(data2, "html.parser")
                city = soup.find('span', text="城市").find_next_sibling().text
                new_airports.append(city + ',' + airport['fn'])
    return new_airports



# main方法，执行这个py，默认调用main方法，相当于java的main
if __name__ == '__main__':
    MainUtil.main(resources_file_path, scratch_url, scratch_airport_name)

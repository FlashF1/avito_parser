
import requests
from bs4 import BeautifulSoup
import time
import random


def get_html(url):
    r = requests.get(url)
    return r.text


def get_total_pages(html):
    soup = BeautifulSoup(html, 'lxml')
    pages = soup.find('div', class_='js-pages').find_all('span')[-2].get('data-marker')
    total_pages = int(pages[5:-1])
    return total_pages


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    ads = soup.find('div', elementtiming='bx.catalog.container').find_all('div', class_='js-catalog-item-enum')
    return ads


def main():
    # url = 'https://www.avito.ru/moskva/tovary_dlya_kompyutera/komplektuyuschie/videokarty-ASgBAgICAkTGB~pm7gmmZw?q=rtx'
    url = str(input('Введите ссылку - результат после поиска искомого товара: '))
    base_url = url + '&p='

    real_total_pages = get_total_pages(get_html(url))
    print('Страниц с объявлениями', real_total_pages)
    
    real_total_ads = 0
    # for i in range(1, real_total_pages + 1):
    for i in range(1, 2):
        time.sleep(random.randint(5, 15))
        url_gen = base_url + str(i)
        html = get_html(url_gen)
        real_total_ads += len(get_page_data(html))
    print('Всего объявлений', real_total_ads)


if __name__ == '__main__':
    main()



























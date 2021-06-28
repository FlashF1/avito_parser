
import requests
from bs4 import BeautifulSoup
import time
import random
import re


def get_html(url):
    r = requests.get(url)
    return r.text


def get_total_pages(html):
    ''' Подсчет количества страниц для данной категории. 
    '''
    soup = BeautifulSoup(html, 'lxml')
    pages = soup.find('div', class_='js-pages').find_all('span')[-2].get('data-marker')
    total_pages = int(pages[5:-1])
    return total_pages


def get_page_data(html):
    ''' Отфильтровываем рекламные и тд объявления.
    На выходе получаем элемент супа с актуальными 
    объявлениями на странице для последующей итерации.
    '''
    soup = BeautifulSoup(html, 'lxml')
    ads = soup.find('div', elementtiming='bx.catalog.container').find_all(class_=re.compile('iva-item-root'))
    return ads


def main():
    url = 'https://www.avito.ru/moskva/tovary_dlya_kompyutera/komplektuyuschie/videokarty-ASgBAgICAkTGB~pm7gmmZw?q=rtx'
    base_url = 'https://www.avito.ru/moskva/tovary_dlya_kompyutera/komplektuyuschie/videokarty-ASgBAgICAkTGB~pm7gmmZw?'
    page_part = 'p='
    query_part = '&q=rtx'

    real_total_pages = get_total_pages(get_html(url))
    print(f'Страниц с объявлениями {real_total_pages}')
    
    real_total_ads = 0
    for i in range(1, real_total_pages + 1):
        time.sleep(random.randint(5, 15))
        url_gen = base_url + query_part + str(i) + query_part
        html = get_html(url_gen)
        real_total_ads += len(get_page_data(html))
        print(f'На странице {i} количество объявлений равно {len(get_page_data(html))}.')
    print(f'Всего объявлений {real_total_ads}')


if __name__ == '__main__':
    main()



























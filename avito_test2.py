
import avito
import time
import random
from datetime import datetime


url = 'https://www.avito.ru/moskva/tovary_dlya_kompyutera/komplektuyuschie/videokarty-ASgBAgICAkTGB~pm7gmmZw?q=rtx'
base_url = 'https://www.avito.ru/moskva/tovary_dlya_kompyutera/komplektuyuschie/videokarty-ASgBAgICAkTGB~pm7gmmZw?'
page_part = 'p='
query_part = '&q=rtx'

# Получаем общее количество страниц с этими объявлениями.
real_total_pages = avito.get_total_pages(avito.get_html(url))
print(f'Обработано {real_total_pages} страниц с объявлениями.')
    
# Идем в цикле по каждой странице. 
for i in range(1, real_total_pages + 1): 
    time.sleep(random.randint(5, 15))
    url_gen = base_url + query_part + str(i) + query_part

    # Получаем список со всеми объявлениями на странице.
    ads = avito.get_page_data(avito.get_html(url_gen)) 

    for ad in ads:
        try:
            url_item = ad.find('a', itemprop='url').get('href')
        except:
            url_item = ''
        try:
            title = ad.find('h3', itemprop='name').text
        except:
            title = ''
        try:
           price = ad.find('span', itemprop='offers').text.replace('₽', '').replace(' ', '')
        except:
            price = ''   

        # Пишем в файл ссылку на объявление, его название и цену.
        file_name = str(datetime.now().date()) + '.txt'
        with open(file_name, 'a', encoding='utf-8') as f:
            f.write('https://www.avito.ru' + url_item + '\n')
            f.write(title + '\n')
            f.write(price + '\n')
            f.write('\n')

print(f'Запись объявлений в файл {file_name} завершена.')


















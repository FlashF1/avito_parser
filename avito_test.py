
import avito


url = 'https://www.avito.ru/moskva/tovary_dlya_kompyutera/komplektuyuschie/videokarty-ASgBAgICAkTGB~pm7gmmZw?p=2&q=rtx'
ads = avito.get_page_data(avito.get_html(url))

print(f'Всего объявлений {len(ads)}')
print('Названия объявлений:')

for ad in ads:
    try:
        title = ad.find('div', class_='iva-item-titleStep-2bjuh').find('h3').text
    except:
        title = ''
    print(title) # выводит название каждого объявления



















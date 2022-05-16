from bs4 import BeautifulSoup
import requests
import csv



#get_content()
    #save()

def get_content(r):
    soup = BeautifulSoup(r.text, 'html.parser')
    items = soup.findAll('div', class_='item product_listbox oh')
    list_laptop = []
    for item in items:
        list_laptop.append({
            'Название ноутбука': item.find('div', class_='listbox_title oh').get_text(strip=True),
            'Описание ноутбука': item.find('div', class_='product_text pull-left').get_text(strip=True),
            'Цена ноутбука': item.find('div', class_='listbox_price text-center').get_text(strip=True),
        })
    return list_laptop


    

def save(data):
    with open('laptops.csv', 'a') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Название ноутбука', 'Описание ноутбука', 'Цена ноутбука'])
        for item in data:
            writer.writerow([item['Название ноутбука'], item['Описание ноутбука'], item['Цена ноутбука']])

def pagenation():
    page = int(input('Сколько страниц спарсить: '))
    for i in range(1, page + 1):
        PAGENATOR = f'https://www.kivano.kg/noutbuki?page={i}'
        r = requests.get(PAGENATOR)
        data = get_content(r)
        save(data)
    print(f'Страница номер {i} готова')


if __name__ == '__main__':
  pagenation()

from bs4 import BeautifulSoup
import requests
import csv

CSV = 'sulpak.coffee.csv'
URL = 'https://www.sulpak.kg/f/kofemashiniy'
HEADER = {

}
def get_html():
    pass

def get_content()
    pass

def pagenation()
    pass

def save()
    pass

def get_content(r):
    soup = BeautifulSoup(r.text, 'html.parser')
    items = soup.findAll('div', class_='item product_listbox oh')
    list_coffee = []
    for item in items:
        list_coffee.append({
            'Картинка кофемашины': item.find('div', class_='goods-photo-container').get_text(strip=True),
            'Название кофемашины': item.find('div', class_='goods enhancement-ecommers-product-click enhancement-ecommers-product-view').get_text(strip=True),
            'Цена кофемашины': item.find('div', class_='old-price').get_text(strip=True),
        })
    return list_coffee


    

def save(data):
    with open('coffemashiny.csv', 'a') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Картинка', 'Название кофемашины', 'Цена кофемашины'])
        for item in data:
            writer.writerow([item['Картинка'], item['Название кофемашины'], item['Цена кофемашины']])

def pagenation():
    page = int(input('Сколько страниц спарсить: '))
    for i in range(1, page + 1):
        PAGENATOR = f'https://www.sulpak.kg/f/kofemashiniy{i}'
        r = requests.get(PAGENATOR)
        data = get_content(r)
        save(data)
    print(f'Страница номер {i} готова')


if __name__ == '__main__':
  pagenation()

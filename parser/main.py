import bs4
import requests
import xlsxwriter

main_url = "https://trade59.ru/"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Safari/605.1.15'}
data = [['Найменование', 'цена', 'Ссылки', 'картинка']]

def get_soup(url):
    res = requests.get(url, headers=headers)
    return bs4.BeautifulSoup(res.text, "html.parser")


categories_page = get_soup(main_url + "catalog.html?cid=7")
categories = categories_page.findAll('a', class_="cat_item_color")

for cat in categories:
    subcategories_page = get_soup(main_url + cat['href'])
    subcategories = subcategories_page.findAll('a', class_="cat_item_color")

    for subcat in subcategories:
        iphones_page = get_soup(main_url + subcat['href'])
        iphones = iphones_page.findAll('div', class_='items-list')

        for iphone in iphones:
            title = iphone.find('a')['title'].strip()
            price = iphone.find('div', class_='price').text.strip()
            url = iphone.find('a')['href'].strip()
            img = iphone.find('div', class_="image")['style'].split('url(')[1].split(')')[0].replace('/tn/', '/source/')
            data.append([title, price, url, img])

categories_page = get_soup(main_url + "catalog.html?cid=1011")
categories = categories_page.findAll('a', class_="cat_item_color")

for cat in categories:
    subcategories_page = get_soup(main_url + cat['href'])
    subcategories = subcategories_page.findAll('a', class_="cat_item_color")

    for subcat in subcategories:
        watches_page = get_soup(main_url + subcat['href'])  # замените на URL для часов
        watches = watches_page.findAll('div', class_='items-list')

        for watch in watches:
            title = watch.find('a')['title'].strip()
            price = watch.find('div', class_='price').text.strip()
            url = watch.find('a')['href'].strip()
            img = watch.find('div', class_="image")['style'].split('url(')[1].split(')')[0].replace('/tn/', '/source/')
            data.append([title, price, url, img])


categories_page = get_soup(main_url + "catalog.html?cid=8")
categories = categories_page.findAll('a', class_="cat_item_color")

for cat in categories:
    subcategories_page = get_soup(main_url + cat['href'])
    subcategories = subcategories_page.findAll('a', class_="cat_item_color")

    for subcat in subcategories:
        samsung_phones_page = get_soup(main_url + subcat['href'])
        samsung_phones = samsung_phones_page.findAll('div', class_='items-list')

        for phone in samsung_phones:
            title = phone.find('a')['title'].strip()
            price = phone.find('div', class_='price').text.strip()
            url = phone.find('a')['href'].strip()
            img = phone.find('div', class_="image")['style'].split('url(')[1].split(')')[0].replace('/tn/', '/source/')
            data.append([title, price, url, img])


with xlsxwriter.Workbook('Products.xlsx') as workbook:
    worksheet = workbook.add_worksheet()
    for row_num, info in enumerate(data):
        worksheet.write_row(row_num, 0, info)

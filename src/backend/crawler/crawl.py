from bs4 import BeautifulSoup
import requests

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    # 'Authorization': 'Bearer {}'.format('jina_521d4c70501c49a688c35e95800e72f8sYOXFclKuVLusF-PKEPbJPZY1tIU')
}

def get_vcar():
    with open('./vcar.html', 'r') as f:
        html = f.read()
    soup = BeautifulSoup(html, 'html.parser')
    loadlifecar = soup.find('tbody', class_='loadlifecar')
    banggiaxx = loadlifecar.find_all('tr', class_='banggiaxe-item init-banggia')
    m = {}
    for item in banggiaxx:
        href_tags = item.find_all(href=True)
        url = 'https://vnexpress.net'+href_tags[1]['href']
        m[url] = True
    return m.keys()


def get_car_detail(url: str, response_type='markdown') -> str:
    jina_reader_url = 'https://r.jina.ai/{}'.format(url)
    header = HEADERS
    header['x-respond-with'] = response_type
    response = requests.get(url=jina_reader_url, headers=header, timeout=60)
    if response.status_code != 200:
        raise Exception('Failed to fetch the page: {}, err: {}'.format(jina_reader_url, response.text))
    return response.text



def get_list_car_by_brand(brand: str):
    url = 'https://www.autofun.vn/{}'.format(brand)
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, 'html.parser')
    price_list = soup.find('div', class_='variant-price-list-content').find_all('div', class_='wa-model-unit-txt')
    m = {}
    for item in price_list:
        item = item.find_all(href=True)
        url = 'https://www.autofun.vn' + item[0]['href']
        m[url] = True
    return m.keys()

def get_brand_car():
    url = 'https://www.autofun.vn/xe-oto/'
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, 'html.parser')
    brand_list = soup.find_all('li', class_='brand-filter-group')
    res = []
    for brand in brand_list:
        items = brand.find_all('li', class_='brand-filter-item')
        for item in items:
            brand = item.find(href=True)
            url = 'https://www.autofun.vn/{}'.format(brand['href'])
            res.append(url)
    return res


ALL_CAR_AUTO_FUN = [
"https://www.autofun.vn/xe-oto/audi",
"https://www.autofun.vn/xe-oto/acura",
"https://www.autofun.vn/xe-oto/alfa-romeo",
"https://www.autofun.vn/xe-oto/aston-martin",
"https://www.autofun.vn/xe-oto/bmw",
"https://www.autofun.vn/xe-oto/baic",
"https://www.autofun.vn/xe-oto/bentley",
"https://www.autofun.vn/xe-oto/brilliance",
"https://www.autofun.vn/xe-oto/bugatti",
"https://www.autofun.vn/xe-oto/cadillac",
"https://www.autofun.vn/xe-oto/chevrolet",
"https://www.autofun.vn/xe-oto/daihatsu",
"https://www.autofun.vn/xe-oto/dongfeng",
"https://www.autofun.vn/xe-oto/ford",
"https://www.autofun.vn/xe-oto/ferrari",
"https://www.autofun.vn/xe-oto/genesis",
"https://www.autofun.vn/xe-oto/gmc",
"https://www.autofun.vn/xe-oto/hyundai",
"https://www.autofun.vn/xe-oto/honda",
"https://www.autofun.vn/xe-oto/hongqi",
"https://www.autofun.vn/xe-oto/infiniti",
"https://www.autofun.vn/xe-oto/isuzu",
"https://www.autofun.vn/xe-oto/jaguar",
"https://www.autofun.vn/xe-oto/jeep",
"https://www.autofun.vn/xe-oto/kia",
"https://www.autofun.vn/xe-oto/koenigsegg",
"https://www.autofun.vn/xe-oto/lexus",
"https://www.autofun.vn/xe-oto/land-rover",
"https://www.autofun.vn/xe-oto/lamborghini",
"https://www.autofun.vn/xe-oto/lincoln",
"https://www.autofun.vn/xe-oto/luxgen",
"https://www.autofun.vn/xe-oto/mazda",
"https://www.autofun.vn/xe-oto/mitsubishi",
"https://www.autofun.vn/xe-oto/mercedes-benz",
"https://www.autofun.vn/xe-oto/mini",
"https://www.autofun.vn/xe-oto/maserati",
"https://www.autofun.vn/xe-oto/mclaren",
"https://www.autofun.vn/xe-oto/mg",
"https://www.autofun.vn/xe-oto/nissan",
"https://www.autofun.vn/xe-oto/peugeot",
"https://www.autofun.vn/xe-oto/porsche",
"https://www.autofun.vn/xe-oto/pagani",
"https://www.autofun.vn/xe-oto/renault",
"https://www.autofun.vn/xe-oto/rolls-royce",
"https://www.autofun.vn/xe-oto/ram",
"https://www.autofun.vn/xe-oto/suzuki",
"https://www.autofun.vn/xe-oto/smart",
"https://www.autofun.vn/xe-oto/ssangyong",
"https://www.autofun.vn/xe-oto/subaru",
"https://www.autofun.vn/xe-oto/toyota",
"https://www.autofun.vn/xe-oto/tesla",
"https://www.autofun.vn/xe-oto/uaz",
"https://www.autofun.vn/xe-oto/vinfast",
"https://www.autofun.vn/xe-oto/volkswagen",
"https://www.autofun.vn/xe-oto/volvo",
"https://www.autofun.vn/xe-oto/zotye"
]


# if __name__ == '__main__':
    
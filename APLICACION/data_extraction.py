import os
import requests
from bs4 import BeautifulSoup
from image_download import download_image

def get_num_pages(base_url):
    response = requests.get(base_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        num_pages = 1
        next_link = soup.find('a', class_='next')
        while next_link:
            next_url = next_link['href']
            response = requests.get(next_url)
            if response.status_code == 200:
                num_pages += 1
                soup = BeautifulSoup(response.content, 'html.parser')
                next_link = soup.find('a', class_='next')
            else:
                print("Error al solicitar la página:", next_url)
                break
        return num_pages
    else:
        print("Error al solicitar la página:", base_url)
        return 0
    
def process_products(base_url, assets_path):
    num_pages = get_num_pages(base_url)
    print(f"Total pages: {num_pages}")
    product_data = []

    for page_num in range(1, num_pages + 1):
        if num_pages == 1:
            url = base_url
        else:
            url = base_url + "?p=" + str(page_num)
        
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            products = soup.find_all('li', class_='product-item')
            for product in products:
                product_code_tag = product.find('div', class_='marca')
                product_code = product_code_tag.find_all('span')[-1].text.strip() if product_code_tag else 'N/A'
                
                description_tag = product.find('a', class_='product-item-link')
                description = description_tag.text.strip() if description_tag else 'N/A'

                base_price_tag = product.find('span', class_='old-price')
                base_price = base_price_tag.find('span', class_='price').text.strip() if base_price_tag else 'N/A'

                discount_price_tag = product.find('span', class_='special-price')
                discount_price = discount_price_tag.find('span', class_='price').text.strip() if discount_price_tag else 'N/A'
                
                if discount_price == 'N/A':
                    normal_price_tag = product.find('span', class_='price-wrapper')
                    if normal_price_tag:
                        base_price = normal_price_tag.find('span', class_='price').text.strip()
                        discount_price = base_price
                
                image_tag = product.find('img', class_='product-image-photo')
                image_url = image_tag['src'] if image_tag else 'N/A'
                
                product_folder = os.path.join(assets_path, product_code)
                os.makedirs(product_folder, exist_ok=True)
                
                image_filename = download_image(image_url, product_folder)
                
                product_data.append({
                    'CODIGO_DE_PRODUCTO': product_code,
                    'DESCRIPCION': description,
                    'PRECIO_BASE': base_price,
                    'PRECIO_CON_DESCUENTO': discount_price,
                    'IMAGEN_DEL_PRODUCTO': image_filename
                })
        else:
            print("Error al solicitar la página:", url)
    
    return product_data


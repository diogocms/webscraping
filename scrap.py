import requests
from bs4 import BeautifulSoup
import time

class cm_scraper():

  def __init__(self):
    self.brands = []
    self.year_link = None

  def scrap(self, year_link):
    start = time.time()

    #listing link for brands
    page = requests.get(year_link)
    if page.status_code != 200:
      print("An error has ocurred in the main link")
    page_response = page.content
    page_content = BeautifulSoup(page_response, 'lxml')
    page_tags = page_content.find_all(class_="item-marca")
    page_links = []

    for page_tag in page_tags:
      page_links.append(page_tag['href'])


    #getting images by brand
    brands = []

    for link in page_links:
      brand_page = requests.get(link)
      if brand_page.status_code == 200:
        brand_response = brand_page.content
        brand_content = BeautifulSoup(brand_response, 'lxml')

        brand_pictures = []
        brand_name = brand_content.h1.string
        brand_tags = brand_content.find_all(class_="cont-foto")

        for tag in brand_tags:
          brand_pictures.append(tag.contents[1]["src"])

        brand = {'name': brand_name , 'url': link, 'links':brand_pictures}
        brands.append(brand)
      else:
        print("An error has ocurred in one of the brands")
        break


    end = time.time()
    time_stamp = round((end-start)/60, 4)

    print(f'Scraped in {time_stamp} minutes')
    print(f'{len(brands)} brands scraped')
    print()

    for brand in brands:
      print(brand["name"])

    self.brands = brands
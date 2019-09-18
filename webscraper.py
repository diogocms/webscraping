from selenium import webdriver
import time
import requests
from bs4 import BeautifulSoup

class scraper():
  def __init__(self): 
    self.ig_profile = None
    
    self.fmi_brands = []
    self.year_link = None

  def ig_scrap(self, url, frames):
    frames = int(frames)
    start = time.time()
    options = webdriver.FirefoxOptions()
    options.add_argument('-headless')
    browser = webdriver.Firefox(executable_path='./geckodriver', firefox_options=options)
    browser.get(url)

    pictures = []
    meta_data = {}
    
    for i in range(frames):
      profile_pictures = browser.find_elements_by_class_name("FFVAD")
      profile_name = browser.find_element_by_tag_name("h1")

      for picture in profile_pictures:
        pictures.append(picture.get_attribute('src'))
        meta_data[picture.get_attribute('src')] = picture.get_attribute('alt')

      browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
      time.sleep(1)

    pictures = list(dict.fromkeys(pictures))
    profile_pictures = []

    for i in range(len(pictures)):
      profile_pictures.append({'link' : pictures[i] , 'meta' : meta_data[pictures[i]]})

      

    profile_result = {'name': profile_name.text, 'pictures' : profile_pictures}
    self.ig_profile = profile_result

    end = time.time()
    time_stamp = round((end - start)/60, 4)

    print(f'Scraped in {time_stamp} minutes')
    print(f'{len(profile_pictures)} pictures captured!')

    browser.close()

    
  def fmi_scrap(self, year_url):
    start = time.time()
    #listing link for brands
    page = requests.get(year_url)

    if page.status_code != 200:
      print("An error has ocurred in the main url")
    page_response = page.content
    page_content = BeautifulSoup(page_response, 'lxml')
    page_tags = page_content.find_all(class_="item-marca")
    page_urls = []

    for page_tag in page_tags:
      page_urls.append(page_tag['href'])

    for link in page_urls:
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
        self.fmi_brands.append(brand)
      else:
        print("An error has ocurred in one of the brands")
        break
    end = time.time()
    time_stamp = round((end-start)/60, 4)
    print(f'Scraped in {time_stamp} minutes')
    print(f'{len(self.fmi_brands)} brands scraped')
    print()
    for brand in self.fmi_brands:
      print(brand["name"])
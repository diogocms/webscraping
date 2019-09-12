from selenium import webdriver
import time

class IGscraper():
  def __init__(self): 
    self.profile = None

  def scrap(self, url, frames):
    frames = int(frames)
    start = time.time()
    browser = webdriver.Firefox(executable_path="./geckodriver")
    browser.get(url)

    for i in range(frames):
      browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
      time.sleep(1)

    profile_name = browser.find_element_by_tag_name("h1")
    profile_pictures = browser.find_elements_by_class_name("FFVAD")

    pictures = []

    for picture in profile_pictures:
      pictures.append({'link': picture.get_attribute('src'), 'meta': picture.get_attribute('alt')})

    profile_result = {'name': profile_name.text, 'pictures' : pictures}

    self.profile = profile_result

    end = time.time()
    time_stamp = round((end - start)/60, 4)

    print(f'Scraped in {time_stamp} minutes')
    print(f'{len(pictures)} pictures captured!')





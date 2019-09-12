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
    self.profile = profile_result

    end = time.time()
    time_stamp = round((end - start)/60, 4)

    print(f'Scraped in {time_stamp} minutes')
    print(f'{len(profile_pictures)} pictures captured!')





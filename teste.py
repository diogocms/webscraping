
'''
from webscraper import scraper

meuscrap = scraper()

meuscrap.ig_scrap('https://www.instagram.com/zenzi.mila/', 20)

print(meuscrap.ig_profile)
'''




from webscraper import scraper

meu_scraper = scraper()

meu_scraper.fmi_scrap("https://fimi.es/en/galeriaspasarela/public/marcas?id=14&idferia=1&f=4")

print(meu_scraper.fmi_brands)
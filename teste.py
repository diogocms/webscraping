from scrap import cm_scraper

meu_scraper = cm_scraper()

meu_scraper.scrap("https://fimi.es/en/galeriaspasarela/public/marcas?id=14&idferia=1&f=4")

print(meu_scraper.brands)
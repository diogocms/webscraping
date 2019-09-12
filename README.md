# webscraping

FMI Scraper:<br>
1 - importar o arquivo scrap.py<br>
2 - criar um novo objeto pertencente a class cm_scraper (ex. new_obj = cm_scraper( ) )<br>
3 - executar o metodo .scrap("link") no objeto<br>
4 - "link" - a url do ano do desfile<br>
5 - Depois de metodo .brands retorna o dicionário com os dados (ex. dados = new_obj.brands)<br>

IG Scraper:<br>
1 - importar o arquivo igscraper.py<br>
2 - criar um novo objeto pertencente a classe IGscraper (ex. new_obj = IGscraper( ) )<br>
3 - executar o metodo .scrap("url", "frames") no objeto<br>
4 - "url" - a url do perfil<br>
5 - "frames" o numero de frames que o scraper deve verificar no perfil (cada frame contem aprox. 12 fotos).<br>
5 - Depois de metodo .profile retorna o dicionário com os dados (ex. dados = new_obj.profile)<br>

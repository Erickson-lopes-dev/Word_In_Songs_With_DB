from functions.web_scraping import main_artist_page

artist = input('Digite o artista/banda: ')

data_page_artist = main_artist_page(artist)

if data_page_artist:
    print(data_page_artist)
else:
    print('404')

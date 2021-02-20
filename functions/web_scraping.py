import requests
from bs4 import BeautifulSoup


def main_artist_page(artist):
    # faz a requisição na página
    req_get = requests.get(f'https://www.vagalume.com.br/{artist.replace(" ", "-").lower()}/')

    if req_get.status_code == 200:
        try:
            # Cria o obj python do corpo html recebido com o beautifulsoup
            obj_bs4 = BeautifulSoup(req_get.content, 'html.parser')

            # busca o cunteudo dentro da clase 'nameMusic' que contem o link para cada musica
            list_alfabet = obj_bs4.find(id='alfabetMusicList').find_all(class_='nameMusic')
        except:
            pass
        else:
            # retorna o obj
            return list_alfabet

    # Se caso o artista não for encontrado retorna uma lsita vazia
    print(f'Nenhum item encontrado ! {artist}')
    return []


def searching_lyrics(artist):
    data_page_artist = main_artist_page(artist)

    if data_page_artist:
        for item in data_page_artist:
            print(item.text, 'https://www.vagalume.com.br' + item.attrs['href'])


if __name__ == '__main__':

    searching_lyrics('')

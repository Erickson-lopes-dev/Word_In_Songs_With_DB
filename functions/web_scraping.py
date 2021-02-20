import requests
from bs4 import BeautifulSoup


def main_artist_page(artist):
    # faz a requisição na página
    req_get = requests.get(f'https://www.vagalume.com.br/{artist.replace(" ", "-").lower()}/')

    if req_get.status_code == 200:
        # Cria o obj python do corpo html recebido com o beautifulsoup
        obj_bs4 = BeautifulSoup(req_get.content, 'html.parser')

        # busca o cunteudo dentro da clase 'nameMusic'
        list_alfabet = obj_bs4.find(id='alfabetMusicList').find_all(class_='nameMusic')

        return list_alfabet

    # Se caso o artista não for encontrado retorna uma lsita vazia
    return []


if __name__ == '__main__':
    for item in main_artist_page('raul'):
        print(item.attrs['href'])
        print(item.text)

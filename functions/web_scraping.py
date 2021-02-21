import string
import requests
from bs4 import BeautifulSoup


def main_artist_page(artist):
    # faz a requisição na página
    req_get = requests.get(f'https://www.vagalume.com.br/{artist.replace(" ", "-").lower()}/')

    # Verifica se o status code é 200
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
    # retorna uma lista vazia
    return []


def searching_lyrics(artist):
    data_page_artist = main_artist_page(artist)

    # for item in tqdm(data_page_artist, desc='Pesquisando musicas'):
    for item in data_page_artist:
        link_lyric = 'https://www.vagalume.com.br' + item.attrs['href']

        req_get = requests.get(link_lyric)
        soup_lyric = BeautifulSoup(req_get.content, 'html.parser')
        lyric_no_format = soup_lyric.find(id='lyrics').contents

        lyric_format = []

        for teste in lyric_no_format:
            if str(teste) != '<br/>':
                lyric_format.append(str(teste))
        print('\n')

        print(item.text, link_lyric)
        lyric_format = ' /-/ '.join(lyric_format)
        print(lyric_format)


if __name__ == '__main__':
    searching_lyrics('nirvana')

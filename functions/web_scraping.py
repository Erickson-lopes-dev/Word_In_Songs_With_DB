import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from colorama import Fore, init

# auto reseta o colorama
init(autoreset=True)


# Função para retornar os links de todas as músicas
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

    # retorna uma lista vazia
    return []


# Função para capturar todas as letras das musicas
def searching_lyrics(artist, id_artist):
    # varaivel que ira retornar os dados coletado
    return_data_lyric = []

    for item in tqdm(main_artist_page(artist), desc='Coletando Lyrics', bar_format=Fore.YELLOW + "{l_bar} {bar} {r_bar}"):
        # Cria o link para a música
        link_lyric = 'https://www.vagalume.com.br' + item.attrs['href']
        # realiza a requisição GET no link
        req_get = requests.get(link_lyric)
        # Tranforma o html em bs4 para analisarmos
        soup_lyric = BeautifulSoup(req_get.content, 'html.parser')
        # recebe a letra da música
        lyric_no_format = soup_lyric.find(id='lyrics').contents
        # variavel para receber a letra formatada
        lyric_format = []
        # por cada item recebido
        for stanza in lyric_no_format:
            # se a estrofe não for igual a <br/>
            if str(stanza) != '<br/>':
                # adiciona dentro da lista
                lyric_format.append(str(stanza))

        # Concatena os itens dentro da lista (a cada estrofe irá conter esse '/-/' )
        lyric_format = ' /-/ '.join(lyric_format)

        # Cria um item dentro da lista com o nome, letra da musica capsulando em um dicionario
        return_data_lyric.append([item.text, link_lyric, lyric_format, id_artist])
    print()
    # retorna a lista com os dadoos de cada música
    return return_data_lyric


if __name__ == '__main__':
    print(searching_lyrics('raul', 12))
    # x = return_data('raul')
    # print(x)
    # if x:
    #     for item in x:
    #         print(item)

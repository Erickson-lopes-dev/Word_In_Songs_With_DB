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
def searching_lyrics(list_lyrics):
    # varaivel que ira retornar os dados coletado
    return_data_lyric = []

    for item in tqdm(list_lyrics, desc='Coletando Lyrics', bar_format=Fore.GREEN + "{l_bar} {bar} {r_bar}"):
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

        # Cria um item dentro da lista com o nome, link e letra da musica capsulando em um dicionario
        return_data_lyric.append({'name': item.text, 'link': link_lyric, 'lyric': lyric_format})
    print()
    # retorna a lista com os dadoos de cada música
    return return_data_lyric


# Função Retorna a junção dos dados
def return_data(artist):
    page_main = main_artist_page(artist)
    if page_main:
        print(Fore.GREEN + f"[!] '{artist.capitalize()}' Encontrado !\n")
        return {'artist': artist.capitalize(), 'lyrics': searching_lyrics(page_main)}
    else:
        print(Fore.RED + f"[!] '{artist.capitalize()}' não foi encontrado, Por favor tente outro vez!")
        return []


if __name__ == '__main__':
    x = return_data('racionais mcs')
    if x:
        print(x)

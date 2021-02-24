from functions.database import DataBase
from functions.web_scraping import main_artist_page, searching_lyrics
from colorama import Fore, init
from prettytable import PrettyTable

init(autoreset=True)
# artist = input('Digite o artista/banda:').lower()
# tirar a pontuação
artist = 'roberto carlos'.lower()
db = DataBase()


def artist_all():
    # Cria a tabela especificando passa as colunas
    table = PrettyTable(['id', 'Artista/Banda'])
    # alinha os itens da tabela a esquerda
    table.align = 'l'
    if db.artist_all():
        [table.add_row([item[0], item[1].capitalize()]) for item in db.artist_all()]
    else:
        table.add_row([0, 'Nenhum item encontrado!'])
    # exibe a tabela
    print(table)


artist_all()


def insert_database(artist_search):
    search_artist = db.search_artist_db(artist_search)

    print(Fore.YELLOW + '[!] Realizando busca no banco de dados')

    if search_artist:
        print(Fore.GREEN + '[!] Artista existe no banco de dados!  \n')
    else:
        print(Fore.RED + f"[!] '{artist_search}' Não foi encontrado em seu banco de dados. \n")

        # se algo for retornado na função
        if main_artist_page(artist_search):
            print(Fore.YELLOW + '[!] Iniciando download.')
            # Adiciona o artista no banco de dados
            db.add_artisct_db(artist_search)
            # recebe os lyrics
            lyrics = searching_lyrics(artist_search, db.search_artist_db(artist_search)[0][0])
            # recebe a chave do id
            db.add_lyrics(lyrics)

        else:
            print(Fore.RED + f"[!] Não foi possível encontrar por '{artist_search}', tente novamente! \n")

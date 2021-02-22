from functions.database import DataBase
from functions.web_scraping import main_artist_page, searching_lyrics
from colorama import Fore, init


init(autoreset=True)
artist = input('Digite o artista/banda:').lower()

db = DataBase()

print('')

search_artist = db.search_artist_db(artist)

if search_artist:
    print('[!] Artista existe no banco de dados! ')
else:
    print(Fore.RED + f"[!] '{artist}' Não foi encontrado em seu banco de dados. \n")
    print(Fore.YELLOW + '[!] Iniciando download. \n')

    # se algo for retornado na função
    if main_artist_page(artist):
        #
        db.add_artisct_db(artist)
        print(searching_lyrics(artist, 1))
    else:
        print(Fore.RED + f"[!] Não foi possível encontrar por '{artist}', tente novamente!")



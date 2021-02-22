from functions.database import DataBase
from functions.web_scraping import main_artist_page, searching_lyrics
from colorama import Fore, init


init(autoreset=True)
# artist = input('Digite o artista/banda:').lower()
# tirar a pontuação
artist = 'mamonas assassinas'.lower()
db = DataBase()

print('')

search_artist = db.search_artist_db(artist)

if search_artist:
    print('[!] Artista existe no banco de dados!  \n')
else:
    print(Fore.RED + f"[!] '{artist}' Não foi encontrado em seu banco de dados. \n")

    # se algo for retornado na função
    if main_artist_page(artist):
        print(Fore.YELLOW + '[!] Iniciando download. \n')
        # Adiciona o artista no banco de dados
        db.add_artisct_db(artist)
        # recebe os lyrics
        lyrics = searching_lyrics(artist, db.search_artist_db(artist)[0][0])
        # recebe a chave do id
        db.add_lyrics(lyrics)

    else:
        print(Fore.RED + f"[!] Não foi possível encontrar por '{artist}', tente novamente! \n")



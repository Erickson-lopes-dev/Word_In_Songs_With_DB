from functions.database import DataBase
from colorama import Fore, init

from functions.web_scraping import return_data

init(autoreset=True)
artist = input('Digite o artista/banda:').lower()

db = DataBase()

print('')

search_artist = db.search_artist_db(artist)

if search_artist:
    print()
else:
    print(Fore.RED + f"[!] '{artist}' Não foi encontrado em seu banco de dados. \n")

    print(Fore.YELLOW + '[!] Iniciando busca. \n')

    x = return_data(artist)
    print(x)


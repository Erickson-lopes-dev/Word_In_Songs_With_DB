from functions.database import DataBase

artist = input('Digite o artista/banda: ').lower()

db = DataBase()
print(db.search_artist_db(artist))


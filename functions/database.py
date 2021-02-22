import os
import sqlite3
from colorama import Fore, init

# auto reseta o colorama
init(autoreset=True)


class DataBase:
    def __init__(self):
        """Em geral o init vai procurar criar o banco de dados"""
        # nome da base de dados
        self.name_file = 'database.db'

        # verifica se o arquivo db existe
        if not os.path.exists(self.name_file):
            try:
                # tenta abrir uma conexão com o banco
                conn = sqlite3.connect(self.name_file)
                # cria um cursor
                cursor = conn.cursor()
                # Cria a coluna artist
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS artist( 
                        id integer primary key,
                        name text
                        );
                    ''')
                # Cria acoluna lyrics, relacionando o artista
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS lyrics(
                        id integer primary key,
                        name text,
                        lyric text,
                        link text,
                        id_artist integer,
                        FOREIGN KEY (id_artist) REFERENCES artist (name)
                        );
                    ''')
                # fecha conexão
                conn.close()
            except:
                # Exibe a mensagem de erro
                print(Fore.RED + '[!] Não foi possível criar o banco de dados. ')
                # Caso ocorra algum erro, exclui a base
                os.remove(self.name_file)
            else:
                print(Fore.GREEN + '[!] Banco de dados Criado com sucesso!')

    # Verifica se o nome do artista
    def search_artist_db(self, artist):
        conn = sqlite3.connect(self.name_file)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM artist WHERE name = '{artist.lower()}'")
        return cursor.fetchall()

    def add_artisct_db(self, artist):
        try:
            conn = sqlite3.connect(self.name_file)
            cursor = conn.cursor()
            cursor.execute(f"INSERT INTO artist (name) VALUES ('{artist.lower()}')")
            conn.commit()
            conn.close()
        except:
            print(Fore.RED + '[!] Não foi possível Adicionar o artista ao banco de dados!')
        else:
            print(Fore.GREEN + f"[!] '{artist}' Adicionado com sucesso ao banco de dados! ")

    def add_lyrics(self, lyrics):
        conn = sqlite3.connect(self.name_file)
        cursor = conn.cursor()
        sql = "INSERT INTO lyrics (name, lyric, id_artist) Values (?, ?, ?)"
        cursor.executemany(sql, lyrics)
        conn.commit()


if __name__ == '__main__':
    db = DataBase()
    print(db.search_artist_db('glovis'))

import requests
import os
from bs4 import BeautifulSoup as soup

suffix = "lol"
url = "https://otakudesu." + suffix + "/"
error_connection = """
Tidak dapat menghubung ke server!
Coba ulangi lagi atau mungkin server lagi down
"""
null_space = ""
null_obj = "[]"

#debug!
y = "variable 200 OK!"

def cls():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
def search_judul():
    while True:
        input_search = input("search: ")
        if not input_search.strip():
            pass
        else:
            search_query = input_search.replace(" ", "+")
            search = (url + "?s=" + search_query + "&post_type=anime")
            find_anime = requests.get(search)

            if find_anime.status_code == 200:
                parsing_search_anime = soup(find_anime.text, "html.parser")
                content_search_anime = parsing_search_anime.find(
                    "ul", {"class": "chivsrc"})

                if content_search_anime is not None:
                    content = content_search_anime.find_all(
                        "a", href=True, title=True)

                    if content:
                        cls()
                        print("Judul yang ditemukan:\n")
                        for i, link in enumerate(content):
                            title = link.text
                            print(f"{i+1}. {title}")
                        print("99. Kembali")
                        break
                    else:
                        cls()
                        print("Judul tidak ditemukan!\n")
            else:
                print(error_connection)
                exit()
    while True:
        num_content = input("Pilih nomor: ")
        if num_content == "99":
            cls()
            search_judul()
            break
        try:
            num_content = int(num_content)
            if num_content > 0 and num_content <= len(content):
                break
        except ValueError:
            pass
        

cls()
find_judul_anime = None
banner = "ASUNIME!"
version = "1.0dev"
print(banner + " " + version + "\n")
search_judul()
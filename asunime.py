import requests
import os
from bs4 import BeautifulSoup as soup
import processing

# basic variable
banner = "ASUNIME!"
version = "1.0dev"
suffix = "lol"

# ambil base url menggunakan suffix yang ada di basic variable
# eg: => https://link.com/
url = "https://otakudesu." + suffix + "/"

# ketika koneksi error pada url saat mengambil data
error_connection = """
Tidak dapat menghubung ke server!
Coba ulangi lagi atau mungkin server lagi down
"""

# null_character
null_space = ""
null_obj = "[]"

# melakukan clear pada terminal


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# begin script


clear()
print(banner + " " + version)
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
                    clear()
                    print("Judul yang ditemukan:\n")
                    for i, link in enumerate(content):
                        title = link.text
                        print(f"{i+1}. {title}")
                    break
                else:
                    clear()
                    print("Judul tidak ditemukan!\n")
        else:
            print(error_connection)
            exit()

while True:
    num_content = input("Pilih nomor: ")
    try:
        num_content = int(num_content)
        if num_content > 0 and num_content <= len(content):
            break
    except ValueError:
        pass

url_episode = content[num_content-1].get("href")

response_episode = requests.get(url_episode)
parsing_episode = soup(response_episode.text, "html.parser")

judul_episode = parsing_episode.find_all(
    "a", href=lambda href: href and ("/episode/" in href or "/batch/" in href))

if judul_episode:
    clear()
    print("Episode yang ditemukan:\n")
    for a, eps in enumerate(judul_episode):
        episode = eps.text
        print(f"{a+1}. {episode}")

print(null_space)

while True:
    num_eps = input("Pilih nomor: ")
    try:
        num_eps = int(num_eps)
        if num_eps > 0 and num_eps <= len(judul_episode):
            break
    except ValueError:
        pass

url_stream = judul_episode[num_eps-1].get("href")
response_stream = requests.get(url_stream)
parsing_stream = soup(response_stream.text, "html.parser")

clear()
print("1. Streaming")
print("2. Downloads")

print(null_space)

while True:
    stream = input("Pilih Nomor: ")
    if stream == '1':
        clear()
        processing.get_mirror(parsing_stream, url_stream)
        break
    elif stream == '2':
        # get_download()
        # OGP
        break
    else:
        pass

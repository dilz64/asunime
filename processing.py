import os
import base64
import json
import requests
from bs4 import BeautifulSoup as s
import media_player

quality_list = {'360p': 'm360p', '480p': 'm480p', '720p': 'm720p'}


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def quality():
    print("Kualitas yang tersedia:\n")
    for a, quality in enumerate(quality_list):
        print(f"{a+1}. {quality}")
    while True:
        quality_choice = input("Pilih nomor: ")
        if quality_choice.isdigit() and int(quality_choice) in range(1, len(quality_list)+1):
            break
        else:
            pass

    return quality_list[list(quality_list.keys())[int(quality_choice)-1]]


def get_mirror(parsing_stream, url_stream):
    quality_choice = quality()
    link = parsing_stream.find('div', {'class': 'mirrorstream'})
    ul_parse_mirror = link.find('ul', {'class': quality_choice})
    parse_mirror = ul_parse_mirror.find_all('li')
    clear()
    print("Mirror yang tersedia:\n")
    if parse_mirror:
        for a, q360 in enumerate(parse_mirror):
            mirror_360 = q360.find('a')
            if mirror_360 is not None:
                print(f"{a+1}. {mirror_360.text}")
            else:
                print(f"{a+1}. Mirror tidak ditemukan")

        while True:
            mirror_choice = input("Pilih mirror: ")
            if mirror_choice.isdigit() and int(mirror_choice) in range(1, len(parse_mirror)+1):
                selected_mirror = parse_mirror[int(mirror_choice)-1]
                selected_mirror_a = selected_mirror.find('a')
                data_content = selected_mirror_a.get('data-content')
                get_video_id(data_content, url_stream)
                break
            else:
                pass
    else:
        clear()
        print("Tidak ada mirror di kualitas tersebut! coba pilih yang lain.")
        get_mirror(parsing_stream, url_stream)


def get_video_id(data_content, url_stream):

    decoded_data_content = base64.b64decode(data_content)
    parse_data_content = json.loads(decoded_data_content)
    id = parse_data_content['id']
    i = parse_data_content['i']
    q = parse_data_content['q']
    # next make def
    nonce_url = "https://otakudesu.lol/wp-admin/admin-ajax.php"
    nonce_data = {
        "action": "aa1208d27f29ca340c92c66d1926f13f"
    }
    nonce_post = requests.post(nonce_url, data=nonce_data)
    nonce_str = nonce_post.text
    nocne_parse = json.loads(nonce_str)
    nonce_value = nocne_parse["data"]

    action_value = "2a3505c93b0035d3f455df82bf976b84"
    post_url = 'https://otakudesu.lol/wp-admin/admin-ajax.php'
    payload = {
        'id': id,
        'i': i,
        'q': q,
        'nonce': nonce_value,
        'action': action_value
    }
    get_video_data = requests.post(post_url, data=payload)

    data_str = get_video_data.text
    data_load = json.loads(data_str)
    data_value = data_load['data']
    data_value_decode = base64.b64decode(data_value)
    get_video_url = s(data_value_decode, 'html.parser')
    video_url = get_video_url.find('iframe')
    vide_src = get_video_url.find('iframe')['src']#
    clear()
    media_player.initial_stream(video_url, vide_src)
from bs4 import BeautifulSoup as soup
import requests
import os

url = "https://otakudesu.lol/"

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def search_titles():
    while True:
        search_titles_input = input("search: ")
        if not search_titles_input.strip():
            pass
        else:
            query_search_titles = search_titles_input.replace(" ", "+")
            fetch_search_titles = (url + "?s=" + query_search_titles + "&post_type=anime")
            request_search_titles = requests.get(fetch_search_titles)

            if request_search_titles.status_code == 200:
                parsing_search_titles = soup(request_search_titles.text, "html.parser")
                parse_search_titles = parsing_search_titles.find("ul", {"class": "chivsrc"})
                
                if parse_search_titles is not None:
                    search_titles_contents = parse_search_titles.find_all("a", href=True, title=True)
                    return search_titles_contents
            else:
                print("error")
                exit()

def parsing_titles(search_titles_contents):
    if search_titles_contents:
        for contents_num, content_urls in enumerate(search_titles_contents):
            content_titles = content_urls.text
            print(f"{contents_num+1}.{content_titles}")
    else:
        print("Not Found!")
        

search_result = search_titles()
parsed_results = parsing_titles(search_result)


import requests
from bs4 import BeautifulSoup

counter_pdf = 1

def get_links_to_files(url):
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, 'html.parser')

    link = soup.find_all('a')
    links = []
    for elem in link:
        links.append(elem['href'])

    return links[13:len(links)-1]

def take_all_files(links, folder):
    global counter_pdf
    for elem in links:
        counter_pdf += 1
        file_response = requests.get(elem)
        with open(folder + str(counter_pdf) + '.pdf', 'wb') as f:
            try:
                f.write(file_response.content)
            except Exception as e:
                print(f"Error processing image on file {counter_pdf}")


# print(get_links_to_files(url))
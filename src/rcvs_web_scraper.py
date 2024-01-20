import requests
from bs4 import BeautifulSoup

base_url = """
https://findavet.rcvs.org.uk/find-a-vet-practice/?filter-choice=&filter-keyword=+&filter-searchtype=practice&p="""


def get_url(url, page):
    full_url = url + str(page)
    print(full_url)
    return requests.get(full_url)


def make_soup(html):
    return BeautifulSoup(html.content, "lxml")


these_pages = range(1, 3)

for this_page in these_pages:
    html_data = get_url(base_url, this_page)
    soup = make_soup(html_data)

    all_practice_names = soup.select("div.practice h2.item-title")
    practice_names = []
    for practice in all_practice_names:
        practice_names.append((practice.get_text(strip=True)))
    print(practice_names)

    all_practice_addresses = soup.select("div.practice div.item-address")
    practice_addresses = []
    for practice in all_practice_addresses:
        practice_addresses.append((practice.get_text(strip=True)))
    print(practice_addresses)

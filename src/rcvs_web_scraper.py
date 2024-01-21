import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

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

    all_practice_tels = soup.select("div.practice div.item-contact span.item-contact-tel")
    temp_practice_tels = []
    for practice in all_practice_tels:
        temp_practice_tels.append((practice.get_text(strip=True)))
    practice_tels = []
    for temp_practice_tel in temp_practice_tels:
        practice_tels.append(re.sub(r"phone2", "", temp_practice_tel))

    all_practice_emails = soup.select("div.practice div.item-contact a.item-contact-email")
    temp_practice_emails = []
    for practice in all_practice_emails:
        temp_practice_emails.append((practice.get_text(strip=True)))
    practice_emails = []
    for temp_practice_email in temp_practice_emails:
        practice_emails.append(re.sub(r"envelope", "", temp_practice_email))

    df = pd.DataFrame(list(zip(practice_names, practice_addresses, practice_tels, practice_emails)),
                      columns=["Name", "Address", "Tel", "Email"])
    print(df)

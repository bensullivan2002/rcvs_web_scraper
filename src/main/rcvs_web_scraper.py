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


these_pages = range(1, 544)

practice_names = []
practice_addresses = []
practice_postcodes = []
practice_tels = []
practice_emails = []

for this_page in these_pages:
    html_data = get_url(base_url, this_page)
    soup = make_soup(html_data)

    practices = soup.select("div.practice")

    for practice in practices:

        practice_names.append(practice.h2.text.strip())

        practice_addresses.append(practice.div.text.strip())

        contacts = practice.find("div", class_="item-contact")
        try:
            temp_phone = contacts.span.text.strip()
        except Exception as e:
            temp_phone = ""
        stripped_temp_phone = re.sub("\n\n\n ", "", temp_phone)

        practice_tels.append(re.sub("phone2", "", stripped_temp_phone))
        try:
            temp_email = contacts.a.text.strip()
        except Exception as e:
            temp_email = ""
        stripped_temp_email = re.sub("\n\n\n ", "", temp_email)
        practice_emails.append(re.sub("envelope", "", stripped_temp_email))

for practice_address in practice_addresses:
    results = re.findall("^([Gg][Ii][Rr] 0[Aa]{2})|((([A-Za-z][0-9]{1,2})|(([A-Za-z][A-Ha-hJ-Yj-y][0-9]{1,2})|(([A-Za-z][0-9][A-Za-z])|([A-Za-z][A-Ha-hJ-Yj-y][0-9]?[A-Za-z])))) [0-9][A-Za-z]{2})$", practice_address)
    count = 0
    if len(results) == 0:
        postcode = ""
        practice_postcodes.append(postcode)
    if len(results) > 0:
        for result in results[0]:
            if len(result) > count:
                count = len(result)
                postcode = result
                practice_postcodes.append(postcode)

df = pd.DataFrame(list(zip(practice_names, practice_addresses, practice_postcodes, practice_tels, practice_emails)),
                  columns=["Name", "Address", "Postcode", "Tel", "Email"])
# print(df)

df.to_csv("out.csv", index=False)

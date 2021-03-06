#!/usr/bin/python3

import json

# Below canteens will be scraped by default by scrape.py
CANTEENS = {
    "bioc": "https://www.biocenter.ku.dk/kantine/menuoversigt/",
    "akb": "https://www1.bio.ku.dk/akb/kantine/menuoversigt/"
}


def get_menu_week(link):
    import requests
    from bs4 import BeautifulSoup

    if link.lower() in CANTEENS.keys():
        link = CANTEENS[link.lower()]

    r = requests.get(link)
    soup = BeautifulSoup(r.text, "html.parser")

    menu_body = soup.select_one("div#content-wrapper").table

    menu = []
    weekday = -1  # For correct indexing with lists below

    for row in menu_body.find_all("tr")[1:]:
        row_text = row.text.strip()

        if row_text.startswith("Uge"):
            weekday += 1
            menu.append({})

        if ":" in row_text:
            dish_type, dish = row_text.split(":")
            menu[weekday].update({dish_type: dish})

    return menu


def load_menu_from_json(canteen):
    with open(canteen.lower() + ".json") as f:
        return json.load(f)

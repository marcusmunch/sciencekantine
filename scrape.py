import json

import kukantine


def main():
    for name, link in kukantine.CANTEENS.items():
        menu = kukantine.get_menu_week(link)

        with open(name.lower() + ".json", "w") as f:
            json.dump(menu, f, indent=4)


if __name__ == "__main__":
    main()

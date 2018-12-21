import datetime

from argparse import ArgumentParser

import kukantine


def motd(sep=", "):
    today_weekday = datetime.datetime.today().weekday()

    parser = ArgumentParser()
    parser.add_argument("-s", "--separator", help="String to use for separation of the different menu items. "
                                                  "Defaults to \", \".")
    parser.add_argument("canteen", help="Enter canteen for which menu is wanted")
    parser.add_argument("-d", help="Debug mode", action="store_true")
    args = parser.parse_args()

    if not args.d:
        menu = kukantine.get_menu_week(args.canteen)
    else:
        import json
        with open(args.canteen.lower() + ".json") as f:
            menu = json.load(f)[args.canteen]

    motd = menu[today_weekday]

    return sep.join(["%s: %s" % (k, v) for k, v in motd.items()])


def main():
    print(motd())


if __name__ == "__main__":
    main()

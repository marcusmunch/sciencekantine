import datetime
import sys

from argparse import ArgumentParser

import kukantine


def get_motd(canteen, debug=False, sep=", "):
    today_weekday = datetime.datetime.today().weekday()

    if not debug:
        menu = kukantine.get_menu_week(canteen)

    else:
        if today_weekday > 4:
            today_weekday = 4

        menu = kukantine.load_menu_from_json(canteen)

    print(menu)

    try:
        motd = menu[today_weekday]

    except IndexError:
        print("An error occured. This might be because it's the weekend today.")
        sys.exit(1)

    return sep.join(["%s: %s" % (k, v) for k, v in motd.items()])


def main():
    parser = ArgumentParser()
    parser.add_argument("-s", "--separator", help="String to use for separation of the different menu items. "
                                                  "Defaults to \", \".")
    parser.add_argument("canteen", help="Enter canteen for which menu is wanted")
    parser.add_argument("-d", help="Debug mode", action="store_true")
    args = parser.parse_args()

    if args.d:
        debug = True
    else:
        debug = False

    print(get_motd(args.canteen, debug=debug))


if __name__ == "__main__":
    main()

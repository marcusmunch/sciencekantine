import datetime
import sys

from argparse import ArgumentParser

import kukantine


def get_motd(args):
    today_weekday = datetime.datetime.today().weekday()

    if args.l:
        menu = kukantine.load_menu_from_json(args.canteen)
    else:
        menu = kukantine.get_menu_week(args.canteen)

    if args.t:
        today_weekday += args.t
    if args.d:
        if today_weekday > 4:
            today_weekday = 0
    if today_weekday > 4:
        print("Error: Couldn't find menu for given day")
        exit(1)

    try:
        motd = {k: v for k, v in menu[today_weekday].items() if v}

    except IndexError:
        print("Weekday is out of range (e.g. it's the weekend).")
        sys.exit(1)

    if not args.separator:
        args.separator = ", "

    menu_string = args.separator.join(["%s: %s" % (k, v) for k, v in motd.items()])

    return menu_string


def main():
    parser = ArgumentParser()
    parser.add_argument("-s", "--separator", help="String to use for separation of the different menu items. "
                                                  "Defaults to \", \".")
    parser.add_argument("canteen", help="Enter canteen for which menu is wanted")
    parser.add_argument("-l", help="Local mode - load from local files.", action="store_true")
    parser.add_argument("-d", help="Debug mode", action="store_true")
    parser.add_argument("-t", help="Get menu a number of days from today (e.g. 1 for tomorrow)", type=int)
    args = parser.parse_args()

    print(get_motd(args))


if __name__ == "__main__":
    main()

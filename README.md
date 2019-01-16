# sciencekantine

SCIENCEkantine gives you the menu of the day at University of Copenhagen, Faculty of Science. Currently two canteens are supported (`BioC` for Biocenter and `AKB` for August Krogh Building canteens)

## Usage

The repo currently contains three scripts:
- `kukantine.py` is the central API for the repository. Scraping and loading from local files is contained in this file.
- `scrape.py` scrapes the currently displayed menu of the week for the default canteens stored within `kukantine.py` and saves them to `akb.json` and `bioc.json`
- `motd.py` is where the magic happens. Usage is as follows:
```bash
python motd.py [-d] [-l] [-t n] CANTEEN
```

## Options
- `-d`:       Debug mode. If you're running `motd.py` during the weekend, an IndexError will be raised since you'll be looking for more menu items than listed on the website. `-d` prevents this by manually setting the current weekday to Monday within the script.
- `-l`:       Load mode. Skips downloading the menu from the web page and loads from the local JSON files.
- `-t n`:     Gets the menu for the given `CANTEEN` `n` days in the future (e.g. `-t 1` for tomorrow)
- `CANTEEN`:  Canteen to get Today's menu from. Takes one of the two canteens described above or a link. Supplied link has to be a page formatted like the default canteens' pages.

### Possible future features
- [x] `+n` days. Typically +1 in order to get the menu for tomorrow. Useful for knowing whether or not to bring lunch the next day.
from glob import glob
from datetime import date


class Day:
    def __init__(self, name, emoji):
        self.name = name
        self.emoji = emoji


days = {
    1: Day('Sonar Sweep', '🧭'),
    2: Day('Dive!', '🌊'),
    3: Day('Binary Diagnostic', '📈'),
    4: Day('Giant Squid', '🐙'),
    5: Day('Hydrothermal Venture', '♨'),
    6: Day('Lanternfish', '🐟'),
    7: Day('The Treachery of Whales', '🐳'),
    8: Day('Seven Segment Search', '📡'),
    9: Day('Smoke Basin', '🌫'),
    10: Day('Syntax Scoring', '✔'),
    11: Day('Dumbo Octopus', '🦑'),
    12: Day('Passage Pathing', '🗺'),
    13: Day('Transparent Origami', '🧻'),
    14: Day('Extended Polymerization', '⚗'),
    15: Day('', ''),
    16: Day('', ''),
    17: Day('', ''),
    18: Day('', ''),
    19: Day('', ''),
    20: Day('', ''),
    21: Day('', ''),
    22: Day('', ''),
    23: Day('', ''),
    24: Day('', ''),
    25: Day('', ''),
}


def write_table_row(first, second, third):
    f.write('|' + first + '|' + second + '|' + third + '|\n')


f = open('../README.md', 'a', encoding="utf-8")

todays_date = date.today()
year = str(todays_date.year)

# File header
f.write('# 🎄 🎅 Advent of code ' + year + ' 🎅 🎄\n')
f.write('My Advent of Code (Season ' + year + ') solutions written in Python 😀\n\n')

# Table
# Table Header
write_table_row('#', 'Problem ☃', 'Solution ❄')
write_table_row('---', '-------------', ':-------------:')

directories = glob("../*/")
directories = sorted([int(y) for y in list(filter(lambda d: str.isdigit(d), [x.strip('..\\') for x in directories]))])


def create_url(idx, day):
    return "[" + day.name + "](" + "https://adventofcode.com/" + year + "/day/" + str(idx) + ") " + day.emoji


def get_files(day):
    raw_files = glob('..//{day}/*.py'.format(day=day))

    return [y.replace('\\', '/') for y in [x.strip('..//') for x in raw_files]]


for day_idx in directories:
    day_str = str(day_idx)
    files = get_files(day_str)

    file_links = ""
    for i, file in enumerate(files):
        if i > 0:
            file_links += " - "
        file_links += "[Part {p}]({file})".format(file=files[0], p=i + 1)

    write_table_row(day_str, create_url(day_str, days[day_idx]), file_links)

f.close()

from glob import glob
from datetime import date


class Day:
    def __init__(self, name, emoji):
        self.name = name
        self.emoji = emoji


days = {
    1: Day('Sonar Sweep', '๐งญ'),
    2: Day('Dive!', '๐'),
    3: Day('Binary Diagnostic', '๐'),
    4: Day('Giant Squid', '๐'),
    5: Day('Hydrothermal Venture', 'โจ'),
    6: Day('Lanternfish', '๐'),
    7: Day('The Treachery of Whales', '๐ณ'),
    8: Day('Seven Segment Search', '๐ก'),
    9: Day('Smoke Basin', '๐ซ'),
    10: Day('Syntax Scoring', 'โ'),
    11: Day('Dumbo Octopus', '๐ฆ'),
    12: Day('Passage Pathing', '๐บ'),
    13: Day('Transparent Origami', '๐งป'),
    14: Day('Extended Polymerization', 'โ'),
    15: Day('Chiton', '๐บ'),
    16: Day('Packet Decoder', '0๏ธโฃ1๏ธโฃ'),
    17: Day('Trick Shot', '๐'),
    18: Day('Snailfish', '๐'),
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
f.write('# ๐ ๐ Advent of code ' + year + ' ๐ ๐\n')
f.write('My Advent of Code (Season ' + year + ') solutions written in Python ๐\n\n')

# Table
# Table Header
write_table_row('#', 'Problem โ', 'Solution โ')
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
    if len(files) == 1:
        file_links = "[Part 1 & 2]({file})".format(file=files[0])
    if len(files) == 2:
        for i, file in enumerate(files):
            if i > 0:
                file_links += " - "
            file_links += "[Part {p}]({file})".format(file=files[i], p=i + 1)

    write_table_row(day_str, create_url(day_str, days[day_idx]), file_links)

f.close()

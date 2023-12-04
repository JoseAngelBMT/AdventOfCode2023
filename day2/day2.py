from functools import reduce
import re
from operator import mul

RED: int = 12
GREEN: int = 13
BLUE: int = 14

def not_possible(result: dict) -> bool:
    if result['red'] > RED or result['green'] > GREEN or result['blue'] > BLUE:
        return True
    return False

def process_line(line: str) -> int:
    info = line[0].split(':')
    id = int(re.findall(r'\d+', info[0])[0])
    games = info[1].split(';')

    patron = re.compile(r'(\d+) (green|red|blue)')
    result = {'green': 0, 'red': 0, 'blue': 0}
    result_game = result.copy()
    for game in games:
        match = patron.findall(game)
        result_game.update({col: int(count) for count, col in match})
        for k, v in result_game.items():
            if k in result and v > result[k]:
                result[k] = v
    return reduce(mul, result.values())

def process_line_minimun_set(line: str) -> int:
    info = line[0].split(':')
    id = int(re.findall(r'\d+', info[0])[0])
    games = info[1].split(';')

    patron = re.compile(r'(\d+) (green|red|blue)')

    for game in games:
        match = patron.findall(game)
        result = {'green': 0, 'red': 0, 'blue': 0}
        result.update({col: int(count) for count, col in match})
        if not_possible(result):
            return 0
    return id

with open('day2.txt') as f:
    lines = [[line.replace('\n','')] for line in f]

sum_map = map(process_line, lines)
sum_ids = reduce(lambda x, acc: acc+x, sum_map, 0)
print(sum_ids)
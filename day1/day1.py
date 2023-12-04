import os
import re

number_dict = {'eightwo': '82', 'twone': '21', 'eighthree': '83', 'sevenine': '79', 'oneight': '18', 'nineight': '98',
               'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
def transform(l: list) -> int:
    return int(l[0]+l[-1])

def replace_dict(l: list, number: dict) -> str:
    for k, v in number.items():
        l = l.replace(k,v)
    return l

lines = []
with open('day1.txt') as f:
    lines = [line for line in f]

lines = list(map(lambda x: replace_dict(x, number_dict), lines))
lines_sum = [re.findall(r'\d', l) for l in lines]
number = list(map(lambda x: transform(x), lines_sum))

print(sum(number))
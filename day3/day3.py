

def search_numbers(matrix: list, i: int, i: int) -> int:
    pass

with open('test.txt', 'r') as f:
    matrix = [line.replace('\n', '') for line in f]
print(matrix)

sum_numbers = 0

for i, row in enumerate(matrix):
    number = ''
    for j, c in enumerate(row):
        if c.isdigit():
            number += c
        else:
            number = ''


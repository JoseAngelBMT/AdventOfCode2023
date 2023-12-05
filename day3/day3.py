import math

def is_valid(matrix: list[str], r: int, c: int) -> bool:
    rows, cols = len(matrix), len(matrix[0])
    adjacent: list[tuple] = [(r+i, c+j) for i in [-1, 0, 1] for j in [-1, 0, 1] if (i, j) != (r, c)]
    for adj in adjacent:
        if (0 <= adj[0] < rows) and (0 <= adj[1] < cols):
            value = matrix[adj[0]][adj[1]]
            if not value.isdigit() and value != '.':
                return True
    return False


def get_sum_matrix(matrix: list[str]) -> int:
    sum_numbers = 0
    for i, row in enumerate(matrix):
        number: str = ''
        valid: bool = False
        for j, ch in enumerate(row):
            if ch.isdigit():
                number += ch
                valid = valid or is_valid(matrix, i, j)
            else:
                sum_numbers += int(number) if valid else 0
                number = ''
                valid = False
        sum_numbers += int(number) if valid else 0
    return sum_numbers


def is_gear(matrix: list[str], r: int, c: int) -> tuple | None:
    rows, cols = len(matrix), len(matrix[0])
    adjacent: list[tuple] = [(r+i, c+j) for i in [-1, 0, 1] for j in [-1, 0, 1] if (i, j) != (r, c)]
    for adj in adjacent:
        if (0 <= adj[0] < rows) and (0 <= adj[1] < cols):
            value = matrix[adj[0]][adj[1]]
            if value == '*':
                return (adj[0], adj[1])
    return None


def get_sum_gears(matrix: list[str]) -> int:
    gear_numbers: dict = {}
    for i, row in enumerate(matrix):
        number: str = ''
        valid: tuple | None = None
        for j, ch in enumerate(row):
            if ch.isdigit():
                number += ch
                if valid is None:
                    valid = is_gear(matrix, i, j)
            else:
                if valid is not None:
                    if valid not in gear_numbers:
                        gear_numbers[valid] = [int(number)]
                    else:
                        gear_numbers[valid] += [int(number)]
                number = ''
                valid = None

        if valid is not None:
            if valid not in gear_numbers:
                gear_numbers[valid] = [int(number)]
            else:
                gear_numbers[valid] += [int(number)]
    two_gears = [li for li in list(gear_numbers.values()) if len(li) == 2]
    gear_numbers = [math.prod(li) for li in two_gears]
    return sum(gear_numbers)


def main() -> None:
    with open('day3.txt', 'r') as f:
        matrix: list[str] = [line.rstrip() for line in f]
    sum_part1: int = get_sum_matrix(matrix)
    print(sum_part1)
    sum_part2: int = get_sum_gears(matrix)
    print(sum_part2)



if __name__ == '__main__':
    main()




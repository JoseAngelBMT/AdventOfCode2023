import re

def card_matches(line: str) -> int:
    game: str = line.split(': ')[1]
    game = re.findall(r'\d+', game)
    return len(game) - len(set(game))
def part1(lines: list[str]) -> int:
    sum_games: int = 0
    for line in lines:
        number = card_matches(line)
        sum_games += int(2**(number -1))
    return sum_games

def part2(lines: list[str]) -> int:
    cards: list[int] = [1 for _ in lines]
    for i, line in enumerate(lines):
        number: int = card_matches(line)
        for j in range(i + 1, i + number + 1):
            cards[j] += cards[i]
    return sum(cards)


def main() -> None:
    with open('day4.txt') as f:
        lines = [line.rstrip() for line in f]

    sum_part1: int = part1(lines)
    print(sum_part1)
    sum_part2: int = part2(lines)
    print(sum_part2)

if __name__ == '__main__':
    main()
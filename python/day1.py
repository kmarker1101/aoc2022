"""Solution to Day1 AOC 2022"""


INPUT_FILE = "Data/Day01/input.txt"


def day_one(file_name):
    """Solves Day1"""
    totals = []
    count = 0
    with open(file_name, 'r', encoding="utf-8") as file:
        for line in file:
            if line.strip() != '':
                count += int(line)
                totals.append(count)
            else:
                count = 0
    return totals


if __name__ == "__main__":
    result = (day_one(INPUT_FILE))
    result.sort(reverse=True)
    print(f"The soltion to part 1 is {result[0]}")
    print(f"The soltion to part 2 is {sum(result[0:3])}")

import re

def main():
    data: str = ''

    with open('data.txt', 'r') as file:
        data = file.read()

    pattern = r'mul\(\d{1,3},\d{1,3}\)'
    pattern2 = r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)"
    result: int = find_occurences(data, pattern)

    print(result)


def find_occurences(data, pattern):
    matches: list[str] = re.findall(pattern=pattern, string=data)
    
    sol: int = 0
    for match in matches:
        numbers = re.findall(r'\d{1,3}', match)
        num1, num2 = int(numbers[0]), int(numbers[1])
        sol += num1 * num2
    return sol

def find_better_ocurrences(data, pattern):
    pass

if __name__ == '__main__':
    main()
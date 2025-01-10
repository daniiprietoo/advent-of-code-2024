import re

def main():
    data: str = ''

    with open('data.txt', 'r') as file:
        data = file.read()

    pattern = r'mul\(\d{1,3},\d{1,3}\)'
    result1: int = find_occurences(data, pattern)
    print(f'Part 1 result: {result1}')

    pattern2 = r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)"
    result2: int = find_better_ocurrences(data, pattern2)
    print(f'Part 2 result: {result2}')
    


def find_occurences(data, pattern):
    matches: list[str] = re.findall(pattern=pattern, string=data)
    
    sol: int = 0
    for match in matches:
        numbers = re.findall(r'\d{1,3}', match)
        num1, num2 = int(numbers[0]), int(numbers[1])
        sol += num1 * num2
    return sol

def find_better_ocurrences(data, pattern):
    matches: list[str] = re.findall(pattern=pattern, string=data)

    sol: int = 0

    allowed: bool = True

    for match in matches:
        match = match.strip()
        if match == 'do()':
            allowed = True
        elif match == "don't()":
            print('dont')
            allowed = False
        elif match.startswith('mul') and allowed:
            numbers = re.findall(r'\d{1,3}', match)
            num1, num2 = int(numbers[0]), int(numbers[1])
            sol += num1 * num2
    
    return sol


if __name__ == '__main__':
    main()
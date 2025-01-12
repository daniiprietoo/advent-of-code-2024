def main():
    equations = [
        # (190, [10, 19]),
        # (3267, [81, 40, 27]),
        # (83, [17, 5]),
        # (156, [15, 6]),
        # (7290, [6, 8, 6, 15]),
        # (161011, [16, 10, 13]),
        # (192, [17, 8, 14]),
        # (21037, [9, 7, 18, 13]),
        # (292, [11, 6, 16, 20]),
    ]

    with open('data.txt', 'r') as file:
        for line in file:
            data = line.strip().split(" ")
            equation = (int(data[0][:-1]), [int(x) for x in data[1:]])
            equations.append(equation)

    print(total_calibration_result(equations))

def total_calibration_result(equations):
    total_calibration: int = 0

    for equation in equations:
        if is_valid(equation[0], equation[1]):
            total_calibration += equation[0]
        
    return total_calibration

def is_valid(target_value, numbers):
    return backtrack(target_value, numbers, 0, numbers[0])

# Backtracking algorithm, when the combinations gets in the base case evaluates and if it find any that it's true, it returns true 
def backtrack(target_value, numbers, index, current_val):

    if len(numbers) - 1 == index:
        return current_val == target_value
    
    if backtrack(target_value, numbers, index + 1, current_val + numbers[index + 1]):
        return True
    
    if backtrack(target_value, numbers, index + 1, current_val * numbers[index + 1]):
        return True
    
    # For part 2, concatenate by creating a f string and cast them back to integers
    if backtrack(target_value, numbers, index + 1, int(f'{current_val}{numbers[index + 1]}')):
        return True
    
    return False 


if __name__ == '__main__':
    main()
from collections import Counter

def distance_between_arrays(array1: list[int], array2: list[int]) -> int:
    """
    Calculate the sum of absolute distances between corresponding elements in 
    two integer arrays of the same length

    Args:
        array1 (list[int]): first list of integers
        array2 (list[int]): second list of integers

    Returns:
        int: sum of absolute distances
    """
    array1.sort()
    array2.sort()

    distance: int = 0
    for i in range(len(array1)):
        distance += abs(array1[i] - array2[i])

    return distance

def similarity_between_arrays(array1: list[int], array2: list[int]) -> int:
    """
    Calculate the similarity score of two integers arrays of the same length.
    Calculation is done based on the elements of array1 times their number of appearance in array2

    Args:
        array1 (list[int]): first list of integers
        array2 (list[int]): second list of integers

    Returns:
        int: similarity score
    """
    counter = Counter(array2)

    score: int = 0
    for num in array1:
        score += num * counter[num]
    
    return score

def main():
    arr1: list[int] = []
    arr2: list[int] = []

    with open('data.txt', 'r') as file:
        for line in file:   
            line = line.strip()
            nums = line.split("   ")
            arr1.append(int(nums[0]))
            arr2.append(int(nums[1]))
    
    part1_sol: int = distance_between_arrays(arr1, arr2)
    
    part2_sol: int = similarity_between_arrays(arr1, arr2)

    print(f'Solution to the first part (distance between arrays):\n{part1_sol}\n    ')
    print(f'Solution to the second part (similarity score of arrays):\n{part2_sol}')

if __name__ == "__main__":
    main()

        
        

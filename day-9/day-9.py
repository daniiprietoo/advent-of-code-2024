def main():
    with open('data.txt', 'r') as file:
        disk_map = file.read().strip()
    # disk_map = '2333133121414131402'
    print(calculate_final_checksum(disk_map))

def calculate_final_checksum(disk_map: str) -> int:
    layout = create_layout(disk_map)

    left = 0 
    right = len(layout) - 1

    while left < right:
        if layout[left] == '.':
            layout[left], layout[right] = layout[right], layout[left]
            left += 1
            right -= 1
        while layout[left] != '.':
            left += 1
        while layout[right] == '.':
            right -= 1

    checksum = 0
    index = 0
    while layout[index] != '.':
        checksum += index * int(layout[index])
        index += 1
    return checksum        

def create_layout(disk_map: str) -> list[list[str]]:
    layout = []
    for i in range(len(disk_map)):
        if i%2 == 0:
            for _ in range(int(disk_map[i])):   
                layout.append(str(i//2))
        else:
            for _ in range(int(disk_map[i])):   
                layout.append('.')

    return layout



if __name__ == '__main__':
    main()
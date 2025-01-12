def main():
    grid = []

    with open('data.txt', 'r') as file:
        for line in file:
            grid.append(line.strip())

    print(predict_positions(grid))


def predict_positions(grid):
    directions_map = {'^': 0, '>': 1, 'v': 2, '<': 3}  # Possible directions
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]    # Movements corresponding to UP, RIGHT, DOWN, LEFT

    rows = len(grid)
    cols = len(grid[0])

    positions_visited = set()

    # Find the starting position
    position = None
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] in directions_map:
                position = (row, col)
                direction = directions_map[grid[row][col]]
                break
        if position:
            break

    # Iterate until the guard moves out of the grid
    while 0 <= position[0] < rows and 0 <= position[1] < cols:
        # Mark the position as visited
        positions_visited.add(position)

        # Get the direction the guard is facing
        dir_row, dir_col = directions[direction]
        front_pos = (position[0] + dir_row, position[1] + dir_col)

        # If front pos is out of bounds, break to prevent index out of bound 
        if not (0 <= front_pos[0] < rows and 0 <= front_pos[1] < cols):
            break

        if grid[front_pos[0]][front_pos[1]] == '#':
            direction = (direction + 1) % 4  # Turn right (clockwise)
        else:
            # Otherwise, move forward
            position = front_pos

    return len(positions_visited)

if __name__ == '__main__':
    main()

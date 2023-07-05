with open(r'H:\OneDrive\Programme\VS\Personal\Advent Calendar 2021\Day_15_Input.txt', "r") as f:
    matrix = (f.read().splitlines())

def dfs(matrix, row, col, total):
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    # Check if we reached the bottom right corner
    if row == num_rows - 1 and col == num_cols - 1:
        # Add the current cell value to the total
        total += int(matrix[row][col])
        return total

    # Add the current cell value to the total
    total += int(matrix[row][col])

    # Explore the path going down
    if row + 1 < num_rows:
        path_down = dfs(matrix, row + 1, col, total)

    # Explore the path going right
    if col + 1 < num_cols:
        path_right = dfs(matrix, row, col + 1, total)

    # Return the path with the lowest total
    if row + 1 < num_rows and col + 1 < num_cols:
        return min(path_down, path_right)
    elif row + 1 < num_rows:
        return path_down
    elif col + 1 < num_cols:
        return path_right

    return total

def find_lowest_total(matrix):
    return dfs(matrix, 0, 0, 0)

lowest_total = find_lowest_total(matrix)
print(lowest_total)
print(matrix)
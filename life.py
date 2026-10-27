
grid = [ 
    [0 , 0 , 0 , 0 , 0 ], 
    [0 , 0 , 1 , 0 , 0 ], 
    [0 , 1 , 1 , 1 , 0 ], 
    [0 , 0 , 1 , 0 , 0 ], 
    [0 , 0 , 0 , 0 , 0 ] 
]

# 1. Initialize the counter
living_count = 0

# 2. Use a nested loop to go through rows and then individual cells
for row in grid:
    for cell in row:
        if cell == 1:
            living_count += 1

print(living_count)
Total_row = len(grid)
Total_col = len(grid[0])
living_neighbor = 0
for r, row in enumerate(grid):
    for c, cell in enumerate(row):
        if cell == 1:
            print(f"FOR LIVING CELL AT co-ordinates: {r}, {c} ")
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue
                    neighbor_r = r + dr
                    neighbor_c = c + dc
                    if  (0 <= neighbor_r and neighbor_r < Total_row) and (0 <= neighbor_c and neighbor_c < Total_col):
                            neighbor_value = grid[neighbor_r][neighbor_c]
                            living_neighbor = 0
                            if neighbor_value == 1:
                                living_neighbor += 1
                                print(f"({neighbor_r},{neighbor_c})is living")
                            if living_neighbor > 1:
                                print(f"Cell at ({r}, {c}) lives")
                            else: 
                                print("The cell has died")
                                for r, row in enumerate(grid):
                                 for c, cell in enumerate(row):
                                     cell = 0
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

#we have 4 elements, they are all lists. we gotta a grids: 4 rows, 3 columns
#access individual elements
#number_grid[row][column]
print(number_grid[0][1])

#nested for loop
#'for row in nested_grid:' prints every row
# 'for column in row: print(column[2]') prints all columns 
for row in number_grid:
    print(row)
    for column in row:
        print(column)
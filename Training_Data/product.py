data = [
    [5, 7, 5], 
    [3, 1000, 1000],
    [3, 3, 1000, 7],
    [3, 3, 1000, 1000], 
    [5, 7, 5, 3, 3, 1000, 1000],
    [3, 1000, 1000, 7],
    [7, 1000, 1000],
    [3, 7, 3, 1000],
    [5, 7, 5, 3, 3, 1000],
    [5, 7, 3, 1000],
    [3, 1000, 1000, 5, 7]
]
product = 1
for row in data:
    row_product = 1
    for num in row:
        row_product *= num
    product += row_product


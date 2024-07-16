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


{
    "words": "Plot scattergraph KRTAP29-1 (Nerves) and LEPR", 
    "tokens": [
               "Plot", "scattergraph", "KRTAP29-1", 
               "(", "Nerves", ")", "and", "LEPR"
              ], 
    "NER_TAG": [
                "O", "B-PLOT_TYPE", "B-X_AXIS_LABEL", "I-X_AXIS_LABEL", 
                "I-X_AXIS_LABEL", "I-X_AXIS_LABEL", "O", "B-Y_AXIS_LABEL"
               ], 
    "NER_ENCODING": [0, 1, 3, 4, 4, 4, 0, 5]
}
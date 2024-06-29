
verb_create = ["Generate", "Manufacture", "Create", "Make", "Plot"] 

verb_show = ["display", "visualize", "highlight", "show", "exhibit"]

noun_relationship = ["relationship", "correlation", "link"]

# Plot type

scatterplot_name_var = ["scatterplot", "scatter plot", "scatter", "scatterchart", "scatter chart", "scattergraph", "scatter graph"]

# Variables

exp_lvl_singular = ["expression level", "expression", "level of expression"]

exp_lvl_plural = ["expression levels", "expressions", "levels of expression"]

protein_x_axis = ["a", "b"]
protein_y_axis = ["c", "d"]

gene_x_axis = ["e", "f"]
gene_y_axis = ["g", "h"]


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

print("Product:", product)
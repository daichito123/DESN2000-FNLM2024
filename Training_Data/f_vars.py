import pandas as pd

def select_genes(file_path, n_genes, state, col_name):
    df = pd.read_csv(file_path)
    genes = df[col_name].dropna().sample(n=n_genes, random_state=state)
    genes = genes.tolist()
    return genes

# 'O' Tag
# vc
verb_create = [
    "Chart", "Graph", "Diagram", 
    "Outline", "Sketch", "Design",
    "Depict", "Create", "Make", "Generate", "Plot",  
]

# vs
verb_show = [
    "Picture", "See", "Perceive", 
    "View", "Conceive", "Visualize",  
    "Render", "Illustrate", 
    "Image", 
    "Display", "Show", "Present", 
    "visualize", "show", "exhibit"
]

# nr
noun_relationship = ["relationship", "correlation", "link", 'connection']

# els
exp_lvl_singular = ["expression level", "expression"]
# elp
exp_lvl_plural = ["expression levels", "levels of expression"]

# Plot type
# snv
scatterplot_name_var = ["scatterplot", "scatter", "scatter chart", "scattergraph"]

# X or Y axis labels
# com_x
common_x_axis = []
# com_y
common_y_axis = ["patient age", "DNA methylation levels"]

file_path = 'csv/human_organs.csv'
# org_x
organ_x_axis = [f"({element})" for element in select_genes(file_path, 25, 1, 'Organ')]
# org_y
organ_y_axis = [f"({element})" for element in select_genes(file_path, 25, 2, 'Organ')]

# oth_x
other_x_axis = ["(Treated)", "(Untreated)", "(Control)"]
# oth_y
other_y_axis = ["(Treated)", "(Untreated)", "(Control)"]

file_path = 'csv/proteins.csv'
# pr_x
protein_x_axis = select_genes(file_path, 250, 1, 'HGNC Symbol')
# pr_y
protein_y_axis = select_genes(file_path, 250, 2, 'HGNC Symbol')

file_path = 'csv/genes.csv'
# g_x
gene_x_axis = select_genes(file_path, 15000, 1, 'Approved symbol')
# g_y
gene_y_axis = select_genes(file_path, 15000, 2, 'Approved symbol')
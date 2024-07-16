import pandas as pd
import random

def select_genes(file_path, n_genes, state, col_name):
    df = pd.read_csv(file_path)
    genes = df[col_name].dropna().sample(n=n_genes, random_state=state)
    genes = genes.tolist()
    return genes

def RNG(high):
    rand_val = random.randint(0, high - 1)
    return rand_val

def concat_lists(list1, list2):
    concatenated = []
    l1 = len(list1)
    l2 = len(list2)
    for i in range(max(l1, l2)):
        l1_element = list1[RNG(l1)]
        l2_element = list2[RNG(l2)]
        l2_element = f"({l2_element})"
        concatenated.append(l1_element + ' ' + l2_element)
    return concatenated

# 'O' Tag
# vc
verb_create = [
    "Diagram", 
    "Outline", "Sketch", "Design",
    "Depict", "Create", "Make", "Generate",  
]

# vp
verb_plot = [
    "Plot", "Chart", "Graph"
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
scatterplot_name_var = ["scatterplot", "scatter", "scatter chart", "scattergraph", "scatter plot", "scatterchart", "scatter graph"]

# X or Y axis labels
# com_x
common_x_axis = []
# com_y
common_y_axis = ["patient age", "DNA methylation levels"]

file_path = 'csv/human_organs.csv'
# org_x
organ_x_axis = select_genes(file_path, 25, 1, 'Organ')
# org_y
organ_y_axis = select_genes(file_path, 25, 2, 'Organ')

# oth_x
other_x_axis = ["treated", "untreated", "control"]
# oth_y
other_y_axis = ["treated", "untreated", "control"]

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

# gene and organ (x axis) - gox
gene_organ_x_axis = concat_lists(gene_x_axis, organ_x_axis)
# gene and organ (y axis) - goy
gene_organ_y_axis = concat_lists(gene_y_axis, organ_y_axis)

# protein and organ (x axis) - pox
protein_organ_x_axis = concat_lists(protein_x_axis, organ_x_axis)
# protein and organ (y axis) - poy
protein_organ_y_axis = concat_lists(protein_y_axis, organ_y_axis)

# gene and other (x axis) - gothx
gene_other_x_axis = concat_lists(gene_x_axis, other_x_axis)
# gene and other (y axis) - gothy
gene_other_y_axis = concat_lists(gene_y_axis, other_y_axis)
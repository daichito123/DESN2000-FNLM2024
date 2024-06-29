import re
import itertools

from f_vars import verb_create, verb_show
from f_vars import noun_relationship
from f_vars import scatterplot_name_var
from f_vars import exp_lvl_plural, exp_lvl_singular
from f_vars import gene_x_axis, gene_y_axis
from f_vars import protein_x_axis, protein_y_axis

def generate_combinations(w2d, template, vars):
    # Generate all combinations from the mega list using itertools.product
    combinations = itertools.product(*w2d)
    
    # Format the template string with each combination using replace
    formatted_strings = []
    for combo in combinations:
        # combo = [x, y, z]
        # vars = [vc, snv, vs]
        formatted_string = template
        for i, word in enumerate(combo):
            if vars[i] == 'vc':
                formatted_string = formatted_string.replace("{vc}", word)
            elif vars[i] == 'vs':
                formatted_string = formatted_string.replace("{vs}", word)
            elif vars[i] == 'nr':
                formatted_string = formatted_string.replace("{nr}", word)
            elif vars[i] == 'snv':
                formatted_string = formatted_string.replace("{snv}", word)
            elif vars[i] == 'els':
                formatted_string = formatted_string.replace("{els}", word)
            elif vars[i] == 'elp':
                formatted_string = formatted_string.replace("{elp}", word)
            elif vars[i] == 'g_x':
                formatted_string = formatted_string.replace("{g_x}", word)
            elif vars[i] == 'g_y':
                formatted_string = formatted_string.replace("{g_y}", word)
            elif vars[i] == 'pr_x':
                formatted_string = formatted_string.replace("{pr_x}", word)
            elif vars[i] == 'pr_y':
                formatted_string = formatted_string.replace("{pr_y}", word)
        formatted_string = re.sub(r'"', '', formatted_string)
        formatted_strings.append(formatted_string)
    
    return formatted_strings

# Extract placeholders
def extract_placeholders(template):
    pattern = re.compile(r'\{.*?\}')
    return pattern.findall(template)

# Reorder filtered data
def order_data(template, data):
    placeholders = extract_placeholders(template)

    # Reorder the list based on precomputed placeholder positions
    ordered_data = [None] * len(placeholders)
    for item in data:
        if item['tag'] in placeholders:
            index = placeholders.index(item['tag'])
            ordered_data[index] = item
    return ordered_data

# Returns an array of all strings
def f2prompts(str_in):
    # initialize data
    data = [
        {'key': 'vc', 'tag': """{vc}""", 'bool': False, 'data': verb_create},
        {'key': 'vs', 'tag': """{vs}""", 'bool': False, 'data': verb_show},
        {'key': 'nr', 'tag': """{nr}""", 'bool': False, 'data': noun_relationship},
        {'key': 'snv', 'tag': """{snv}""", 'bool': False, 'data': scatterplot_name_var},
        {'key': 'els', 'tag': """{els}""", 'bool': False, 'data': exp_lvl_singular},
        {'key': 'elp', 'tag': """{elp}""", 'bool': False, 'data': exp_lvl_plural},
        {'key': 'g_x', 'tag': """{g_x}""", 'bool': False, 'data': gene_x_axis},
        {'key': 'g_y', 'tag': """{g_y}""", 'bool': False, 'data': gene_y_axis},
        {'key': 'pr_x', 'tag': """{pr_x}""", 'bool': False, 'data': protein_x_axis},
        {'key': 'pr_y', 'tag': """{pr_y}""", 'bool': False, 'data': protein_y_axis}
    ]

    # Find vars
    vars = re.findall(r'{(.*?)}', str_in)

    # Set bools
    for dict in data:
        key = dict['key']
        if key in vars:
            dict['bool'] = True

    # Filter data
    filtered = [item for item in data if item['bool']]

    # Order data
    data = order_data(str_in, filtered)

    # Define mega list
    w2d = [w['data'] for w in data]

    # Generate the formatted strings
    formatted_strings = generate_combinations(w2d, str_in, vars)
    return formatted_strings

def main():
    with open('empty_tags/scatter_empty_tags.txt', 'r') as f_in, open('prompts/scatter_prompts.txt', 'w') as f_out:
        for line in f_in:
            prompts = f2prompts(line)
            for prompt in prompts:
                f_out.write(prompt)

if __name__ == "__main__":
    main()
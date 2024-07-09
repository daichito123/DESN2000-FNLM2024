import re
import itertools
import json
import os

from nltk.tokenize import word_tokenize

from f_vars import verb_create, verb_show
from f_vars import noun_relationship
from f_vars import scatterplot_name_var
from f_vars import exp_lvl_plural, exp_lvl_singular
from f_vars import gene_x_axis, gene_y_axis
from f_vars import protein_x_axis, protein_y_axis
from f_vars import common_x_axis, common_y_axis
from f_vars import organ_x_axis, organ_y_axis
from f_vars import other_x_axis, other_y_axis

from create_token_object import create_token_object

def generate_files(w2d, str_in, vars, txt_path, json_path):
    # Generate all combinations from the mega list using itertools.product
    combinations = itertools.product(*w2d)
    
    # Format the template string with each combination using replace
    # prompts = []
    # jsons = []
    for comb_number, combo in enumerate(combinations):
        # combo = [x, y, z]
        # vars = [vc, snv, vs]
        formatted_string = str_in
        tokens = []
        for i, input in enumerate(combo):
            # 'O' tag
            if vars[i] == 'vc':
                formatted_string = formatted_string.replace("{vc}", input)
                token_object = create_token_object(input, 'O', 'B')
                tokens.append(token_object)
            elif vars[i] == 'vs':
                formatted_string = formatted_string.replace("{vs}", input)
                token_object = create_token_object(input, 'O', 'B')
                tokens.append(token_object)
            elif vars[i] == 'nr':
                formatted_string = formatted_string.replace("{nr}", input)
                token_object = create_token_object(input, 'O', 'B')
                tokens.append(token_object)
            elif vars[i] == 'els':
                formatted_string = formatted_string.replace("{els}", input)
                token_object = create_token_object(input, 'O', 'B')
                tokens.append(token_object)
            elif vars[i] == 'elp':
                formatted_string = formatted_string.replace("{elp}", input)
                token_object = create_token_object(input, 'O', 'B')
                tokens.append(token_object)
            # Plot type tag
            elif vars[i] == 'snv':
                formatted_string = formatted_string.replace("{snv}", input)
                token_object = create_token_object(input, 'P', 'B')
                tokens.append(token_object)
            # X or Y axis tag
            elif vars[i] == 'g_x':
                formatted_string = formatted_string.replace("{g_x}", input)
                token_object = create_token_object(input, 'X', 'B')
                tokens.append(token_object)
            elif vars[i] == 'g_y':
                formatted_string = formatted_string.replace("{g_y}", input)
                token_object = create_token_object(input, 'Y', 'B')
                tokens.append(token_object)
            elif vars[i] == 'pr_x':
                formatted_string = formatted_string.replace("{pr_x}", input)
                token_object = create_token_object(input, 'X', 'B')
                tokens.append(token_object)
            elif vars[i] == 'pr_y':
                formatted_string = formatted_string.replace("{pr_y}", input)
                token_object = create_token_object(input, 'Y', 'B')
                tokens.append(token_object)
            elif vars[i] == 'com_x':
                formatted_string = formatted_string.replace("{com_x}", input)
                token_object = create_token_object(input, 'X', 'B')
                tokens.append(token_object)
            elif vars[i] == 'com_y':
                formatted_string = formatted_string.replace("{com_y}", input)
                token_object = create_token_object(input, 'Y', 'B')
                tokens.append(token_object)
            elif vars[i] == 'org_x':
                formatted_string = formatted_string.replace("{org_x}", input)
                token_object = create_token_object(input, 'X', 'I')
                tokens.append(token_object)
            elif vars[i] == 'org_y':
                formatted_string = formatted_string.replace("{org_y}", input)
                token_object = create_token_object(input, 'Y', 'I')
                tokens.append(token_object)
            elif vars[i] == 'oth_x':
                formatted_string = formatted_string.replace("{oth_x}", input)
                token_object = create_token_object(input, 'X', 'I')
                tokens.append(token_object)
            elif vars[i] == 'oth_y':
                formatted_string = formatted_string.replace("{oth_y}", input)
                token_object = create_token_object(input, 'Y', 'I')
                tokens.append(token_object)
                
        # Final formatted string
        p = re.sub(r'"', '', formatted_string)
        
		# Create json using p (prompt)
        new_json = prompt2json(p, tokens)
        new_json = json.dumps(new_json)
        # Write to json file
        write2json(new_json, json_path)

        print(f"Line {comb_number}: Written to JSON")
        
        # Write to txt file
        write2txt(p, txt_path)
        print(f"Line {comb_number}: Written to TXT")

# Extract placeholders
def extract_placeholders(template):
    pattern = re.compile(r'\{.*?\}')
    return pattern.findall(template)

# Reorder filtered data
def order_data(template, data):
    placeholders = extract_placeholders(template)
    # Reorder the list based on precomputed placeholder positions
    ordered_data = []
    for tag in placeholders:
        for item in data:
            if tag == item['tag']:
                ordered_data.append(item)
    return ordered_data

# Returns an array of all strings
def f2prompts(str_in, txt_path, json_path):
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
        {'key': 'pr_y', 'tag': """{pr_y}""", 'bool': False, 'data': protein_y_axis},
        {'key': 'com_x', 'tag': """{com_x}""", 'bool': False, 'data': common_x_axis},
        {'key': 'com_y', 'tag': """{com_y}""", 'bool': False, 'data': common_y_axis},
        {'key': 'org_x', 'tag': """{org_x}""", 'bool': False, 'data': organ_x_axis},
        {'key': 'org_y', 'tag': """{org_y}""", 'bool': False, 'data': organ_y_axis},
        {'key': 'oth_x', 'tag': """{oth_x}""", 'bool': False, 'data': other_x_axis},
        {'key': 'oth_y', 'tag': """{oth_y}""", 'bool': False, 'data': other_y_axis}
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

    # Define list
    w2d = [w['data'] for w in data]

    # Generate prompts based on empty tags version and write to json and txt files
    generate_files(w2d, str_in, vars, txt_path, json_path)

def prompt2json(str_in, tokens2tag):
    prompt_cleaned = str_in.strip()
    tokens = word_tokenize(prompt_cleaned)
    size = len(tokens)

    new_json = {
        "words": prompt_cleaned, 
        "tokens": word_tokenize(prompt_cleaned),
        "NER_TAG": ["O"] * size,
        "NER_ENCODING": [0] * size
    }

    for t in tokens2tag:
        # To do fix the duplicates thing - see line 3
        try:
            index = tokens.index(t["tokens"][0])
        except ValueError:
            continue
        str_len = len(t["tokens"])
        for i in range(str_len):
            new_json["NER_TAG"][index] = t["NER_TAG"][i]
            new_json["NER_ENCODING"][index] = t["NER_ENCODING"][i]
            index += 1
            
    return new_json

def write2files():
    with open('empty_tags/scatter_empty_tags.txt', 'r') as txt_in: 
        for i, line in enumerate(txt_in):
            txt_path = "prompts/scatter.txt"
            json_path = "json/scatter.json"
            f2prompts(line, txt_path, json_path)
            print(f"LINE {i + 1}: FILE WRITES COMPLETE \n")
            """
            with open(txt_out_file_path, 'w') as txt_out, open(json_out_file_path, 'w') as json_out:
                prompts, jsons = f2prompts(line)
                for prompt in prompts:
                    txt_out.write(prompt)
                print(f"Line {i + 1}: Write to txt complete")
                json.dump(jsons, json_out, indent=4)
                print(f"Line {i + 1}: Write to json complete")
            """
            
def write2txt(str_in, file_path):
    with open(file_path, 'a') as file:
        file.write(str_in)
    return

def write2json(json_obj, file_path):
    with open(file_path, 'r+') as file:
        # Move file pointer to the EOF
        file.seek(0, os.SEEK_END)
        # Move back to check if file ends with '[]' or '}, ]'
        file.seek(file.tell() - 2, os.SEEK_SET)

        # Read the last character
        last_char = file.read(1)
        
        if last_char == '[':
            # If the file is just an empty array, add the new data directly
            file.seek(file.tell() - 1, os.SEEK_SET)
            file.write(json_obj + ']')
        else:
            # Otherwise, insert the new data with a preceding comma
            file.seek(file.tell() - 1, os.SEEK_SET)
            file.write(',' + json_obj + ']')
    return

def main():
    write2files()
if __name__ == "__main__":
    main()
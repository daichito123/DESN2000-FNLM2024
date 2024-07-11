# Implemented batch writing
import os
import re
import json
import itertools
from multiprocessing import Pool, cpu_count
from nltk.tokenize import word_tokenize
from f_vars import (verb_create, verb_show, noun_relationship, scatterplot_name_var,
                    exp_lvl_plural, exp_lvl_singular, gene_x_axis, gene_y_axis,
                    protein_x_axis, protein_y_axis, common_x_axis, common_y_axis,
                    organ_x_axis, organ_y_axis, other_x_axis, other_y_axis)
from create_token_object import create_token_object

def generate_files(w2d, str_in, vars, txt_path, json_path, batch_size=1000):
    combinations = itertools.product(*w2d)
    txt_batch = []
    json_batch = []
    for comb_number, combo in enumerate(combinations):
        formatted_string, tokens = format_string(combo, vars, str_in)
        p = re.sub(r'"', '', formatted_string)
        new_json = prompt2json(p, tokens)
        new_json_str = json.dumps(new_json)
        
        txt_batch.append(p)
        json_batch.append(new_json_str)
        
        if len(txt_batch) >= batch_size:
            write_batches_to_files(txt_batch, json_batch, txt_path, json_path)
            txt_batch = []
            json_batch = []
        print(f"Line: {comb_number + 1}: Writes complete")
    
    # Write remaining items in batch
    if txt_batch:
        write_batches_to_files(txt_batch, json_batch, txt_path, json_path)

def write_batches_to_files(txt_batch, json_batch, txt_path, json_path):
    write2txt_batch(txt_batch, txt_path)
    write2json_batch(json_batch, json_path)

def write2txt_batch(str_list, file_path):
    with open(file_path, 'a', buffering=1) as file:
        for str_in in str_list:
            file.write(str_in + "\n")

def write2json_batch(json_list, file_path):
    with open(file_path, 'r+') as file:
        file.seek(0, os.SEEK_END)
        if file.tell() == 0:
            file.write('[' + ','.join(json_list) + ']')
        else:
            file.seek(file.tell() - 1, os.SEEK_SET)
            file.write(',' + ','.join(json_list) + ']')

def format_string(combo, vars, str_in):
    formatted_string = str_in
    tokens = []
    for i, input in enumerate(combo):
        tag_type = get_tag_type(vars[i])
        formatted_string = formatted_string.replace(f"{{{vars[i]}}}", input)
        token_object = create_token_object(input, *tag_type)
        tokens.append(token_object)
    return formatted_string, tokens

def get_tag_type(var):
    tag_map = {
        'vc': ('O', 'B'), 'vs': ('O', 'B'), 'nr': ('O', 'B'), 'els': ('O', 'B'),
        'elp': ('O', 'B'), 'snv': ('P', 'B'), 'g_x': ('X', 'B'), 'g_y': ('Y', 'B'),
        'pr_x': ('X', 'B'), 'pr_y': ('Y', 'B'), 'com_x': ('X', 'B'), 'com_y': ('Y', 'B'),
        'org_x': ('X', 'I'), 'org_y': ('Y', 'I'), 'oth_x': ('X', 'I'), 'oth_y': ('Y', 'I')
    }
    return tag_map[var]

def extract_placeholders(template):
    pattern = re.compile(r'\{.*?\}')
    return pattern.findall(template)

def order_data(template, data):
    placeholders = extract_placeholders(template)
    ordered_data = [item for tag in placeholders for item in data if tag == item['tag']]
    return ordered_data

def f2prompts_wrapper(line, txt_path, json_path):
    f2prompts(line, txt_path, json_path)

def f2prompts(str_in, txt_path, json_path):
    data = [
        {'key': 'vc', 'tag': "{vc}", 'data': verb_create},
        {'key': 'vs', 'tag': "{vs}", 'data': verb_show},
        {'key': 'nr', 'tag': "{nr}", 'data': noun_relationship},
        {'key': 'snv', 'tag': "{snv}", 'data': scatterplot_name_var},
        {'key': 'els', 'tag': "{els}", 'data': exp_lvl_singular},
        {'key': 'elp', 'tag': "{elp}", 'data': exp_lvl_plural},
        {'key': 'g_x', 'tag': "{g_x}", 'data': gene_x_axis},
        {'key': 'g_y', 'tag': "{g_y}", 'data': gene_y_axis},
        {'key': 'pr_x', 'tag': "{pr_x}", 'data': protein_x_axis},
        {'key': 'pr_y', 'tag': "{pr_y}", 'data': protein_y_axis},
        {'key': 'com_x', 'tag': "{com_x}", 'data': common_x_axis},
        {'key': 'com_y', 'tag': "{com_y}", 'data': common_y_axis},
        {'key': 'org_x', 'tag': "{org_x}", 'data': organ_x_axis},
        {'key': 'org_y', 'tag': "{org_y}", 'data': organ_y_axis},
        {'key': 'oth_x', 'tag': "{oth_x}", 'data': other_x_axis},
        {'key': 'oth_y', 'tag': "{oth_y}", 'data': other_y_axis}
    ]

    vars = re.findall(r'{(.*?)}', str_in)
    filtered = [item for item in data if item['key'] in vars]
    data = order_data(str_in, filtered)
    w2d = [w['data'] for w in data]
    generate_files(w2d, str_in, vars, txt_path, json_path)

def prompt2json(str_in, tokens2tag):
    prompt_cleaned = str_in.strip()
    tokens = word_tokenize(prompt_cleaned)
    size = len(tokens)
    new_json = {
        "words": prompt_cleaned,
        "tokens": tokens,
        "NER_TAG": ["O"] * size,
        "NER_ENCODING": [0] * size
    }

    for t in tokens2tag:
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
        lines = txt_in.readlines()

    num_workers = cpu_count()
    pool = Pool(num_workers)
    txt_path = "prompts/scatter.txt"
    json_path = "json/scatterV2.json"

    pool.starmap(f2prompts_wrapper, [(line.strip(), txt_path, json_path) for line in lines])
    pool.close()
    pool.join()

def main():
    write2files()

if __name__ == "__main__":
    main()
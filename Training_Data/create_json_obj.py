import json
from nltk.tokenize import word_tokenize

from tags import scatter

data = []

# To do - implement ability to input different title_prompts.txt files

with open('scatter_prompts.txt', 'r') as f_in:
    for i, prompt in enumerate(f_in):
        prompt_cleaned = prompt.strip()
        new_data = {
            "words": prompt_cleaned, 
            "tokens": word_tokenize(prompt_cleaned),
            "NER_TAG": [],
            "NER_ENCODING": []
        }
        # Fix common words error
        tags = scatter[i]["Tokens to tag"]
        for word in new_data["tokens"]:
            found = False
            for t in tags:
                if word in t["tokens"]:
                    index = t["tokens"].index(word)
                    new_data["NER_TAG"].append(t["NER_TAG"][index])
                    new_data["NER_ENCODING"].append(t["NER_ENCODING"][index])
                    found = True
                    break
            if not found:
                new_data["NER_TAG"].append("O")
                new_data["NER_ENCODING"].append(0)
        data.append(new_data)

with open('scatter_data.json', 'w') as f_out:
    json.dump(data, f_out, indent=4)
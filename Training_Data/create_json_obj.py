import json
from nltk.tokenize import word_tokenize

from tags import scatter, bar

chart_types = [
    {
        "key": "scatter",
        "tags": scatter
    },
    {
        "key": "bar",
        "tags": bar
    }
]

for chart in chart_types:
    
    data = []

    input_file = f"prompts/{chart["key"]}_prompts.txt"
    output_file = f"data/{chart["key"]}_data.json"

    with open(input_file, 'r') as f_in:
        for i, prompt in enumerate(f_in):

            prompt_cleaned = prompt.strip()
            tokens = word_tokenize(prompt_cleaned)
            size = len(tokens)

            new_data = {
                "words": prompt_cleaned, 
                "tokens": tokens,
                "NER_TAG": ["O"] * size,
                "NER_ENCODING": [0] * size
            }
            
            tags = chart["tags"][i]["Tokens to tag"]

            for t in tags:
                try: 
                    # Gets the corresponding index for new_data["tokens"]
                    index = tokens.index(t["tokens"][0])
                    for i in range(len(t["tokens"])):
                        new_data["NER_TAG"][index] = t["NER_TAG"][i]
                        new_data["NER_ENCODING"][index] = t["NER_ENCODING"][i]
                        index += 1
                except ValueError:
                    continue
            
            data.append(new_data)

    with open(output_file, 'w') as f_out:
        json.dump(data, f_out, indent=4)
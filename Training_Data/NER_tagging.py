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
            #
            print("new prompt")

            prompt_cleaned = prompt.strip()
            tokens = word_tokenize(prompt_cleaned)
            size = len(tokens)

            new_data = {
                "words": prompt_cleaned, 
                "tokens": word_tokenize(prompt_cleaned),
                "NER_TAG": ["O"] * size,
                "NER_ENCODING": [0] * size
            }
            
            tags = chart["tags"][i]["Tokens to tag"]

            for t in tags:
                try: 
                    # Gets the corresponding index for new_data["tokens"]
                    index = tokens.index(t["tokens"][0])
                except ValueError:
                    continue
                
                # print(t["tokens"][0])

                offset = 0

                str_len = len(t["tokens"])
                for i in range(str_len):
                    new_data["NER_TAG"][index + offset] = t["NER_TAG"][i]
                    new_data["NER_ENCODING"][index + offset] = t["NER_ENCODING"][i]
                    print(tokens)
                    tokens.pop(t["tokens"][i])
                    print(tokens)
                    index += 1

            data.append(new_data)

            #
            print('\n')

    with open(output_file, 'w') as f_out:
        json.dump(data, f_out, indent=4)
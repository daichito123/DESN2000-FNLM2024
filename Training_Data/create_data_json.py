import json
from nltk.tokenize import word_tokenize
from dicts import plot_vars, x_vars, y_vars

def create_list(dict):
	new_list = [token for element in dict for token in element["tokens"]]
	return new_list

def main():
	plot_labs = create_list(plot_vars)
	x_labs = create_list(x_vars)
	y_labs = create_list(y_vars)

	data = []

	with open('prompts_processed.txt', 'r') as f_in:
		for prompt in f_in:
			words = word_tokenize(prompt.strip())
			new_obj = {
				"words": prompt.strip(),
				"tokens": words,
				"NER_TAG": [],
				"NER_ENCODING": []
			}

			for word in words:
				found = False
				if word in plot_labs:
					for p in plot_vars:
						if word in p["tokens"]:
							index = p["tokens"].index(word)
							new_obj["NER_TAG"].append(p["NER_TAG"][index])
							new_obj["NER_ENCODING"].append(p["NER_ENCODING"][index])
							found = True
							break
				elif word in x_labs:
					for x in x_vars:
						if word in x["tokens"]:
							index = x["tokens"].index(word)
							new_obj["NER_TAG"].append(x["NER_TAG"][index])
							new_obj["NER_ENCODING"].append(x["NER_ENCODING"][index])
							found = True
							break
				elif word in y_labs:
					for y in y_vars:
						if word in y["tokens"]:
							index = y["tokens"].index(word)
							new_obj["NER_TAG"].append(y["NER_TAG"][index])
							new_obj["NER_ENCODING"].append(y["NER_ENCODING"][index])
							found = True
							break
				if not found:
					new_obj["NER_TAG"].append("O")
					new_obj["NER_ENCODING"].append(0)

			data.append(new_obj)
	
	with open('data.json', 'w') as f_out:
		json.dump(data, f_out, indent=4)

if __name__ == "__main__":
    main()
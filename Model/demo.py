import torch
from transformers import BertTokenizerFast, BertForTokenClassification
import re

model_name = 'GraphBot/model-pt'

text = "Plot KCNE4 vs ORTAP12. Use a scatterplot"

print("Load Model...")
model = BertForTokenClassification.from_pretrained(model_name)
print("Model loaded!")

print("Load Tokenizer...")
tokenizer = BertTokenizerFast.from_pretrained(model_name)
print("Tokenier loaded! \n")

# Tokenize the input text
print(f"Input query: {text}\n")

inputs = tokenizer(text, return_tensors="pt")
tokens = tokenizer.convert_ids_to_tokens(inputs['input_ids'][0])

print(f"Tokenized query: {tokens}\n")
print(f"Numerical representation of tokenized query (Model input): {inputs['input_ids'][0]}\n")


# Get model predictions
outputs = model(**inputs)
logits = outputs.logits

# Convert logits to predicted labels
predictions = torch.argmax(logits, dim=-1)
print(f"Model output: {predictions[0]}\n")

# Map the predicted labels to entity names
label_map = {0: "O", 1: "B-PLOT_TYPE", 2: "I-PLOT_TYPE", 3: "B-X_AXIS_LABEL", 4: "I-X_AXIS_LABEL", 5: "B-Y_AXIS_LABEL", 6: "I-Y_AXIS_LABEL"}
predicted_labels = [label_map[label.item()] for label in predictions[0]]

print(f"Model output - mapped to labels: {predicted_labels}\n")

print("Postprocessing...")
# Remove items with 'O' Tag
filtered_results = [(token, label) for token, label in zip(tokens, predicted_labels) if label != 'O']

# Remove B and O tags
filtered_results = [(token, label.replace('B-', '').replace('I-', '')) for token, label in filtered_results]

# Group by NER_TAG
data = {}
for token, label in filtered_results:
    if label not in data:
        data[label] = ''
    if '#' in token:
        data[label] = (data[label] + token).replace('#', '')
    else:
        data[label] = data[label] + token

print(f"JSON Object: {data}\n")

print("Standerdizing JSON object...")
# Standardize plot type
if re.search(r'scatter', data['PLOT_TYPE'].lower()):
    data['PLOT_TYPE'] = 'scatter'

# Capitalize everything
for key, value in data.items():
    data[key] = re.sub(r'[(){}\[\]<>]', '', value)

print(f"Final JSON Object: {data}\n")
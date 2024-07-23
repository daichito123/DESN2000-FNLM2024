import tensorflow as tf
from transformers import BertTokenizerFast, TFBertForTokenClassification
import re
import json

model_name = 'ditto123/FNLM-DESN200-tf'

# Load the trained model and tokenizer
print("Loading model...")
model = TFBertForTokenClassification.from_pretrained(model_name)
print("Model loaded\n")

print("Loading tokenizer...")
tokenizer = BertTokenizerFast.from_pretrained(model_name)
print("Tokenizer loaded\n")

text = "Compare gene expression levels of KRTAP12 (Heart) and LCE3D-1 in the liver using a scatterplot"

# Tokenize the input text
inputs = tokenizer(text, return_tensors="tf")
tokens = tokenizer.convert_ids_to_tokens(inputs['input_ids'][0].numpy())

# Get model predictions
outputs = model(inputs)
logits = outputs.logits                                                                                                                                            

# Convert logits to predicted labels
predictions = tf.argmax(logits, axis=-1)

print(predictions)

# Map the predicted labels to entity names
label_map = {0: "O", 1: "B-PLOT_TYPE", 2: "I-PLOT_TYPE", 3: "B-X_AXIS_LABEL", 4: "I-X_AXIS_LABEL", 5: "B-Y_AXIS_LABEL", 6: "I-Y_AXIS_LABEL"}
predicted_labels = [label_map[label.numpy()] for label in predictions[0]]
print("Process complete\n")

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

# Standardize plot label
if re.search(r'scatter', data['PLOT_TYPE'].lower()):
    data['PLOT_TYPE'] = 'SCATTER'

# Capitalize everything
for key, value in data.items():
    data[key] = value.upper()

print("Postprocessing complete\n")


print(f"JSON output: {data}")
with open("output.json", 'w') as json_file:
    json.dump(data, json_file, indent=4)
print("Output written to JSON")
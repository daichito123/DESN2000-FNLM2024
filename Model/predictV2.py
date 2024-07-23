from transformers import pipeline, BertTokenizerFast, BertForTokenClassification

model_name = 'ditto123/FNLM-DESN200'

text = "Compare gene expression levels of KRTAP12 (Heart) and LCE3D-1 in the liver using a scatterplot"
model = BertForTokenClassification.from_pretrained(model_name)
tokenizer = BertTokenizerFast.from_pretrained(model_name)

pipe = pipeline('ner', model=model, tokenizer=tokenizer)
results = pipe(text)
print(results)
for dict in results:
    print(f"{dict['entity']}: {dict['word']}")
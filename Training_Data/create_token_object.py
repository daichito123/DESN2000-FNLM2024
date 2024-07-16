import nltk
from nltk.tokenize import word_tokenize

NER_TAGS = [
    'O',
    'B-PLOT_TYPE',
    'I-PLOT_TYPE',
    'B-X_AXIS_LABEL',
    'I-X_AXIS_LABEL',
    'B-Y_AXIS_LABEL',
    'I-Y_AXIS_LABEL'
]

NER_ENCODING = {
  'O': 0,
  'B-PLOT_TYPE': 1,
  'I-PLOT_TYPE': 2,
  'B-X_AXIS_LABEL': 3,
  'I-X_AXIS_LABEL': 4,
  'B-Y_AXIS_LABEL': 5,
  'I-Y_AXIS_LABEL': 6
}

def modify_NER_content(object, tag_type, index, IOB):

    if tag_type == 'O':
        tag = 'O'
    
    if index == 0 and IOB == 'B':
        if tag_type == 'P':
            tag = 'B-PLOT_TYPE'
        elif tag_type == 'X':
            tag = 'B-X_AXIS_LABEL'
        elif tag_type == 'Y':
            tag = 'B-Y_AXIS_LABEL'
    else:
        if tag_type == 'P':
            tag = 'I-PLOT_TYPE'
        elif tag_type == 'X':
            tag = 'I-X_AXIS_LABEL'
        elif tag_type == 'Y':
            tag = 'I-Y_AXIS_LABEL'

    object['NER_TAG'].append(tag)
    object['NER_ENCODING'].append(NER_ENCODING[tag])

    return object

def create_token_object(input, tag_type, IOB):
    # tag_type must be either: O, P, X or Y
    tokens = word_tokenize(input)
    token_object = {
        "words": input,
        "tokens": tokens,
        "NER_TAG": [],
        "NER_ENCODING": []
    }
    if len(tokens) == 1:
        token_object = modify_NER_content(token_object, tag_type, 0, IOB)
    else:
        for i in range(len(tokens)):
            token_object = modify_NER_content(token_object, tag_type, i, IOB)

    return token_object
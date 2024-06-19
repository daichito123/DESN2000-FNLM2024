plot_vars = [
    {
        "words": "Scatterplot",
        "tokens": ["Scatterplot"],
        "NER_TAG": ["B-Plot"],
        "NER_ENCODING": [1] 
    },
    {
        "words": "Bar graph",
        "tokens": ["Bar", "graph"],
        "NER_TAG": ["B-Plot", "I-Plot"],
        "NER_ENCODING": [1, 2] 
    } 
]

x_vars = [
    {
        "words": "Apples",
        "tokens": ["Apples"],
        "NER_TAG": ["B-X_ax"],
        "NER_ENCODING": [3]
    },
    {
        "words": "X",
        "tokens": ["X"],
        "NER_TAG": ["B-X_ax"],
        "NER_ENCODING": [3]
    },
    {
        "words": "Alpha",
        "tokens": ["Alpha"],
        "NER_TAG": ["B-X_ax"],
        "NER_ENCODING": [3]
    },
    {
        "words": "OpenAI users",
        "tokens": ["OpenAI", "users"],
        "NER_TAG": ["B-X_ax", "I-X_ax"],
        "NER_ENCODING": [3, 4]
    }
]

y_vars = [
    {
        "words": "Oranges",
        "tokens": ["Oranges"],
        "NER_TAG": ["B-Y_ax"],
        "NER_ENCODING": [5]
    },
    {
        "words": "Y",
        "tokens": ["Y"],
        "NER_TAG": ["B-Y_ax"],
        "NER_ENCODING": [5]
    },
    {
        "words": "Beta",
        "tokens": ["Beta"],
        "NER_TAG": ["B-Y_ax"],
        "NER_ENCODING": [5]
    },
    {
        "words": "Google users",
        "tokens": ["Google", "users"],
        "NER_TAG": ["B-Y_ax", "I-Y_ax"],
        "NER_ENCODING": [5, 6]
    },
]
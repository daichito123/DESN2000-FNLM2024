scatter = [
    {
        "Line No.": 1,
        "Tokens to tag": [
            {
                "words": "scatterplot",
                "tokens": ["scatterplot"],
                "NER_TAG": ["B-PLOT_TYPE"],
                "NER_ENCODING": [1]
            }, 
            {
                "words": "GC content",
                "tokens": ["GC", "content"],
                "NER_TAG": ["B-X_AXIS_LABEL", "I-X_AXIS_LABEL"],
                "NER_ENCODING": [3, 4]
            }, 
            {
                "words": "Melting temperature",
                "tokens": ["Melting", "temperature"],
                "NER_TAG": ["B-Y_AXIS_LABEL", "I-Y_AXIS_LABEL"],
                "NER_ENCODING": [5, 6]
            }
        ]
    }, 
    {
        "Line No.": 2,
        "Tokens to tag": [
            {
                "words": "Scatter",
                "tokens": ["Scatter"],
                "NER_TAG": ["B-PLOT_TYPE"],
                "NER_ENCODING": [1]
            }, 
            {
                "words": "TP53",
                "tokens": ["TP53"],
                "NER_TAG": ["B-X_AXIS_LABEL"],
                "NER_ENCODING": [3]
            }, 
            {
                "words": "MDM2",
                "tokens": ["MDM2"],
                "NER_TAG": ["B-Y_AXIS_LABEL"],
                "NER_ENCODING": [5]
            }
        ]
    }, 
    {
        "Line No.": 3,
        "Tokens to tag": [
            {
                "words": "scatter chart",
                "tokens": ["scatter", "chart"],
                "NER_TAG": ["B-PLOT_TYPE", "I-PLOT_TYPE"],
                "NER_ENCODING": [1, 2]
            }, 
            {
                "words": "expression of RNU4-31P",
                "tokens": ["expression", "of", "RNU4-31P"],
                "NER_TAG": ["B-X_AXIS_LABEL", "I-X_AXIS_LABEL", "I-X_AXIS_LABEL"],
                "NER_ENCODING": [3, 4, 4]
            }, 
            {
                "words": "p-value of a SNP",
                "tokens": ["p-value", "of", "a", "SNP"],
                "NER_TAG": ["B-Y_AXIS_LABEL", "I-Y_AXIS_LABEL", "I-Y_AXIS_LABEL", "I-Y_AXIS_LABEL"],
                "NER_ENCODING": [5, 6, 6, 6]
            }
        ]
    },
    {
        "Line No.": 4,
        "Tokens to tag": [
            {
                "words": "TP53 in healthy samples",
                "tokens": ["TP53", "in", "healthy", "samples"],
                "NER_TAG": ["B-X_AXIS_LABEL", "I-X_AXIS_LABEL", "I-X_AXIS_LABEL", "I-X_AXIS_LABEL"],
                "NER_ENCODING": [3, 4, 4, 4]
            }, 
            {
                "words": "TP53 in cancerous samples",
                "tokens": ["TP53", "in", "cancerous", "samples"],
                "NER_TAG": ["B-Y_AXIS_LABEL", "I-Y_AXIS_LABEL", "I-Y_AXIS_LABEL", "I-Y_AXIS_LABEL"],
                "NER_ENCODING": [5, 6, 6, 6]
            }, 
            {
                "words": "scatter graph",
                "tokens": ["scatter", "graph"],
                "NER_TAG": ["B-PLOT_TYPE", "I-PLOT_TYPE"],
                "NER_ENCODING": [1, 2]
            }
        ]
    }
]

bar = [
    {
        "Line No.": 1,
        "Tokens to tag": [
            {
                "words": "bar chart",
                "tokens": ["bar", "chart"],
                "NER_TAG": ["B-PLOT_TYPE", "I-PLOT_TYPE"],
                "NER_ENCODING": [1, 2]
            }, 
            {
                "words": "GC content",
                "tokens": ["GC", "content"],
                "NER_TAG": ["B-Y_AXIS_LABEL", "I-Y_AXIS_LABEL"],
                "NER_ENCODING": [5, 6]
            }, 
            {
                "words": "BRCA1",
                "tokens": ["BRCA1"],
                "NER_TAG": ["B-X_AXIS_LABEL"],
                "NER_ENCODING": [3]
            }, 
            {
                "words": "MTHFR",
                "tokens": ["MTHFR"],
                "NER_TAG": ["B-X_AXIS_LABEL"],
                "NER_ENCODING": [3]
            }
        ]
    },
    {
        "Line No.": 2,
        "Tokens to tag": [
            {
                "words": "bar graph",
                "tokens": ["bar", "graph"],
                "NER_TAG": ["B-PLOT_TYPE", "I-PLOT_TYPE"],
                "NER_ENCODING": [1, 2]
            }, 
            {
                "words": "number of genes associated",
                "tokens": ["number", "of", "genes"],
                "NER_TAG": ["B-Y_AXIS_LABEL", "I-Y_AXIS_LABEL", "I-Y_AXIS_LABEL"],
                "NER_ENCODING": [5, 6, 6, 6]
            }, 
            {
                "words": "AMPK signaling pathway",
                "tokens": ["AMPK", "signaling", "pathway"],
                "NER_TAG": ["B-X_AXIS_LABEL", "I-X_AXIS_LABEL", "I-X_AXIS_LABEL"],
                "NER_ENCODING": [3, 4, 4]
            },
            {
                "words": "Glycolysis",
                "tokens": ["Glycolysis"],
                "NER_TAG": ["B-X_AXIS_LABEL"],
                "NER_ENCODING": [3]
            }
        ]
    }
]
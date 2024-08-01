import pandas as pd

def select_entities(file_path, num, state, col_name):
    df = pd.read_csv(file_path)
    entities = df[col_name].dropna().sample(n=num, random_state=state)
    entities = entities.tolist()
    return entities

def main():
    protein_path = 'csv/proteins.csv'
    proteins = select_entities(protein_path, 100, 1, 'HGNC Symbol')

    gene_path = 'csv/genes.csv'
    genes = select_entities(gene_path, 100, 1, 'Approved symbol')

    organ_path = 'csv/human_organs.csv'
    organs = select_entities(organ_path, 5, 4, 'Organ')
    
    p_o = [f'{p} ({o})' for p in proteins for o in organs]

    g_o = [f'{g} ({o})' for g in genes for o in organs]

    n_samples = 200

    array = [0] * n_samples

    sample = [f'Sample {i + 1}' for i in range(n_samples)]

    protein_data = {'Sample': sample}
    gene_data = {'Sample': sample}

    for po in p_o:
        protein_data.update({po: array})
    
    for go in g_o:
        gene_data.update({go: array})

    df_p = pd.DataFrame(protein_data)
    df_g = pd.DataFrame(gene_data)

    df_p.to_csv('protein-raw.csv', index=False)
    df_g.to_csv('gene-raw.csv', index=False)

if __name__ == "__main__":
    main()
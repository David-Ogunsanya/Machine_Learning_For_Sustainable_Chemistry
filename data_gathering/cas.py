from pypdf import PdfReader
import re
import cirpy
import pandas as pd

def Extracting_cas_numbers():
    with open('cas_number.pdf', 'rb') as f:
        reader = PdfReader(f)
        cas = []

        for j in range(1, 18):
            pg = reader.pages[j]

            txt = pg.extract_text()

            s = re.findall(r"\[(.*\d)\]", txt)

            cas.extend([x.replace(" ", "")for x in s])
    return cas


def Smiles_string():
    cas = Extracting_cas_numbers() 
    num = []
    Smi = []
    name = []

    for number, cas_number in enumerate(cas):
        smiles = cirpy.resolve(cas_number, 'Smiles')
        name = cirpy.resolve(cas_number, 'name')
        Smi.append(smiles)
        num.append(number + 1)

    df = pd.DataFrame("\n\n Number Smiles Casnumber", num, Smi, cas)
    df.to_csv('initial_solvent_data.csv')


Smiles_string()

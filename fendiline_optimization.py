!pip install rdkit
!pip install pubchempy
from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem import Descriptors
my_molecule_smiles = "C1=CC=C(C=C1)C=CCNCC2=CC=C(C=C2)F"
     

fendiline_smiles = "CC(C1=CC=CC=C1)NCCC(C2=CC=CC=C2)C3=CC=CC=C3"
     

mol_mine = Chem.MolFromSmiles(my_molecule_smiles)
mol_fendiline = Chem.MolFromSmiles(fendiline_smiles)
     

print("Comparing Your Derivative vs. Fendiline")
Draw.MolsToGridImage([mol_mine, mol_fendiline], molsPerRow=2, subImgSize=(300, 300), legends=["Your Derivative (Failed)", "Fendiline (Active)"])
     import pandas as pd

def get_properties(mol, label):
    return {
        "Name": label,
        "MW (Weight)": Descriptors.MolWt(mol),
        "LogP (Lipophilicity)": Descriptors.MolLogP(mol),
        "H-Donors": Descriptors.NumHDonors(mol),
        "H-Acceptors": Descriptors.NumHAcceptors(mol),
        "TPSA (Polar Surface Area)": Descriptors.TPSA(mol)
    }
     

props_mine = get_properties(mol_mine, "Your Derivative")
props_fendiline = get_properties(mol_fendiline, "Fendiline")
     

df = pd.DataFrame([props_mine, props_fendiline])
print(df)
print("\n--- COMPUTATIONAL DIAGNOSIS ---")
logp = props_mine["LogP (Lipophilicity)"]
if logp > 3.5:
    print(f"DIAGNOSIS: Your derivative has a high LogP ({logp}).")
    print("ANALYSIS: This confirms your thesis hypothesis. The molecule is too lipophilic, leading to poor solubility in the MTT assay media.")
else:
    print(f"LogP is {logp}. While acceptable, we can improve solubility by adding polar groups.")
print("\n--- ANALYSIS ---")
if props_mine["LogP (Lipophilicity)"] > 3.0:
    print(f"CONFIRMED: Your derivative has a high LogP ({props_mine['LogP (Lipophilicity)']}).")
    print("This supports your thesis conclusion: 'Poor water solubility... and vulnerability to metabolic oxidation'.")
# We will keep the 'Cinnamyl' backbone but change the 'Tail' to make it more soluble

# Idea 1: Add a Hydroxyl group (Increases polarity)
idea_1_smiles = "C1=CC=C(C=C1)/C=C/CNCC2=CC=C(C=C2)O"
# Idea 2: Add a Methoxy group (Metabolic stability)
idea_2_smiles = "C1=CC=C(C=C1)/C=C/CNCC2=CC=C(C=C2)OC"
# Idea 3: Add Morpholine (Standard medicinal chemistry trick for solubility)
idea_3_smiles = "C1=CC=C(C=C1)/C=C/CNCC2=CC=C(C=C2)N3CCOCC3"

# List of new ideas
ideas = [Chem.MolFromSmiles(s) for s in [idea_1_smiles, idea_2_smiles, idea_3_smiles]]
labels = ["Idea 1 (Hydroxyl)", "Idea 2 (Methoxy)", "Idea 3 (Morpholine)"]

# Visualize the new candidates
print("--- NEW CANDIDATES DESIGNED BY SARONA ---")
img_ideas = Draw.MolsToGridImage(ideas, molsPerRow=3, subImgSize=(250, 250), legends=labels)
display(img_ideas)

# Calculate their properties to prove they are better
idea_props = [get_properties(m, l) for m, l in zip(ideas, labels)]
df_ideas = pd.DataFrame(idea_props)
print("\n--- PREDICTED PROPERTIES OF NEW CANDIDATES ---")
display(df_ideas)

# Recommendation
best_logp = df_ideas["LogP (Lipophilicity)"].min()
best_candidate = df_ideas.loc[df_ideas["LogP (Lipophilicity)"] == best_logp, "Name"].values[0]
print(f"\nRECOMMENDATION: The {best_candidate} derivative has the lowest LogP ({best_logp}).")
print("This molecule should have better water solubility than your original thesis compound.")
     

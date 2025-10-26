from rdkit import DataStructs
from rdkit.Chem import AllChem
import numpy as np

def morgan_fp(mol):
  morgan = AllChem.GetMorganGenerator(radius=2, fpSize=512)
  return morgan.GetFingerprint(mol)

def bitvect_to_array(bitvect):
  arr = np.zeros((1,), dtype=int)
  DataStructs.ConvertToNumpyArray(bitvect, arr)
  return arr


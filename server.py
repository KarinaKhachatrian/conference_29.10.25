import joblib
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from rdkit.Chem import MolFromSmiles
import numpy as np
from morgan_fingerprints import morgan_fp, bitvect_to_array


app = FastAPI()
model = joblib.load("./model/model.joblib")

class SolubilityPrediction(BaseModel):
    temperature_k: float
    smiles_solute: str
    smiles_solvent: str

@app.get("/")
def root():
    return {"message": "ok"}

@app.post('/predict')
def predict(solubility_prediction: SolubilityPrediction):
    mol_solute = MolFromSmiles(solubility_prediction.smiles_solute)
    mol_solvent = MolFromSmiles(solubility_prediction.smiles_solvent)

    fp_solute_bv = morgan_fp(mol_solute)
    fp_solvent_bv = morgan_fp(mol_solvent)

    fp_solute_arr = bitvect_to_array(fp_solute_bv)
    fp_solvent_arr = bitvect_to_array(fp_solvent_bv)

    features = np.concatenate([
        [solubility_prediction.temperature_k],
        fp_solute_arr,
        fp_solvent_arr
    ]).reshape(1, -1)

    prediction = model.predict(features).tolist()[0]
    return {
        "prediction": prediction
    }

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=80)
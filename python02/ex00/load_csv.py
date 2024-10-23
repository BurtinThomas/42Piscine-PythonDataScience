import pandas
import os

def load(path: str):
    try:
        if not isinstance(path, str):
            raise TypeError("Le chemin doit être une chaîne de caractères")
        if not path.lower().endswith((".csv")):
            raise AssertionError("put only csv file")
        if not os.path.exists(path):
            raise FileNotFoundError(f"Le fichier {path} n'existe pas.")
        dataset = pandas.read_csv(path)
        print(f"Loading dataset of dimensions {dataset.shape}")
        return dataset
    except Exception as error:
        print(f"{Exception.__name__} : {error}") 
        return None
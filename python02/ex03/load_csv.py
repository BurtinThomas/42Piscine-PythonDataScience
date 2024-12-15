import pandas


def load(path: str):
    """
    Charge un fichier CSV dans un DataFrame Pandas.
    Args:
        path (str): Le chemin du fichier CSV à charger.
    Returns:
        pandas.DataFrame: Le DataFrame contenant les données du fichier CSV
        si le chargement réussit.
        None: Si une erreur se produit lors du chargement.
    """
    try:
        df = pandas.read_csv(path)
        print(f"Loading dataset of dimensions {df.shape}")
        return df
    except Exception as error:
        print(f"{Exception.__name__} : {error}")
        return None

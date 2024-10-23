from PIL import Image 
import numpy as np
import os

def ft_load(path: str) -> np.ndarray:
    try:
        if not isinstance(path, str):
            raise TypeError("Le chemin doit être une chaîne de caractères")
        if not path.lower().endswith((".jpg", ".jpeg")):
            raise AssertionError("put only jpg or jpeg")
        if not os.path.exists(path):
            raise FileNotFoundError(f"Le fichier {path} n'existe pas.")
        image = Image.open(path)
        image_array = np.array(image)
        print(f"The shape of image is: {image_array.shape}")
        return image_array
    
    except Exception as error:
        print(f"{type(error).__name__} : {error}")


from fastapi import FastAPI
from typing import List
from fuzzywuzzy import process
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats 
import ast
import json
from collections import Counter

app = FastAPI()

# Cargar el DataFrame con los datos
df = pd.read_csv('Dataset/movies_cleaned.csv')

@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API de películas"}

@app.get("/peliculas_idioma/")
def peliculas_idioma(Idioma: str):
    # Contar la cantidad de películas en el idioma especificado
    count = df['spoken_languages'].str.contains(Idioma, case=False, na=False).sum()
    
    return {"message": f"{count} cantidad de películas fueron estrenadas en idioma {Idioma}"}











"""# Función 1: Películas por idioma
@app.get("/peliculas_idioma")
def peliculas_idioma(Idioma: str):
    # Aquí implementa la lógica para contar películas por idioma y devuelve la respuesta adecuada
    return f"{X} cantidad de películas fueron estrenadas en idioma {Idioma}"

# Función 2: Duración y año de una película
@app.get("/peliculas_duracion")
def peliculas_duracion(Pelicula: str):
    # Aquí implementa la lógica para obtener duración y año de una película y devuelve la respuesta adecuada
    return f"Duración: {X} minutos. Año: {YYYY}"

# Función 3: Información de una franquicia
@app.get("/franquicia")
def franquicia(Franquicia: str):
    # Aquí implementa la lógica para obtener información de una franquicia y devuelve la respuesta adecuada
    return f"La franquicia {Franquicia} posee {X} películas, una ganancia total de {X} y una ganancia promedio de {XX}"

# Función 4: Películas por país
@app.get("/peliculas_pais")
def peliculas_pais(Pais: str):
    # Aquí implementa la lógica para contar películas por país y devuelve la respuesta adecuada
    return f"Se produjeron {X} películas en el país {Pais}"

# Función 5: Información de una productora
@app.get("/productoras_exitosas")
def productoras_exitosas(Productora: str):
    # Aquí implementa la lógica para obtener información de una productora y devuelve la respuesta adecuada
    return f"La productora {Productora} ha tenido un revenue de {X}"

# Función 6: Información de un director
@app.get("/get_director")
def get_director(nombre_director: str):
    # Aquí implementa la lógica para obtener información de un director y devuelve la respuesta adecuada
    return [{"pelicula": "Nombre Película", "fecha_lanzamiento": "YYYY-MM-DD", "retorno": X, "costo": X, "ganancia": X}, ...]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)"""

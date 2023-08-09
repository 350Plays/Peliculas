from fastapi import FastAPI
from typing import List
from fuzzywuzzy import process
import pandas as pd
from collections import Counter
import uvicorn

app = FastAPI(debug=True)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

# Cargar el DataFrame de películas
df = pd.read_csv('Dataset/movies_cleaned.csv')

# Cargar el DataFrame de créditos
credits_df = pd.read_csv('Dataset/credits_cleaned.csv')

# Convertir los valores de la columna 'id' a strings
df['id'] = df['id'].astype(str)
credits_df['id'] = credits_df['id'].astype(str)

@app.get('/')
def read_root():
    return {"message": "Bienvenido a la API de recomendación de películas"}

@app.get('/peliculas_idioma/')
def peliculas_idioma(Idioma: str):
    idioma_lower = Idioma.lower()
    idiomas = df['spoken_languages'].str.lower().unique()
    
    closest_exact_match = None
    closest_matches = []
    
    for idioma in idiomas:
        if idioma_lower == idioma:
            closest_exact_match = idioma
            break
        else:
            closest_matches.append(idioma)
    
    if closest_exact_match:
        count = df['spoken_languages'].str.lower().str.contains(closest_exact_match, case=False, na=False).sum()
        return {"resultado": f"{count} cantidad de películas fueron estrenadas en idioma {Idioma}"}
    elif closest_matches:
        results = []
        for closest_idioma in closest_matches[:3]:
            count = df['spoken_languages'].str.lower().str.contains(closest_idioma, case=False, na=False).sum()
            results.append({
                "idioma": closest_idioma,
                "cantidad_peliculas": count
            })
        
        resultados_text = "\n".join([
            f"{r['idioma']} - Cantidad de películas: {r['cantidad_peliculas']}"
            for r in reversed(results)
        ])
        return {"resultados": resultados_text}
    else:
        return {"resultado": f"No se encontraron resultados para el idioma {Idioma}"}

@app.get('/peliculas_duracion/')
def peliculas_duracion(Pelicula: str):
    pelicula_lower = Pelicula.lower()
    peliculas = df['title'].str.lower().unique()
    
    closest_exact_match = None
    closest_matches = []
    
    for pelicula in peliculas:
        if pelicula_lower == pelicula:
            closest_exact_match = pelicula
            break
        else:
            closest_matches.append(pelicula)
    
    if closest_exact_match:
        pelicula_info = df[df['title'].str.lower() == closest_exact_match]
        duracion = int(pelicula_info['runtime'].values[0])
        año = int(pelicula_info['release_year'].values[0])
        return {"resultado": f"{Pelicula}. Duración: {duracion} minutos. Año: {año}"}
    elif closest_matches:
        results = []
        for closest_pelicula in closest_matches[:3]:
            pelicula_info = df[df['title'].str.lower() == closest_pelicula]
            duracion = int(pelicula_info['runtime'].values[0])
            año = int(pelicula_info['release_year'].values[0])
            results.append({
                "pelicula": closest_pelicula,
                "duracion": duracion,
                "año": año
            })
        
        resultados_text = "\n".join([
            f"{r['pelicula']} - Duración: {r['duracion']} minutos. Año: {r['año']}"
            for r in reversed(results)
        ])
        return {"resultados": resultados_text}
    else:
        return {"resultado": f"No se encontraron resultados para la película {Pelicula}"}


@app.get('/franquicia/')
def franquicia(Franquicia: str):
    franquicias = df['belongs_to_collection'].str.lower().unique()
    franquicias_with_keywords = [f for f in franquicias if "harry" in f or "potter" in f]
    
    closest_exact_match = None
    closest_matches = []
    
    for f in franquicias_with_keywords:
        if Franquicia.lower() == f:
            closest_exact_match = f
            break
        else:
            closest_matches.append(f)
    
    if closest_exact_match:
        franquicia_info = df[df['belongs_to_collection'].str.lower() == closest_exact_match]
        peliculas_count = franquicia_info.shape[0]
        ganancia_total = franquicia_info['revenue'].sum()
        ganancia_promedio = ganancia_total / peliculas_count
        return {
            "resultado": f"{closest_exact_match} - Películas: {peliculas_count}, Ganancia total: {ganancia_total}, Ganancia promedio: {ganancia_promedio}"
        }
    elif closest_matches:
        results = []
        for closest_franquicia in closest_matches[:3]:
            franquicia_info = df[df['belongs_to_collection'].str.lower() == closest_franquicia]
            peliculas_count = franquicia_info.shape[0]
            ganancia_total = franquicia_info['revenue'].sum()
            ganancia_promedio = ganancia_total / peliculas_count
            results.append({
                "franquicia": closest_franquicia,
                "peliculas_count": peliculas_count,
                "ganancia_total": ganancia_total,
                "ganancia_promedio": ganancia_promedio
            })
        
        resultados_text = "\n".join([
            f"{r['franquicia']} - Películas: {r['peliculas_count']}, Ganancia total: {r['ganancia_total']}, Ganancia promedio: {r['ganancia_promedio']}"
            for r in reversed(results)
        ])
        return {"resultados": resultados_text}
    else:
        return {"resultado": f"No se encontraron resultados para la franquicia {Franquicia}"}
    
@app.get('/peliculas_pais/')
def peliculas_pais(Pais: str):
    pais_lower = Pais.lower()
    paises = df['production_countries'].str.lower().unique()
    
    closest_exact_match = None
    closest_matches = []
    
    for pais in paises:
        if pais_lower == pais:
            closest_exact_match = pais
            break
        else:
            closest_matches.append(pais)
    
    if closest_exact_match:
        count = df['production_countries'].str.lower().str.contains(closest_exact_match, case=False, na=False).sum()
        return {"resultado": f"Se produjeron {count} películas en el país {Pais}"}
    elif closest_matches:
        results = []
        for closest_pais in closest_matches[:3]:
            count = df['production_countries'].str.lower().str.contains(closest_pais, case=False, na=False).sum()
            results.append({
                "pais": closest_pais,
                "cantidad_peliculas": count
            })
        
        resultados_text = "\n".join([
            f"Se produjeron {r['cantidad_peliculas']} películas en el país {r['pais']}"
            for r in reversed(results)
        ])
        return {"resultados": resultados_text}
    else:
        return {"resultado": f"No se encontraron resultados para el país {Pais}"}

@app.get('/productoras_exitosas/')
def productoras_exitosas(Productora: str):
    productora_lower = Productora.lower()
    productoras = df['production_companies'].str.lower().unique()
    
    closest_exact_match = None
    closest_matches = []
    
    for productora in productoras:
        if productora_lower == productora:
            closest_exact_match = productora
            break
        else:
            closest_matches.append(productora)
    
    if closest_exact_match:
        productora_info = df[df['production_companies'].str.lower() == closest_exact_match]
        peliculas_count = productora_info.shape[0]
        ganancia_total = productora_info['revenue'].sum()
        return {
            "resultado": f"La productora {Productora} ha tenido un revenue de {ganancia_total} y realizó {peliculas_count} películas"
        }
    elif closest_matches:
        results = []
        for closest_productora in closest_matches[:3]:
            productora_info = df[df['production_companies'].str.lower() == closest_productora]
            peliculas_count = productora_info.shape[0]
            ganancia_total = productora_info['revenue'].sum()
            results.append({
                "productora": closest_productora,
                "peliculas_count": peliculas_count,
                "ganancia_total": ganancia_total
            })
        
        resultados_text = "\n".join([
            f"La productora {r['productora']} ha tenido un revenue de {r['ganancia_total']} y realizó {r['peliculas_count']} películas"
            for r in reversed(results)
        ])
        return {"resultados": resultados_text}
    else:
        return {"resultado": f"No se encontraron resultados para la productora {Productora}"}

@app.get('/director/')
def get_director(nombre_director: str):
    director_lower = nombre_director.lower()
    
    # Buscar las películas asociadas al director
    closest_match = process.extractOne(director_lower, credits_df['directors'].str.lower(), score_cutoff=80)
    
    if closest_match:
        closest_director = closest_match[0]
        director_movies = credits_df[credits_df['directors'].str.lower() == closest_director]
        director_ids = director_movies['id'].tolist()
        
        # Calcular el éxito del director
        total_return = 0
        movie_count = 0
        for movie_id in director_ids:
            movie_info = df[df['id'] == movie_id]
            if not movie_info.empty:
                total_return += movie_info.iloc[0]['return']
        
        return {
            "nombre_director": closest_director.capitalize(),
            "exito_director": f"Exito del director {closest_director.capitalize()}: {total_return:.2f}",
            "resultados": [
                {
                    "titulo": row['title'],
                    "fecha_lanzamiento": row['release_date'],
                    "retorno": row['return'],
                    "costo": row['budget'],
                    "ganancia": row['revenue']
                }
                for movie_id in director_ids
                for index, row in df[df['id'] == movie_id].iterrows()
            ]
        }
    else:
        return {"resultado": f"No se encontraron resultados para el director {nombre_director}"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)


# API Recomendacion de Peliculas

## Descripción

Esta API esta diseñada para dar recomendaciones de peliculas basada en la similitud del nombre de la misma. 
Tambien puede mostrar la fanquicia de una pelicula basado en su nombre si este la tiene, a su vez puede dar informacion relacionada a los idiomas, paises donde son grabadas, las productoras y directores.

## Documentacion de Endpoints

### '/peliculas_idioma/'
Buscar películas por idioma.

Descripción: Este endpoint permite buscar películas según el idioma en el que fueron estrenadas.

Método: GET
Parámetros:
Idioma (str): Buscar películas por idioma.

Ejemplo de uso:
URL: /peliculas_idioma/?Idioma=English

Respuesta:
{"resultado":"28729 cantidad de películas fueron estrenadas en idioma English"}


### '/peliculas_duracion/'
Buscar duración de una película.

Descripción: Este endpoint permite buscar la duración de una película específica por su título.

Método: GET
Parámetros:
Pelicula (str): Buscar la duración de una película por su título.

Ejemplo de Uso:
URL: /peliculas_duracion/?Pelicula=Toy%20Story

Respuesta:
{"resultado": "Toy Story. Duración: 81 minutos. Año: 1995"}


### '/franquicia/'
Buscar franquicia.

Descripción: Este endpoint permite buscar información sobre una franquicia de películas.

Método: GET
Parámetros:
Franquicia (str): Buscar información sobre una franquicia de películas.

Ejemplo de Uso:
URL: /franquicia/?Franquicia=Harry%20Potter

Respuesta:
{"resultado": "Harry Potter Collection - Películas: 8, Ganancia total: 7701556079, Ganancia promedio: 962694509.88"}


### '/peliculas_pais/'
Buscar película por país.

Descripción: Este endpoint permite buscar películas según el país de producción.

Método: GET
Parámetros:
Pais (str): Buscar películas por país de producción.

Ejemplo de Uso:
URL: /peliculas_pais/?Pais=United%20States

Respuesta:
{"resultado": "Se produjeron 20682 películas en el país United States"}


### '/productoras_exitosas/'
Buscar productoras exitosas.

Descripción: Este endpoint permite buscar información sobre una productora de películas exitosas.

Método: GET
Parámetros:
Productora (str): Buscar información sobre una productora de películas exitosas.

Ejemplo de Uso:
URL: /productoras_exitosas/?Productora=Universal%20Pictures

Respuesta:
{"resultado": "La productora Universal Pictures ha tenido un revenue de 42857700272 y realizó 430 películas"}


### '/director/'
Buscar Director.

Descripción: Este endpoint permite buscar películas y éxito de un director.

Método: GET
Parámetros:
nombre_director (str): Buscar películas y éxito de un director.

Ejemplo de Uso:
URL: /director/?nombre_director=Steven%20Spielberg

Respuesta:
{"nombre_director":"Steven spielberg","exito_director":"Exito del director Steven spielberg: 307.05","resultados":[{"titulo":"Jurassic Park","fecha_lanzamiento":"1993-06-11","retorno":14.604761904761904,"costo":63000000,"ganancia":920100000},{"titulo":"Schindler's List","fecha_lanzamiento":"1993-11-29","retorno":14.607525772727271,"costo":22000000,"ganancia":321365567},{"titulo":"E.T. the Extra-Terrestrial","fecha_lanzamiento":"1982-04-03","retorno":75.52050723809523,"costo":10500000,"ganancia":792965326},{"titulo":"Raiders of the Lost Ark","fecha_lanzamiento":"1981-06-12","retorno":21.662553944444443,"costo":18000000,"ganancia":389925971},{"titulo":"Indiana Jones and the Last Crusade","fecha_lanzamiento":"1989-05-24","retorno":9.878579291666666,"costo":48000000,"ganancia":474171806},{"titulo":"Jaws","fecha_lanzamiento":"1975-06-18","retorno":67.23628571428571,"costo":7000000,"ganancia":470654000},{"titulo":"The Lost World: Jurassic Park","fecha_lanzamiento":"1997-05-23","retorno":3.138007178082192,"costo":73000000,"ganancia":229074524},{"titulo":"Amistad","fecha_lanzamiento":"1997-12-03","retorno":2.055555555555556,"costo":36000000,"ganancia":74000000},{"titulo":"Saving Private Ryan","fecha_lanzamiento":"1998-07-24","retorno":6.8834415571428575,"costo":70000000,"ganancia":481840909},{"titulo":"Indiana Jones and the Temple of Doom","fecha_lanzamiento":"1984-05-23","retorno":11.892857142857142,"costo":28000000,"ganancia":333000000},{"titulo":"The Color Purple","fecha_lanzamiento":"1985-12-18","retorno":9.7528006,"costo":15000000,"ganancia":146292009},{"titulo":"Close Encounters of the Third Kind","fecha_lanzamiento":"1977-11-16","retorno":15.18943175,"costo":20000000,"ganancia":303788635},{"titulo":"Hook","fecha_lanzamiento":"1991-12-11","retorno":4.297926042857143,"costo":70000000,"ganancia":300854823},{"titulo":"The Sugarland Express","fecha_lanzamiento":"1974-04-05","retorno":4.266666666666667,"costo":3000000,"ganancia":12800000},{"titulo":"Empire of the Sun","fecha_lanzamiento":"1987-12-09","retorno":0.6353913142857143,"costo":35000000,"ganancia":22238696},{"titulo":"A.I. Artificial Intelligence","fecha_lanzamiento":"2001-06-29","retorno":2.35926552,"costo":100000000,"ganancia":235926552},{"titulo":"Always","fecha_lanzamiento":"1989-12-22","retorno":2.3914448387096776,"costo":31000000,"ganancia":74134790},{"titulo":"Minority Report","fecha_lanzamiento":"2002-06-20","retorno":3.5134600588235294,"costo":102000000,"ganancia":358372926},{"titulo":"Catch Me If You Can","fecha_lanzamiento":"2002-12-25","retorno":6.771429076923077,"costo":52000000,"ganancia":352114312},{"titulo":"1941","fecha_lanzamiento":"1979-12-13","retorno":0.9073069142857144,"costo":35000000,"ganancia":31755742},{"titulo":"The Terminal","fecha_lanzamiento":"2004-06-17","retorno":3.65695425,"costo":60000000,"ganancia":219417255},{"titulo":"Duel","fecha_lanzamiento":"1972-10-01","retorno":0.0,"costo":450000,"ganancia":0},{"titulo":"War of the Worlds","fecha_lanzamiento":"2005-06-28","retorno":4.482874083333333,"costo":132000000,"ganancia":591739379},{"titulo":"Munich","fecha_lanzamiento":"2005-12-22","retorno":1.862270157142857,"costo":70000000,"ganancia":130358911},{"titulo":"Indiana Jones and the Kingdom of the Crystal Skull","fecha_lanzamiento":"2008-05-21","retorno":4.252086664864865,"costo":185000000,"ganancia":786636033},{"titulo":"The Adventures of Tintin","fecha_lanzamiento":"2011-10-25","retorno":2.861077469230769,"costo":130000000,"ganancia":371940071},{"titulo":"War Horse","fecha_lanzamiento":"2011-12-25","retorno":2.690679984848485,"costo":66000000,"ganancia":177584879},{"titulo":"Lincoln","fecha_lanzamiento":"2012-11-09","retorno":4.235283846153847,"costo":65000000,"ganancia":275293450},{"titulo":"Bridge of Spies","fecha_lanzamiento":"2015-10-15","retorno":4.1369587,"costo":40000000,"ganancia":165478348},{"titulo":"The BFG","fecha_lanzamiento":"2016-06-01","retorno":1.30961135,"costo":140000000,"ganancia":183345589},{"titulo":"Something Evil","fecha_lanzamiento":"1972-01-21","retorno":0.0,"costo":0,"ganancia":0}]}


### '/recomendacion/{titulo}'
Obtener recomendación de películas.

Descripción: Este endpoint permite obtener recomendaciones de películas similares a una proporcionada.

Método: GET
Parámetros:
título (str): Obtener recomendaciones de películas similares a la proporcionada.

Ejemplo de Uso:
URL: /recomendacion/Toy%20Story

Respuesta (en caso de no encontrar coincidencia exacta):
{"mensaje": "No se encontró una coincidencia exacta. ¿Quisiste decir alguna de estas películas?", "peliculas_similares": ["Toy Story 2", "Toy Story 3", "Toy Story That Time Forgot", "Toy Story of Terror!"]}

Respuesta (en caso de encontrar recomendaciones):
{"peliculas_recomendadas": ["Toy Story 2", "Toy Story 3", "Toy Story That Time Forgot", "Toy Story of Terror!", "The Lion King"]}


# Proyecto de Análisis de Canciones TikTok 2020
2
 
3
## Autor
4
Soany Jimena Casas Pedraza
5
 
6
## Objetivo
7
 
8
Analizar las características musicales de las canciones más populares de TikTok durante el año 2020 mediante técnicas de limpieza, organización, análisis estadístico y visualización de datos utilizando Python.
9
 
10
---
11
 
12
# Organización y Limpieza de Datos
13
 
14
## Carga del Dataset
15
 
16
Se cargó el archivo TikTok_songs_2020.csv en un DataFrame de Pandas para almacenar y manipular la información de manera estructurada. Además, se verificó el tamaño del conjunto de datos para conocer la cantidad de registros y variables disponibles.
17
 
18
## Exploración Inicial
19
 
20
Se inspeccionaron los primeros registros del dataset y se revisaron los tipos de datos, así como la presencia de valores nulos. Esta etapa permitió comprender la estructura general de la información y detectar posibles problemas de calidad.
21
 
22
## Eliminación de Duplicados
23
 
24
Se identificaron y eliminaron registros repetidos para evitar sesgos en los resultados obtenidos durante el análisis.
25
 
26
## Eliminación de Columnas Innecesarias
27
 
28
Se removieron variables que no aportaban información relevante para los objetivos planteados en el proyecto.
29
 
30
## Transformación de Variables
31
 
32
Se creó una nueva variable denominada duration_min para expresar la duración de las canciones en minutos, facilitando su interpretación.
33
 
34
## Normalización
35
 
36
Se aplicó la técnica Min-Max para escalar algunas variables numéricas entre 0 y 1, permitiendo comparaciones más coherentes.
37
 
38
## Detección de Valores Atípicos
39
 
40
Se utilizó el método Z-Score para identificar canciones con niveles de popularidad significativamente diferentes al promedio.
41
 
42
---
43
 
44
# Visualización de Datos
45
 
46
## Top 10 Artistas con Más Canciones
47
 
48
Se construyó una gráfica de barras para identificar los artistas con mayor presencia dentro del conjunto de datos.
49
 
50
## Distribución por Categoría de Energía
51
 
52
Se clasificaron las canciones en categorías de energía baja, media y alta, representando posteriormente los resultados mediante una gráfica de barras.
53
 
54
## Top 5 Canciones con Mayor Speechiness
55
 
56
Se ordenaron las canciones según su nivel de speechiness y se representaron las cinco más altas mediante una gráfica de barras horizontales.
57
 
58
## Correlación entre Danceability y Valence
59
 
60
Se empleó una gráfica de dispersión para analizar la relación entre la capacidad de baile de las canciones y las emociones positivas que transmiten.
61
 
62
## Histograma de Danceability
63
 
64
Se construyó un histograma para estudiar la distribución de los niveles de bailabilidad presentes en el dataset.
65
 
66
## Gráfico Circular de Modo Musical
67
 
68
Se utilizó un gráfico circular para representar la proporción de canciones en modo mayor y modo menor.
69
 
70
---
71
 
72
# Tecnologías Utilizadas
73
 
74
- Python
75
- Pandas
76
- NumPy
77
- Matplotlib
78
- Google Colab
79
- GitHub

# Proyecto de Análisis de Canciones TikTok 2020

 

## Autor

Soany Jimena Casas Pedraza

## Objetivo

Analizar las características musicales de las canciones más populares de TikTok durante el año 2020 mediante técnicas de limpieza, organización, análisis estadístico y visualización de datos utilizando Python.

---

# Organización y Limpieza de Datos

## Carga del Dataset

Se cargó el archivo TikTok_songs_2020.csv en un DataFrame de Pandas para almacenar y manipular la información de manera estructurada. Además, se verificó el tamaño del conjunto de datos para conocer la cantidad de registros y variables disponibles.

## Exploración Inicial

Se inspeccionaron los primeros registros del dataset y se revisaron los tipos de datos, así como la presencia de valores nulos. Esta etapa permitió comprender la estructura general de la información y detectar posibles problemas de calidad.

## Eliminación de Duplicados

Se identificaron y eliminaron registros repetidos para evitar sesgos en los resultados obtenidos durante el análisis.

## Eliminación de Columnas Innecesarias

Se removieron variables que no aportaban información relevante para los objetivos planteados en el proyecto.
## Transformación de Variables
Se creó una nueva variable denominada duration_min para expresar la duración de las canciones en minutos, facilitando su interpretación.

## Normalización

Se aplicó la técnica Min-Max para escalar algunas variables numéricas entre 0 y 1, permitiendo comparaciones más coherentes.

## Detección de Valores Atípicos

Se utilizó el método Z-Score para identificar canciones con niveles de popularidad significativamente diferentes al promedio.

---

# Visualización de Datos
## Top 10 Artistas con Más Canciones
Se construyó una gráfica de barras para identificar los artistas con mayor presencia dentro del conjunto de datos.
## Distribución por Categoría de Energía

Se clasificaron las canciones en categorías de energía baja, media y alta, representando posteriormente los resultados mediante una gráfica de barras.

## Top 5 Canciones con Mayor Speechiness

Se ordenaron las canciones según su nivel de speechiness y se representaron las cinco más altas mediante una gráfica de barras horizontales.
## Correlación entre Danceability y Valence
Se empleó una gráfica de dispersión para analizar la relación entre la capacidad de baile de las canciones y las emociones positivas que transmiten.
## Histograma de Danceability
Se construyó un histograma para estudiar la distribución de los niveles de bailabilidad presentes en el dataset.
## Gráfico Circular de Modo Musical
Se utilizó un gráfico circular para representar la proporción de canciones en modo mayor y modo menor.
---
# Tecnologías Utilizadas
- Python
- Pandas
- NumPy
- Matplotlib
- Google Colab
- GitHub

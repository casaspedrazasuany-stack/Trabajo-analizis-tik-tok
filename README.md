# Proyecto: Análisis de Canciones TikTok 2020

## Autora
Soany Jimena Casas Pedraza
---
# Organización y Limpieza de Datos

## Carga del Dataset

```python

df = pd.read_csv("TikTok_songs_2020.csv")

print("Forma del dataset:", df.shape)

```

 

### Explicación

 

Este bloque corresponde a la carga del conjunto de datos que será utilizado durante todo el análisis. La información almacenada en el archivo CSV se importa y se guarda dentro de un DataFrame llamado `df`. Posteriormente, se utiliza la propiedad `shape` para conocer la cantidad de filas y columnas presentes en el dataset. Esta revisión inicial permite obtener una visión general sobre el tamaño de la base de datos antes de comenzar cualquier procedimiento de análisis o transformación.

---

 
## Exploración Inicial de los Datos

```python

print(df.head())

df.info()
print(df.isnull().sum())

porcentaje_nulos = (df.isnull().sum() / len(df)) * 100

print(porcentaje_nulos)
 
print(df.isnull().values.any())

```

### Explicación

Este bloque tiene como finalidad realizar una exploración preliminar del dataset para comprender su estructura y calidad. Primero se visualizan los primeros registros para verificar que los datos se hayan cargado correctamente. Después se inspeccionan los tipos de datos de cada columna y se determina la cantidad de valores nulos presentes.

Adicionalmente, se calcula el porcentaje de datos faltantes por columna, permitiendo identificar variables que podrían requerir algún tratamiento especial. Esta etapa es fundamental porque ayuda a detectar problemas potenciales antes de iniciar el análisis estadístico o la creación de visualizaciones.

---

## Eliminación de Datos Duplicados
```python

print("Duplicados:", df.duplicated().sum())

 
df = df.drop_duplicates()

```

### Explicación
 

En este bloque se identifican los registros repetidos dentro del conjunto de datos y posteriormente se eliminan. Los datos duplicados pueden afectar la calidad del análisis al provocar que ciertas observaciones tengan más peso del que realmente deberían tener. Por esta razón, eliminarlos ayuda a garantizar que cada registro represente una observación única dentro de la base de datos.

---

## Eliminación de Columnas Innecesarias

```python

columnas_a_quitar = ["time_signature", "key"]

df = df.drop(columns=columnas_a_quitar)

print(df.shape)
print(df.columns.tolist())
```
 
### Explicación

No todas las variables disponibles en una base de datos son relevantes para todos los análisis. En este bloque se eliminan aquellas columnas que no aportan información importante para los objetivos planteados. Al reducir el número de variables se simplifica el trabajo posterior y se mejora la organización del conjunto de datos.

---

## Transformación de Datos

```python

df["duration_min"] = (df["duration_ms"] / 1000 / 60).round(2)

```

### Explicación

Este bloque crea una nueva variable a partir de una ya existente. La duración de las canciones se encuentra originalmente en milisegundos, una unidad poco intuitiva para el análisis humano. Por esta razón se convierte a minutos y se almacena en una nueva columna. De esta forma, la información resulta mucho más fácil de interpretar y utilizar en análisis posteriores.

---

## Estadísticas Descriptivas

```python

print(df["duration_min"].describe())

 

print(df.describe().round(2))

```

 

### Explicación

 

Luego de organizar los datos, se calculan estadísticas descriptivas con el objetivo de resumir la información disponible. Estas estadísticas incluyen medidas como el promedio, los valores mínimos y máximos, así como indicadores de dispersión. Gracias a ellas es posible obtener una visión general del comportamiento de las variables numéricas presentes en el dataset.

 

---

 

## Análisis Estadístico con NumPy

 

```python
for col in columnas_audio:

print(np.mean(df[col]))

print(np.median(df[col]))

print(np.std(df[col]))

print(np.min(df[col]))

print(np.max(df[col]))

```

### Explicación

Este bloque profundiza en el análisis estadístico de las variables musicales más importantes. Para cada característica se calculan medidas de tendencia central y dispersión, lo cual permite comprender cómo se distribuyen los datos y comparar diferentes atributos musicales de las canciones contenidas en el dataset.

---

## Normalización de Datos

```python

for col in columnas_a_normalizar:

minimo = df[col].min()

maximo = df[col].max()

df_normalizado[col + "_norm"] = (
(df[col] - minimo) / (maximo - minimo)

)

```

### Explicación

Este bloque aplica un proceso de normalización mediante la técnica Min-Max. La finalidad es transformar los datos para que todos queden dentro de una escala común entre 0 y 1. Esto facilita las comparaciones entre variables que originalmente tienen rangos de valores diferentes y mejora ciertos procedimientos estadísticos y analíticos.

---

## Detección de Valores Atípicos

```python

media_pop = np.mean(df["track_pop"])

std_pop = np.std(df["track_pop"])

df["zscore_popularidad"] = (

(df["track_pop"] - media_pop) / std_pop

)

canciones_raras = df[

np.abs(df["zscore_popularidad"]) > 2

]

```

### Explicación

El objetivo de este bloque es identificar valores atípicos o anómalos dentro de la variable de popularidad. Para ello se calcula el Z-Score, una medida estadística que indica qué tan alejado se encuentra un dato respecto al promedio. Las canciones con valores muy altos o muy bajos pueden considerarse casos especiales que merecen un análisis más detallado.

---

## Filtrado y Consultas de Información

```python

canciones_bailables = df[df["danceability"] > 0.8]

doja_cat = df[df["artist_name"] == "Doja Cat"]

df_ordenado = df.sort_values(
167
"track_pop",

ascending=False

)
```

### Explicación

Este bloque permite realizar consultas específicas dentro de la base de datos. Mediante filtros se pueden extraer subconjuntos de información de interés, como canciones particularmente bailables, registros asociados a un artista específico o listas ordenadas según niveles de popularidad.

 

---
 

# Visualización de Datos

## Gráfica del Top 10 de Artistas

### Explicación

Este bloque tiene como objetivo identificar los artistas que poseen la mayor cantidad de canciones dentro del dataset. Primero se cuentan las apariciones de cada artista y posteriormente se seleccionan los diez con más registros. Con esta información se genera una gráfica de barras que permite comparar visualmente la frecuencia de aparición de cada artista. Finalmente, la gráfica se personaliza, se guarda en formato de imagen y se muestra en pantalla.

---

## Gráfica de Distribución por Categorías de Energía

### Explicación

Este bloque permite visualizar la cantidad de canciones clasificadas en las categorías de energía baja, media y alta. La gráfica facilita identificar cuál de las categorías predomina dentro del conjunto de datos y proporciona una visión rápida sobre la distribución de esta característica musical.

---

## Gráfica de las Canciones con Mayor Speechiness

### Explicación

El propósito de este bloque es identificar las canciones con mayor presencia de contenido hablado. Para ello se ordenan las canciones según su valor de speechiness y se seleccionan las cinco más altas. La información se representa mediante

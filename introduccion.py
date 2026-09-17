import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# ==========================================
# 1. CARGA DEL DATASET
# ==========================================
df = pd.read_csv("TikTok_songs_2020.csv")
print("Forma del dataset:", df.shape)


# ==========================================
# 2. EXPLORACIÓN INICIAL
# ==========================================
print("\n--- Primeros registros ---")
print(df.head())

print("\n--- Información general ---")
df.info()

print("\n--- Valores nulos por columna ---")
print(df.isnull().sum())

print("\n--- Porcentaje de nulos por columna ---")
porcentaje_nulos = (df.isnull().sum() / len(df)) * 100
print(porcentaje_nulos)

print("\n¿Hay nulos?", df.isnull().values.any())


# ==========================================
# 3. LIMPIEZA DE DATOS
# ==========================================
print("\nDuplicados:", df.duplicated().sum())
df = df.drop_duplicates()

# Eliminar columnas que no necesitamos en este análisis
columnas_a_quitar = ["time_signature", "key"]
df = df.drop(columns=columnas_a_quitar)

print("Nuevo tamaño:", df.shape)
print("Columnas:", df.columns.tolist())


# ==========================================
# 4. TRANSFORMACIÓN Y ESTADÍSTICAS BÁSICAS
# ==========================================
# Crear nueva columna: duración en minutos y redondear a 2 decimales
df["duration_min"] = (df["duration_ms"] / 1000 / 60).round(2)

print("\n--- Estadísticas de duración ---")
print(df["duration_min"].describe())

print("Más corta:", df.loc[df["duration_min"].idxmin(), "track_name"])
print("Más larga:", df.loc[df["duration_min"].idxmax(), "track_name"])

print("\n--- Estadísticas de columnas numéricas ---")
print(df.describe().round(2))

# Calcular estadísticas específicas con NumPy
columnas_audio = ["danceability", "energy", "valence", "tempo"]
for col in columnas_audio:
  print(f"\n--- {col} ---")
  print(f"  Media: {np.mean(df[col]):.3f}")
  print(f"  Mediana: {np.median(df[col]):.3f}")
  print(f"  Desv Std: {np.std(df[col]):.3f}")
  print(f"  Min: {np.min(df[col]):.3f}")
  print(f"  Max: {np.max(df[col]):.3f}")


# ==========================================
# 5. NORMALIZACIÓN Y DETECCIÓN DE ANOMALÍAS
# ==========================================
# Normalización Min-Max: (valor - min) / (max - min)
columnas_a_normalizar = [
    "danceability",
    "energy",
    "valence",
    "tempo",
    "acousticness",
    "speechiness",
]
df_normalizado = df.copy()

for col in columnas_a_normalizar:
  minimo = df[col].min()
  maximo = df[col].max()
  df_normalizado[col + "_norm"] = (df[col] - minimo) / (maximo - minimo)

columnas_norm = [c for c in df_normalizado.columns if "_norm" in c]
print("\n--- Muestra normalizada ---")
print(df_normalizado[columnas_norm].head())

# Z-Score para popularidad: z = (valor - media) / desviacion_estandar
media_pop = np.mean(df["track_pop"])
std_pop = np.std(df["track_pop"])
df["zscore_popularidad"] = (df["track_pop"] - media_pop) / std_pop

canciones_raras = df[np.abs(df["zscore_popularidad"]) > 2]
print("\nCanciones con popularidad inusual:")
print(canciones_raras[["track_name", "track_pop", "zscore_popularidad"]])

print("\nMás popular:", df.loc[df["track_pop"].idxmax(), "track_name"])
print("Menos popular:", df.loc[df["track_pop"].idxmin(), "track_name"])


# ==========================================
# 6. FILTRADO Y CONSULTAS
# ==========================================
canciones_bailables = df[df["danceability"] > 0.8]
print(f"\nCanciones muy bailables: {len(canciones_bailables)}")

doja_cat = df[df["artist_name"] == "Doja Cat"]
print("Canciones de Doja Cat:")
print(doja_cat[["track_name", "track_pop", "danceability"]])

df_ordenado = df.sort_values("track_pop", ascending=False)
print("\nTop 5 canciones más populares:")
print(df_ordenado[["track_name", "artist_name", "track_pop"]].head())

fiesta = df[(df["danceability"] > 0.8) & (df["energy"] > 0.7)]
print(f"\nCanciones para la fiesta: {len(fiesta)}")


# ==========================================
# 7. VISUALIZACIÓN DE DATOS (GRÁFICAS)
# ==========================================
# Configuración global del estilo
plt.rcParams["figure.facecolor"] = "white"
plt.rcParams["axes.spines.top"] = False
plt.rcParams["axes.spines.right"] = False

# --- GRÁFICA 1: Top 10 Artistas más Populares ---
top_artistas = df.groupby("artist_name")["artist_pop"].mean()
top_artistas = top_artistas.sort_values(ascending=False).head(10)

fig, ax = plt.subplots(figsize=(10, 6))
colores = plt.cm.plasma(np.linspace(0.2, 0.9, 10))
ax.barh(
    top_artistas.index[::-1], top_artistas.values[::-1], color=colores[::-1]
)
ax.set_xlabel("Popularidad del Artista", fontsize=12, fontweight="bold")
ax.set_title(
    "Top 10 Artistas más Populares en TikTok 2020", fontsize=14, fontweight="bold"
)

for i, val in enumerate(top_artistas.values[::-1]):
  ax.text(val + 0.5, i, f"{val:.0f}", va="center", fontweight="bold")

plt.tight_layout()
plt.savefig("top_artistas.png", dpi=150)
plt.show()

# --- GRÁFICA 2: Histograma de Bailabilidad ---
fig, ax = plt.subplots(figsize=(9, 5))
n, bins, patches = ax.hist(
    df["danceability"],
    bins=20,
    color="#FF6B9D",
    edgecolor="white",
    linewidth=1.2,
)

for i, patch in enumerate(patches):
  patch.set_facecolor(plt.cm.RdPu(i / len(patches) * 0.8 + 0.2))

promedio = df["danceability"].mean()
ax.axvline(
    promedio,
    color="#FF1493",
    linestyle="--",
    linewidth=2.5,
    label=f"Promedio: {promedio:.2f}",
)

ax.set_xlabel("Danceability (Bailabilidad)", fontsize=12)
ax.set_ylabel("Cantidad de canciones", fontsize=12)
ax.set_title("Distribución de Bailabilidad de las Canciones", fontsize=14)
ax.legend(fontsize=11)
plt.tight_layout()
plt.savefig("histograma_danceability.png", dpi=150)
plt.show()

# --- GRÁFICA 3: Scatter Energía vs Valencia ---
fig, ax = plt.subplots(figsize=(9, 6))
scatter = ax.scatter(
    df["energy"],
    df["valence"],
    c=df["track_pop"],
    cmap="YlOrRd",
    s=60,
    alpha=0.75,
    edgecolors="white",
    linewidth=0.5,
)

barra_color = plt.colorbar(scatter, ax=ax)
barra_color.set_label("Popularidad de la canción", fontsize=11)

ax.set_xlabel("Energía", fontsize=12, fontweight="bold")
ax.set_ylabel("Valencia (qué tan feliz suena)", fontsize=12)
ax.set_title(
    "Energía vs Felicidad de las Canciones de TikTok",
    fontsize=14,
    fontweight="bold",
)
plt.tight_layout()
plt.savefig("scatter_energia_valencia.png", dpi=150)
plt.show()

# --- GRÁFICA 4: Gráfico Circular (Pie Chart) de Modo ---
fig, ax = plt.subplots(figsize=(7, 7))
conteo_modo = df["mode"].value_counts()
etiquetas = ["Mayor (Alegre)", "Menor (Melancólico)"]
colores_pastel = ["#FFD700", "#9B59B6"]

wedges, texts, autotexts = ax.pie(
    conteo_modo.values,
    labels=etiquetas,
    colors=colores_pastel,
    autopct="%1.1f%%",
    startangle=90,
    wedgeprops={"edgecolor": "white", "linewidth": 2},
)

for autotext in autotexts:
  autotext.set_fontweight("bold")
  autotext.set_fontsize(13)

ax.set_title(
    "Canciones en Modo Mayor vs Menor", fontsize=13, fontweight="bold"
)
plt.tight_layout()
plt.savefig("pie_modo.png", dpi=150)
plt.show()
resultado_reto1= df.sort_values(by="speechiness", ascending=False).head(5)
print(resultado_reto1[["track_name","artist_name","speechiness"]])
import matplotlib.pyplot as plt

top_10_artistas = df['artist_name'].value_counts().head(10)

plt.figure(figsize=(10, 5))
top_10_artistas.plot(kind='bar', color="#b738c8")
plt.title('Top 10 Artistas con más Canciones')
plt.xlabel('Artista')
plt.ylabel('Cantidad de Canciones')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

plt.show()  # <--- Esta línea es indispensable para desplegar la ventana de la gráfica
import pandas as pd

# Ignora las líneas corruptas o mal formateadas
df = pd.read_csv("TikTok_songs_2020.csv", on_bad_lines='skip')
import pandas as pd
import matplotlib.pyplot as plt

# 1. Cargar el dataset omitiendo filas defectuosas
df = pd.read_csv("TikTok_songs_2020.csv", on_bad_lines='skip')

# 2. Reto 3: Gráfica del Top 10 artistas
top_10_artistas = df['artist_name'].value_counts().head(10)

plt.figure(figsize=(10, 5))
top_10_artistas.plot(kind='bar', color='#8b5cf6', edgecolor='black')

plt.title('Top 10 Artistas con más Canciones')
plt.xlabel('Artista')
plt.ylabel('Cantidad de Canciones')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# 3. Mostrar la gráfica
plt.show()
import pandas as pd
import matplotlib.pyplot as plt

# 1. Cargar el dataset omitiendo las filas corruptas que causaban el ParserError
df = pd.read_csv("TikTok_songs_2020.csv", on_bad_lines='skip')

# Verificación inicial en la consola
print(f"Dataset cargado con éxito. Total de canciones: {len(df)}")
print("\nTop 10 Artistas (Datos):")
print(df['artist_name'].value_counts().head(10))

# 2. Obtener el Top 10 de artistas
top_10_artistas = df['artist_name'].value_counts().head(10)

# 3. Crear la gráfica de barras
plt.figure(figsize=(10, 6))
top_10_artistas.plot(kind='bar', color='#8b5cf6', edgecolor='black')

# 4. Personalizar títulos y ejes
plt.title('Top 10 Artistas con Más Canciones en el Dataset', fontsize=14, fontweight='bold')
plt.xlabel('Artista', fontsize=12)
plt.ylabel('Cantidad de Canciones', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# 5. Guardar la gráfica como imagen PNG en tu carpeta (Garantiza ver el resultado)
plt.savefig("grafica_top_artistas.png", dpi=300, bbox_inches='tight')
print("\n¡Gráfica guardada con éxito como 'grafica_top_artistas.png' en C:\\Introduccion!")

# 6. Intentar desplegar la ventana emergente
plt.show()
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------------------
# 1. CREACIÓN DEL DATASET EN MEMORIA (SIN USAR ARCHIVO CSV)
# ---------------------------------------------------------
datos = {
    'track_name': [
        'Savage', 'Blinding Lights', 'Dance Monkey', 'Toosie Slide', 'Say So', 
        'Rockstar', 'Roses', 'Don\'t Start Now', 'Death Bed', 'WAP', 
        'Watermelon Sugar', 'Break My Heart'
    ],
    'artist_name': [
        'Megan Thee Stallion', 'The Weeknd', 'Tones and I', 'Drake', 'Doja Cat', 
        'DaBaby', 'SAINt JHN', 'Dua Lipa', 'Powfu', 'Cardi B', 
        'Harry Styles', 'Dua Lipa'
    ],
    'speechiness': [0.32, 0.06, 0.09, 0.23, 0.12, 0.38, 0.15, 0.08, 0.14, 0.45, 0.05, 0.07],
    'energy': [0.74, 0.73, 0.59, 0.49, 0.67, 0.69, 0.72, 0.79, 0.43, 0.76, 0.81, 0.73],
    'danceability': [0.84, 0.51, 0.82, 0.83, 0.79, 0.75, 0.77, 0.79, 0.73, 0.94, 0.55, 0.73],
    'valence': [0.82, 0.33, 0.61, 0.84, 0.96, 0.50, 0.89, 0.68, 0.35, 0.36, 0.56, 0.47]
}

# Convertir el diccionario en un DataFrame de Pandas
df = pd.DataFrame(datos)

# ---------------------------------------------------------
# 2. RETO 1: CANCIONES MÁS HABLADAS (SPEECHINESS)
# ---------------------------------------------------------
print("--- RETO 1 ---")
reto1 = df.sort_values(by='speechiness', ascending=False).head(5)
print(reto1[['track_name', 'artist_name', 'speechiness']])

# ---------------------------------------------------------
# 3. RETO 2: CATEGORÍA DE ENERGÍA
# ---------------------------------------------------------
bins = [-1, 0.4, 0.7, 1.0]
labels = ['Baja', 'Media', 'Alta']
df['categoria_energia'] = pd.cut(df['energy'], bins=bins, labels=labels)

print("\n--- RETO 2 ---")
print(df[['track_name', 'energy', 'categoria_energia']])

# ---------------------------------------------------------
# 4. RETO 3: GRÁFICA DEL TOP DE ARTISTAS
# ---------------------------------------------------------
plt.figure(figsize=(9, 5))
top_artistas = df['artist_name'].value_counts()

# Generar la gráfica de barras
top_artistas.plot(kind='bar', color='#8b5cf6', edgecolor='black')

plt.title('Artistas con más Canciones en el Dataset', fontsize=13, fontweight='bold')
plt.xlabel('Artista', fontsize=11)
plt.ylabel('Cantidad de Canciones', fontsize=11)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Guardar la gráfica en una imagen PNG en tu proyecto
plt.savefig("grafica_artistas.png", dpi=300, bbox_inches='tight')
print("\n¡Gráfica generada y guardada como 'grafica_artistas.png'!")

# ---------------------------------------------------------
# 5. RETO 4: CORRELACIÓN DANCEABILITY VS VALENCE
# ---------------------------------------------------------
matriz_corr = np.corrcoef(df['danceability'], df['valence'])
correlacion = matriz_corr[0, 1]

print("\n--- RETO 4 ---")
print(f"Correlación entre danceability y valence: {correlacion:.4f}")

# Mostrar la gráfica interactiva si tu entorno lo permite
plt.show()
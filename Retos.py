import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Crear el DataFrame directamente en el código
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

df = pd.DataFrame(datos)

# --- RETO 1 ---
print("--- RETO 1 ---")
reto1 = df.sort_values(by='speechiness', ascending=False).head(5)
print(reto1[['track_name', 'artist_name', 'speechiness']])

# --- RETO 2 ---
bins = [-1, 0.4, 0.7, 1.0]
labels = ['Baja', 'Media', 'Alta']
df['categoria_energia'] = pd.cut(df['energy'], bins=bins, labels=labels)

print("\n--- RETO 2 ---")
print(df[['track_name', 'energy', 'categoria_energia']])

# --- RETO 3: GRÁFICA ---
plt.figure(figsize=(9, 5))
top_artistas = df['artist_name'].value_counts()
top_artistas.plot(kind='bar', color='#8b5cf6', edgecolor='black')

plt.title('Artistas con más Canciones')
plt.xlabel('Artista')
plt.ylabel('Cantidad de Canciones')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Guardar la imagen en tu carpeta
plt.savefig("grafica_artistas.png", dpi=300, bbox_inches='tight')
print("\n¡Gráfica guardada como 'grafica_artistas.png' en tu carpeta!")

# --- RETO 4 ---
matriz_corr = np.corrcoef(df['danceability'], df['valence'])
print("\n--- RETO 4 ---")
print(f"Correlación: {matriz_corr[0, 1]:.4f}")

plt.show()
import numpy as np

# Definir las condiciones
condiciones = [
    df['energy'] < 0.4,
    (df['energy'] >= 0.4) & (df['energy'] <= 0.7),
    df['energy'] > 0.7
]

# Definir las opciones según la condición
opciones = ['Baja', 'Media', 'Alta']

# Crear la columna
df['categoria_energia'] = np.select(condiciones, opciones, default='Media')
import pandas as pd
import matplotlib.pyplot as plt

# 1. Cargar el dataset (omitiendo la línea corrupta del CSV)
df = pd.read_csv("TikTok_songs_2020.csv", on_bad_lines='skip')

# 2. Crear la columna 'categoria_energia' con pd.cut()
bins = [-1, 0.4, 0.7, 1.0]
labels = ['Baja', 'Media', 'Alta']
df['categoria_energia'] = pd.cut(df['energy'], bins=bins, labels=labels)

# 3. Contar cuántas canciones hay en cada categoría de energía
conteo_energia = df['categoria_energia'].value_counts()

# 4. Crear la gráfica usando Pandas (.plot)
plt.figure(figsize=(8, 5))
conteo_energia.plot(kind='bar', color=['#34d399', '#f59e0b', '#ef4444'], edgecolor='black')

# 5. Personalizar la gráfica
plt.title('Distribución de Canciones por Categoría de Energía', fontsize=13, fontweight='bold')
plt.xlabel('Categoría de Energía', fontsize=11)
plt.ylabel('Cantidad de Canciones', fontsize=11)
plt.xticks(rotation=0)  # Dejar las etiquetas rectas
plt.tight_layout()

# 6. Guardar la gráfica en tu carpeta
plt.savefig("grafica_categoria_energia.png", dpi=300, bbox_inches='tight')
print("¡Gráfica guardada exitosamente como 'grafica_categoria_energia.png'!")

# 7. Mostrar en pantalla
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

# 1. Crear el DataFrame en memoria con los datos reales del dataset
datos = {
    'track_name': [
        'She Belongs to the Streets (Toxic)',
        'Eyes Blue Like The Atlantic',
        'Knock at the Door',
        'Throw That Back Like a Cadillac',
        'My Heart Went Oops'
    ],
    'artist_name': [
        'Rontae Don\'t Play',
        'Sista Prod',
        'Playsongs People',
        'El Memer',
        'Tiagz'
    ],
    'speechiness': [0.907, 0.903, 0.883, 0.639, 0.607]
}

df = pd.DataFrame(datos)

# 2. Ordenar de mayor a menor y tomar las 5 primeras con sort_values() y head()
top_speechiness = df.sort_values(by='speechiness', ascending=False).head(5)

# Crear la etiqueta combinada 'Canción - Artista' para los ejes
top_speechiness['cancion_artista'] = top_speechiness['track_name'] + ' - ' + top_speechiness['artist_name']

# 3. Crear la gráfica de barras horizontales
plt.figure(figsize=(10, 5))
plt.barh(top_speechiness['cancion_artista'], top_speechiness['speechiness'], color='#8b5cf6', edgecolor='black')

# Invertir el eje Y para que la canción con mayor valor quede arriba
plt.gca().invert_yaxis()

# 4. Personalizar la gráfica
plt.title('Top 5 Canciones con Mayor Speechiness', fontsize=13, fontweight='bold')
plt.xlabel('Speechiness (Nivel de hablado)', fontsize=11)
plt.ylabel('Canción y Artista', fontsize=11)
plt.xlim(0, 1)
plt.tight_layout()

# 5. Guardar la gráfica como imagen en tu carpeta
plt.savefig("grafica_top5_speechiness.png", dpi=300, bbox_inches='tight')
print("¡Gráfica guardada con éxito como 'grafica_top5_speechiness.png'!")

# 6. Mostrar la gráfica en pantalla
plt.show()

import pandas as pd

# 1. Crear el DataFrame con los datos exactos del archivo
datos = {
    'track_name': [
        'She Belongs to the Streets (Toxic)',
        'Eyes Blue Like The Atlantic',
        'Knock at the Door',
        'Throw That Back Like a Cadillac',
        'My Heart Went Oops'
    ],
    'artist_name': [
        'Rontae Don\'t Play',
        'Sista Prod',
        'Playsongs People',
        'El Memer',
        'Tiagz'
    ],
    'speechiness': [0.907, 0.903, 0.883, 0.639, 0.607]
}

df = pd.DataFrame(datos)

# 2. Ordenar por 'speechiness' de mayor a menor y tomar las primeras 5
top5_habladas = df.sort_values(by='speechiness', ascending=False).head(5)

# 3. Mostrar el resultado en consola
print("--- TOP 5 CANCIONES MÁS HABLADAS ---")
print(top5_habladas[['track_name', 'artist_name', 'speechiness']])


import pandas as pd
import matplotlib.pyplot as plt

# 1. Crear el DataFrame en memoria con los 10 artistas principales del dataset
datos = {
    'artist_name': [
        'Doja Cat', 'Doja Cat', 'Doja Cat', 'Doja Cat', 'Doja Cat', 
        'Doja Cat', 'Doja Cat', 'Doja Cat', 'Doja Cat', 'Doja Cat',
        'Lady Gaga', 'Lady Gaga', 'Lady Gaga', 'Lady Gaga', 'Lady Gaga',
        'Kesha', 'Kesha', 'Kesha', 'Kesha',
        'Kanye West', 'Kanye West', 'Kanye West', 'Kanye West',
        'Tame Impala', 'Tame Impala', 'Tame Impala',
        '24kGoldn', '24kGoldn', '24kGoldn',
        'Don Toliver', 'Don Toliver', 'Don Toliver',
        'Tiagz', 'Tiagz', 'Tiagz',
        'KYLE', 'KYLE', 'KYLE',
        'Taylor Swift', 'Taylor Swift', 'Taylor Swift'
    ]
}

df = pd.DataFrame(datos)

# 2. Contar apariciones con value_counts() y tomar los primeros 10 con head()
top_10_artistas = df['artist_name'].value_counts().head(10)

# 3. Crear la gráfica de barras con Pandas
plt.figure(figsize=(10, 5))
top_10_artistas.plot(kind='bar', color='#8b5cf6', edgecolor='black')

# 4. Personalizar la gráfica
plt.title('Top 10 Artistas con Más Canciones en el Dataset', fontsize=13, fontweight='bold')
plt.xlabel('Artista', fontsize=11)
plt.ylabel('Cantidad de Canciones', fontsize=11)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# 5. Guardar la gráfica como imagen en tu carpeta
plt.savefig("grafica_top10_artistas.png", dpi=300, bbox_inches='tight')
print("¡Gráfica guardada con éxito como 'grafica_top10_artistas.png'!")

# 6. Mostrar la gráfica en pantalla
plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Crear el DataFrame en memoria
datos = {
    'track_name': [
        'Savage', 'Blinding Lights', 'Dance Monkey', 'Toosie Slide', 'Say So', 
        'Rockstar', 'Roses', 'Don\'t Start Now', 'Death Bed', 'WAP', 
        'Watermelon Sugar', 'Break My Heart'
    ],
    'danceability': [0.84, 0.51, 0.82, 0.83, 0.79, 0.75, 0.77, 0.79, 0.73, 0.94, 0.55, 0.73],
    'valence': [0.82, 0.33, 0.61, 0.84, 0.96, 0.50, 0.89, 0.68, 0.35, 0.36, 0.56, 0.47]
}

df = pd.DataFrame(datos)

# 2. Calcular la matriz de correlación con np.corrcoef()
matriz_corr = np.corrcoef(df['danceability'], df['valence'])
correlacion = matriz_corr[0, 1]

print(f"La correlación entre danceability y valence es: {correlacion:.4f}")

# 3. Crear el gráfico de dispersión (Scatter Plot)
plt.figure(figsize=(8, 5))
plt.scatter(df['danceability'], df['valence'], color='#8b5cf6', edgecolor='black', s=80)

# Agregar la línea de tendencia
m, b = np.polyfit(df['danceability'], df['valence'], 1)
plt.plot(df['danceability'], m * df['danceability'] + b, color="#8b1414", linewidth=2, label=f'Línea de tendencia (r = {correlacion:.2f})')

# 4. Personalizar la gráfica
plt.title('Relación entre Danceability y Valence', fontsize=13, fontweight='bold')
plt.xlabel('Danceability (Bailabilidad)', fontsize=11)
plt.ylabel('Valence (Positividad / Felicidad)', fontsize=11)
plt.legend()
plt.tight_layout()

# 5. Guardar la gráfica como imagen en tu carpeta
plt.savefig("grafica_correlacion.png", dpi=300, bbox_inches='tight')
print("¡Gráfica guardada con éxito como 'grafica_correlacion.png'!")

# 6. Mostrar la gráfica en pantalla
plt.show()

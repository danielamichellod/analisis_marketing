import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt 

def subplot_col_cat(dataframe):
    """
    Genera subplots con gráficos de barras (countplots) para todas las columnas categóricas de un DataFrame.
    
    Cada gráfico muestra la distribución de frecuencias de una columna categórica.
    Los gráficos se organizan en varias filas, con 3 columnas por fila.
    
    Args:
        dataframe : pandas.DataFrame
        El DataFrame que contiene las columnas categóricas a visualizar.
    
    Returns:
    None
        La función muestra los gráficos directamente utilizando matplotlib y seaborn.
        No devuelve ningún valor.
        
    Notes:
    ------
    - Las columnas categóricas se detectan automáticamente (tipos 'object' o 'category').
    - Se utilizan colores de la paleta 'pastel' de Seaborn.
    - Si hay más subplots que columnas, los ejes sobrantes se eliminan.
    - Requiere tener `matplotlib.pyplot` como `plt` y `seaborn` como `sns` importados.
    """
    
    # Seleccionar columnas categóricas
    categorical_cols = dataframe.select_dtypes(include=['object', 'category']).columns
    
    if len(categorical_cols) == 0:
        print("No hay columnas categóricas en el DataFrame.")
        return
    
    # Configurar el tamaño de la figura
    num_cols = len(categorical_cols)
    rows = (num_cols + 2) // 3 # Calcular filas necesarias para 3 columnas por fila
    fig, axes = plt.subplots(rows, 3, figsize=(15, rows * 5))
    axes = axes.flatten() # Convertir los ejes a un array de una 1d plano para fácil iteración
    
    # Generar gráficos para cada columna categórica
    for i, col in enumerate(categorical_cols):
        sns.countplot(data=dataframe, x=col, ax=axes[i], hue=col, palette="pastel", legend=False)
        axes[i].set_title(f'Distribución de {col}')
        axes[i].set_xlabel(col)
        axes[i].set_ylabel('Frecuencia')
        axes[i].tick_params(axis='x', rotation=90) # Rotar etiquetas si es necesario
    
    # Eliminar ejes sobrantes si hay menos columnas que subplots
    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])
    
    # Ajustar diseño
    plt.tight_layout()
    plt.show()
    
def subplot_col_num(dataframe, col):
    num_graph = len(col)

    num_rows = (num_graph +2 )//2

    fig, axes = plt.subplots(num_graph, 2, figsize=(15, num_rows*5))

    for i, col in enumerate(col):
        sns.histplot(data=dataframe, x=col, ax = axes[i, 0], bins=200)
        axes[i, 0].set_title(f'Distribución de {col}')
        axes[i, 0].set_xlabel(col)
        axes[i, 0].set_ylabel('Frecuencia')
        
        sns.boxplot(data=dataframe, x=col, ax = axes[i, 1])
        axes[i, 1].set_title(f'Boxplot de {col}')
        
    for j in range(i+1, len(axes)):
        fig.delaxes(axes[j])

    plt.tight_layout()
    plt.show()
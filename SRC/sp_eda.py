import pandas as pd
import numpy as np 

def calcular_porcentaje_nulos(dataframe):   
    """
    Calcula el número y el porcentaje de valores nulos por columna en un DataFrame.

    Args:
        dataframe : pandas.DataFrame
            El DataFrame sobre el cual se desea calcular los valores nulos.

    Returns:
        tuple:
            - numero_nulos (pandas.Series): Número total de valores nulos por columna.
            - porcentaje_nulos (pandas.Series): Porcentaje de valores nulos por columna, redondeado a 2 decimales. 
    """
    numero_nulos = dataframe.isnull().sum()
    porcentaje_nulos = (dataframe.isnull().sum() / dataframe.shape[0]) * 100
    porcentaje_nulos = porcentaje_nulos.round(2)
    return numero_nulos, porcentaje_nulos

def analisis_general_cat(dataframe):
    """
    Realiza un análisis general de las columnas categóricas de un DataFrame.

    Para cada columna de tipo 'object', muestra:
    - El número de valores únicos.
    - La distribución relativa (frecuencia normalizada).
    - Estadísticas descriptivas básicas.

    Args:
        dataframe : pandas.DataFrame
            El DataFrame que contiene las columnas categóricas a analizar.

    Returns:
    None
        La función muestra los resultados en pantalla usando `print()` y `display()`.
    """
    
    col_cat = dataframe.select_dtypes(include="O").columns
    
    if len(col_cat) == 0:
        print("No hay columnas categoricas")
    
    else:
        for col in col_cat:
            print(f"La distribucion de la columna {col.upper()}")
            print(f"Esta columna tiene {len(dataframe[col].unique())} valores unicos")
            display(dataframe[col].value_counts(normalize=True))
            print("______________")
            display(dataframe[col].describe())
            print("--------------")


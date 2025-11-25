import pandas as pd 
import numpy as np 

def contar_outliers(df, columnas):
    """
    Calcula y muestra información sobre outliers en columnas numéricas de un DataFrame.

    Para cada columna indicada, identifica los outliers usando el criterio de IQR (1.5 * IQR) y muestra:
    - Nombre de la columna
    - Q1, Q3 y rango intercuartílico (IQR)
    - Límite inferior y superior
    - Cantidad de outliers
    - Porcentaje de outliers respecto al total de filas

    Args:
        df : pandas.DataFrame
            DataFrame a analizar.
        columnas : list of str
            Lista de columnas numéricas a analizar para outliers.

    Returns:
        outliers_count : dict
            Diccionario con la cantidad de outliers por columna.
        outliers_percent : dict
            Diccionario con el porcentaje de outliers por columna.
    """
    
    outliers_count = {}
    outliers_percent = {}
    outliers_info = []

    for col in columnas:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
        count = outliers.shape[0]
        percent = round(count / df.shape[0] * 100, 2)
        
        outliers_count[col] = count
        outliers_percent[col] = percent
        
        outliers_info.append({
            "Column": col,
            "Q1": Q1,
            "Q3": Q3,
            "IQR": IQR,
            "LowerBound": lower_bound,
            "UpperBound": upper_bound,
            "OutlierCount": count,
            "Outlier%": percent
        })
    
    # Mostrar tabla resumida
    display(pd.DataFrame(outliers_info))
    
    return outliers_count, outliers_percent


import pandas as pd 
import numpy as np 

def calcular_solo_col_nuls(DataFrame, umbral=10):
    """
    Calcula y muestra información sobre las columnas con valores nulos en un DataFrame.

    Para cada columna con al menos un valor nulo, muestra:
    - Nombre de la columna
    - Tipo de dato
    - Cantidad de valores nulos
    - Porcentaje de valores nulos respecto al total de filas

    Además, clasifica las columnas en dos listas:
    - Columnas con un porcentaje de nulos mayor al umbral especificado
    - Columnas con un porcentaje de nulos menor o igual al umbral

    Args:
        dataframe : pandas.DataFrame  
            El DataFrame a analizar.
        
        umbral : float, opcional (default=10)  
            Porcentaje (en valor numérico, no decimal) a partir del cual una columna se considera con "alta" cantidad de nulos.

    Returns:
        high_null_cols : list of str  
            Lista con los nombres de columnas cuyo porcentaje de nulos es mayor al umbral.

        low_null_cols : list of str  
            Lista con los nombres de columnas cuyo porcentaje de nulos es menor o igual al umbral.

    Notes:
    ------
    - Se requiere tener `pandas` y `IPython.display.display()` importados.
    - La función usa `display()` para mostrar una tabla con el resumen de nulos.
    - Las columnas sin ningún valor nulo no se incluyen en el análisis.
    """
    
    columns_with_nulls = DataFrame.columns[DataFrame.isnull().any()]
    
    null_columns_info = pd.DataFrame(
        {"Column": columns_with_nulls,
         "Datatype": [DataFrame[col].dtype for col in columns_with_nulls],
         "NullCount": [DataFrame[col].isnull().sum() for col in columns_with_nulls],
         "Null%": [((DataFrame[col].isnull().sum() / DataFrame.shape[0]) * 100) for col in columns_with_nulls]}
    )
    
    display(null_columns_info)
    high_null_cols = null_columns_info[null_columns_info['Null%'] > umbral]['Column'].tolist()
    low_null_cols = null_columns_info[null_columns_info['Null%'] <= umbral]['Column'].tolist()
    return high_null_cols, low_null_cols




    
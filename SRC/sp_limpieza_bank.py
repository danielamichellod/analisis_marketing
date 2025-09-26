import pandas as pd

def eda_preliminar(df):
    """
    Realiza un análisis exploratorio preliminar sobre un DataFrame.
    
    Muestra:
    - Una muestra aleatoria de 5 filas del DataFrame.
    - Información general del DataFrame (columnas, tipos, memoria, etc.).
    - Porcentaje de valores nulos por columna.
    - Número total de filas duplicadas.
    - Conteo de valores únicos en columnas categóricas (tipo 'object').

    Args:
    df : pandas.DataFrame
        El DataFrame sobre el cual se desea realizar el análisis exploratorio.
    
    Returns:
    None
        La función muestra los resultados directamente con `print()` y `display()`.
    """

    display(df.sample(5))
    
    print('----------------')
    
    print('INFO')
    
    display(df.info())
    
    print('----------------')
    
    print('NULOS')
    
    display(round(df.isnull().sum()/df.shape[0]*100,2))
    
    print('----------------')
    
    print('DUPLICADOS')
    
    print(df.duplicated().sum())
    
    print('----------------')
    
    print('VALUE COUNTS')
    
    for col in df.select_dtypes(include ='O').columns:
        print(df[col].value_counts())
        print('---------------------------')

def valores_minus(df):
    """
    Convierte a minúsculas todos los valores de texto en columnas categóricas (tipo object).

    Recorre todas las columnas de tipo 'object' del DataFrame y transforma 
    sus valores en minúsculas utilizando `.str.lower()`.

    Args:
    df : pandas.DataFrame
        El DataFrame que contiene las columnas a transformar.
    
    Returns:
    None
        La función modifica el DataFrame original directamente (efecto in-place).
    """
    for col in df.select_dtypes(include='O').columns:
        df[col] = df[col].str.lower()

def cambiar_coma (df, lista_col):
    """
    Reemplaza comas por puntos en columnas específicas de un DataFrame.

    Esta función es útil cuando los valores numéricos están representados 
    como cadenas con comas (",") como separador decimal, y se desea 
    convertirlas a formato compatible con Python (usando puntos ".").

    Args:
    df : pandas.DataFrame
        El DataFrame que contiene las columnas a transformar.
    lista_col : list of str
        Lista con los nombres de las columnas en las que se desea reemplazar comas por puntos.
    
    Returns:
    None
        La función modifica el DataFrame original directamente (efecto in-place).
    """
    for col in lista_col:
        df[col] = df[col].astype(str).str.replace(',', '.', regex=False)

def valor_cero (df, lista_col):
    """
    Reemplaza los valores nulos (NaN) por cero en las columnas especificadas de un DataFrame.

    Esta función es útil cuando se desea imputar con cero los valores faltantes 
    en columnas numéricas o categóricas donde el valor cero tenga sentido.

    Args:
    df : pandas.DataFrame
        El DataFrame que contiene los datos.
    lista_col : list of str
        Lista con los nombres de las columnas donde se desea reemplazar NaN por 0.
    
    Returns:
    None
        La función modifica el DataFrame original directamente (in-place).
    """
    for col in lista_col:
        df[col] = df[col].fillna(0)

def convertir_float(df, lista_col):
    """
    Convierte las columnas especificadas de un DataFrame a tipo numérico (float/int).

    Usa `pd.to_numeric()` para convertir los valores. Si hay datos no convertibles 
    (por ejemplo, texto no numérico), se transforman en NaN gracias a `errors='coerce'`.

    Args:
    df : pandas.DataFrame
        El DataFrame que contiene las columnas a convertir.
    lista_col : list of str
        Lista de nombres de columnas que se desea convertir a tipo numérico.
    
    Returns:
    None
        La función modifica el DataFrame original directamente (in-place).
    """
    for col in lista_col:
        df[col] = pd.to_numeric(df[col], errors='coerce')

def round_decimal(df, lista_col):
    """
    Redondea los valores de las columnas numéricas especificadas a 1 decimal.

    Esta función aplica `.round(1)` a cada columna en la lista dada. 
    Es útil para estandarizar el formato de salida o reducir el número de decimales.

    Args:
    df : pandas.DataFrame
        El DataFrame que contiene las columnas a redondear.
    lista_col : list of str
        Lista con los nombres de las columnas numéricas a redondear.
    
    Returns:
    None
        La función modifica el DataFrame original directamente (in-place).
    """
    for col in lista_col:
        df[col] = df[col].round(1)


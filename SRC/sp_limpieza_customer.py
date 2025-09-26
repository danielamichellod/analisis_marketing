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
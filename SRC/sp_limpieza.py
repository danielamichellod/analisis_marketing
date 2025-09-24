import pandas as pd

def eda_preliminar(df):
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
    for col in df.select_dtypes(include='O').columns:
        df[col] = df[col].str.lower()

def cambiar_coma (df, lista_col):
    for col in lista_col:
        df[col] = df[col].astype(str).str.replace(',', '.', regex=False)

def valor_cero (df, lista_col):
    for col in lista_col:
        df[col] = df[col].fillna(0)

def convertir_float(df, lista_col):
    for col in lista_col:
        df[col] = pd.to_numeric(df[col], errors='coerce')

def round_decimal(df, lista_col):
    for col in lista_col:
        df[col] = df[col].round(1)


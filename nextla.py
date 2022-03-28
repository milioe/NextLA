def describe_datos(df):
  """
  Devuelve un análisis completo de cada columna con su dtype, valores no nulos, número de valores únicos y valores únicos
  """
  unicos =[]
  for col in df:
    unicos.append(df[col].unique())
  unicos = pd.Series(unicos, index=df.columns)
  descripcion = pd.concat([df.dtypes, len(df)-df.isna().sum(),df.nunique(),unicos], axis=1)
  descripcion.columns = ['dtypes', 'not-null','nunique','unique' ]
  return(descripcion)
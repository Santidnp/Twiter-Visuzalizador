import twint
import pandas as pd
import nest_asyncio
import os



#os.chdir(r'C:/Users/sngh9/OneDrive/Escritorio/Maestria Semestre 1/Computación_IA')


def available_columns():
    return twint.output.panda.Tweets_df.columns

# Transform result to pandas
def twint_to_pandas(columns):
    return twint.output.panda.Tweets_df[columns]



def busqueda_tweets_termino(busqueda, df_path=None, min_date=None, max_date=None, geo=None, imgs=False,Limite = None,Lang = 'es'):
    # Si ya existe un dataframe, cargarlo y actualizar fecha mínima, el termino de busqueda tambien puede ser un #
    if df_path is not None:
        if os.path.isfile(df_path):
            df = pd.read_csv(df_path)
            df['date'] = pd.to_datetime(df['date'], format="%Y-%m-%d %H:%M:%S")
            if busqueda in list(df['search']):
                max_existing_date = max(df[df.search==busqueda].date)
                if min_date is not None:
                    min_date = datetime.strptime(min_date, "%Y-%m-%d %H:%M:%S")
                    min_date = max(min_date, max_existing_date)
                else:
                    min_date = max_existing_date
        else:
            print(f'Archivo no existente. Creando {df_path}')
            df = pd.DataFrame()
    else:
        df = pd.DataFrame()

    # Crear scrapper y configuarlo
    c = twint.Config()
    c.Search = busqueda
    #c.Format = "{username} |  {tweet}"
    # Para que los resultados salgan en formato pandas
    c.Pandas = True
    #c.Pandas_clean = True
    # Para que no imprima los resultados en consola
    #c.HideOutput = True
    c.Hide_output = True
    # Argumentos opcionales
    if Limite is not None:
        c.Limit = Limite
    if geo is not None:
        c.Geo = geo  # Por ejemplo: c.Geo = "4.092126,-72.955408,3400km"
    if min_date is not None:
        c.Since = str(min_date)
    if max_date is not None:
        c.Until  = str(max_date)
    
    if Lang is not None:
        c.Lang = Lang
    if imgs:
        c.Images = True
    # Correr búsqueda
    twint.run.Search(c)
    df_pd = twint_to_pandas(["id", "date", "username", "tweet", "hashtags", "nlikes", "nretweets", "link", "search"])
    df = df.append(df_pd)
    # Si se proporcionó un path, se guardan ahí los resultados. Si no, se retorna como salida el dataframe 
    if df_path is not None:
        df.to_csv(df_path, index= False)
    else:
        return df_pd

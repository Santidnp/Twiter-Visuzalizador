# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 19:03:41 2021

@author: sngh9
"""
import streamlit as st
from Procesado_tweets import *
import sys
import os
import base64
import matplotlib.pyplot as plt
#os.chdir(r'C:\Users\sngh9\OneDrive\Escritorio\Entornovirtual1')
#st.set_option('deprecation.showPyplotGlobalUse', False)

def nube_palabras2(X,idioma = 'spanish',busqueda = None):
      
  '''
  X : columna de dataframe con texto  que se quiere graficar 
  retorna : nube de palabras
  '''
  import numpy as np
  import matplotlib.pyplot as plt
  from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
  from nltk.corpus import stopwords
  import nltk
  from PIL import Image
  
  nube = np.array(Image.open("nube.png"))
  def transformacion_formato(val):
    '''
    funcion para cambiar el formato de los png
    '''
    if val == 0:
        return 255
    else:
        return val
  transformed_nube_mask = np.ndarray((nube.shape[0],nube.shape[1]), np.int32)
  for i in range(len(nube)):
      transformed_nube_mask[i] = list(map(transformacion_formato, nube[i]))
  nltk.download('stopwords')
  
  en_stops = list(stopwords.words(idioma))
  en_stops.append('https')
  en_stops.append(busqueda)

  nltk.download('stopwords')
  wd=WordCloud(max_font_size=70,
                      margin=0,stopwords=en_stops,mask=transformed_nube_mask,background_color="white")
  wd.generate(''.join(str(palabra) for palabra in X))
  plt.imshow(wd,interpolation = 'bilinear')
  plt.axis("off")
  plt.show

def get_table_download_link_csv(df):
    #csv = df.to_csv(index=False)
    csv = df.to_csv().encode()
    #b64 = base64.b64encode(csv.encode()).decode() 
    b64 = base64.b64encode(csv).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="captura.csv" target="_blank">Download csv file</a>'
    return href



#st.sidebar.markdown("## Termino a buscar ")



st.title('Visualizador de Twitter V1')
Busqueda = st.sidebar.text_input('Termino a Buscar', 'My Text')
Numero_tweets = st.sidebar.slider("Número de tweets a buscar",10,3599)
date = st.sidebar.date_input('Fecha Minima de busqueda')
date_final = st.sidebar.date_input('Fecha Maxima de busqueda')

df = busqueda_tweets_termino(Busqueda,min_date= str(date)+' 00:00:00',max_date=str(date_final)+' 11:59:59',Limite= Numero_tweets,Lang='es')


def Top_likes_fig():
    Top_likesdf = df.sort_values('nlikes',ascending=False).head(15)
    fig, ax = plt.subplots() 
    fig.autofmt_xdate(rotation=45)
    ax.bar(Top_likesdf.username,Top_likesdf.nlikes)
    ax.set_title('Usurarios con mas likes')

    return fig
    




st.dataframe(df.style.highlight_max(axis=0))
st.markdown(get_table_download_link_csv(df), unsafe_allow_html=True)
#st.markdown(get_table_download_link(df), unsafe_allow_html=True)
option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone'))

st.sidebar.write('Futuro seleccionador de idioma:', option)

#st.write(""" # Prueba """)




#st.dataframe(df, 200, 100)

#nube= nube_palabras2(df['tweet'],busqueda=Busqueda)
st.pyplot(nube_palabras2(df['tweet'],busqueda=Busqueda))
st.pyplot(Top_likes_fig())
 
 
print(date)

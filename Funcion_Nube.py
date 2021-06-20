import os
import sys
os.chdir(os.path.dirname(sys.executable))
def nube_palabras(X):
      
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
  
  en_stops = set(stopwords.words('english'))

  nltk.download('stopwords')
  wd=WordCloud(max_font_size=70,
                      margin=0,stopwords=en_stops,mask=transformed_nube_mask,background_color="white")
  wd.generate(''.join(str(palabra) for palabra in X))
  plt.imshow(wd,interpolation = 'bilinear')
  plt.axis("off")
  plt.show


def nube_palabras2(X,idioma = 'spanish'):
      
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
  
  en_stops = set(stopwords.words(idioma))

  nltk.download('stopwords')
  wd=WordCloud(max_font_size=70,
                      margin=0,stopwords=en_stops,mask=transformed_nube_mask,background_color="white")
  wd.generate(''.join(str(palabra) for palabra in X))
  plt.imshow(wd,interpolation = 'bilinear')
  plt.axis("off")
  plt.show

# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 19:55:44 2021

@author: sngh9
"""


from Nube import nube_palabras
import numpy as np
import matplotlib.pyplot as plt
import os
os.chdir(r'C:\Users\sngh9\OneDrive\Escritorio\Entornovirtual1')
nube_palabras(df['tweet'])

nube_palabras2(df['tweet'])


df2 = busqueda_tweets_termino('Dead by daylight',min_date='2021-06-10 11:59:23',max_date='2021-06-15 11:59:23',Limite= 1500)


nube_palabras2(df2['tweet'],'english')

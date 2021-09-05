import nltk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
from glob import glob
import os


def Merger(path):
    speeches = []
    years = []
    countries = []
    sessions = []
    years_cleaned = []
    
    folders = os.listdir(path)
    for root, dirs, files in os.walk(path):
        for name in files:
            if name.endswith('.txt'):
                with open(os.path.join(root, name), 'r', encoding='utf-8') as f:
                    data = f.read()
                    try:
                        speeches.append(data)
                    except:
                        speeches.append(np.nan)
                countries.append(name.split('_')[0])
                years.append(name.split('_')[-1])
                sessions.append(name.split('_')[1])
                
    for year in years:
        years_cleaned.append(year.replace('.txt', ''))
        
    dic = {
            'Year': years_cleaned,
            'Session': sessions,
            'Country': countries, 
            'Speech': speeches
            }

    df = pd.DataFrame(dic)
    return df
import pandas as pd
import numpy as np

# EXTRACION
wine_url ="https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data"
wine_data= pd.read_csv(wine_url,header=None)

wine_quality_url= "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
wine_quality_data=pd.read_csv(wine_quality_url,sep=";")

#print (wine_data.head())
#print(wine_quality_data.head())

# TRANSFORMACION
wine_data.columns=['class','alcohol','malic-acid','ash',
                   'alcalinity of ash','magnesium','total plenols',
                   'flavonoids','nonflavonoid phenols','proacthocyanidins',
                   'color intensity','hue','OD280/OD135 of diluted wines',
                   'proline']

#Coverting class
wine_data['class']=wine_data['class'].astype('category')

#checking for any 
print(wine_data.isnull().sum())

print(wine_quality_data.isnull().sum())

#normalizar 
wine_data['alcohol'] = (wine_data['alcohol'] - wine_data['alcohol'].min()) / (wine_data['alcohol'].max() - wine_data['alcohol'].min())

wine_data['alcohol'] = wine_data['alcohol'] * 1

#CREANDO UNA NUEVA COLUMNA
wine_quality_data['average_quality'] = wine_quality_data[['fixed acidity', 'volatile acidity', 'citric acid',
                                                          'residual sugar', 'chlorides', 'free sulfur dioxide',
                                                          'total sulfur dioxide', 'density', 'pH', 'sulphates',
                                                          'alcohol']].mean(axis = 1)







# cargar los datos....
wine_data.to_csv('wine_dataset',index=False)
wine_quality_data.to_csv('wine_quaily_dataset.csv',index=False)




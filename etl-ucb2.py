import pandas as pd
import numpy as np

# EXTRACION
wine_url ="population_by_country_2020.csv"
wine_data= pd.read_csv(wine_url,header=None)


print (wine_data.head())

# TRANSFORMACION

# cargar los datos....
#wine_data.to_csv('wine_dataset',index=False)

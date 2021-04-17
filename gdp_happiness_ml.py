from bs4 import BeautifulSoup
import requests
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np


# r = requests.get('https://en.wikipedia.org/wiki/World_Happiness_Report#International_rankings')
# c = r.content
# soup = BeautifulSoup(c,'html.parser')

# table = soup.find('table', class_ = 'wikitable sortable')

df = pd.read_csv('happiness_gdp.csv')

#print(df.head())

y= list(df['Score'])
x = list(df['Perceptions of corruption'])
plt.figure(figsize=(6,4))
plt.scatter(x,y)
plt.xlabel('Corruption Perception')
plt.ylabel('HAPPINESS SCORE')
plt.title('Does GDP affect Happiness')
plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)))
plt.show()

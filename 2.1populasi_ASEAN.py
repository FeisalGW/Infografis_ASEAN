import mysql.connector
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

dbku = mysql.connector .connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    passwd = '1616',
    database = 'world'
)
kursor = dbku.cursor()


querydb = """select Name, Population from country where Region = 'Southeast Asia' order by Name asc;"""
kursor.execute(querydb)
x = kursor.fetchall()
populasi_penduduk = []

for i in range (len(x)):
    populasi_penduduk.append(x[i][1])


df = pd.DataFrame(x, columns=['Negara','Populasi'])


plt.style.use ('seaborn')
plt.bar(df['Negara'],df['Populasi'], color = ['orange','blue','red','green','lightred','lightbrown','pink','grey','gold','lightblue','green'])
plt.xticks(rotation = 45)
plt.ylabel('Populasi(x100jt jiwa)')
plt.xlabel('Negara')
ax = plt.gca()
for p in ax.patches :
    ax.annotate(str(p.get_height()),(p.get_x() * 1.000, p.get_height()*1.010))
plt.show()
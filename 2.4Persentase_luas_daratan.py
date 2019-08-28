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

querydb = """select Name as Negara, SurfaceArea as LuasWilayah from country where Region = 'Southeast Asia' order by Name asc"""

kursor.execute(querydb)
x = kursor.fetchall()
df = pd.DataFrame(x, columns=['Negara','LuasWilayah'])


plt.pie(df['LuasWilayah'], labels=df['Negara'],autopct='%.1f%%')
plt.title('PERSENTASE PENDUDUK ASEAN')
plt.show()
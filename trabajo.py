#Importamos la librería pandas 
import pandas as pd 
df_datos = pd.read_csv(r"output.csv") # Leemos el archivo csv
#print(df_datos)
#Traducimos los nombres de las columnas de nuestros datasets para facilitar el trabajo

df_datos = df_datos.dropna()
df_datos = df_datos.sort_values("Year", ascending=False)

df_datos.to_csv("Nuevo_CSV.csv")
df_datos = pd.read_csv(r"Nuevo_CSV.csv")

año_1990 = 0
año_1991 = 0
año_1992 = 0
año_1993 = 0
año_1994 = 0
año_1995 = 0
año_1996 = 0
año_1997 = 0
año_1998 = 0
año_1999 = 0
año_2000 = 0
año_2001 = 0
año_2002 = 0
año_2003 = 0
año_2004 = 0
año_2005 = 0
año_2006 = 0
año_2007 = 0
año_2008 = 0
año_2009 = 0
año_2010 = 0
año_2011 = 0
año_2012 = 0
año_2013 = 0
año_2014 = 0
año_2015 = 0
año_2016 = 0
año_2017 = 0
año_2018 = 0
año_2019 = 0

for i in range (len(df_datos["Year"])): 
    if df_datos["Year"][i-1] == 1990:
        año_1990 += df_datos["Deaths"][i-1]
    elif df_datos["Year"][i] ==1991:
        año_1991 += df_datos["Deaths"][i]
    elif df_datos["Year"][i] ==1992:
        año_1992 += df_datos["Deaths"][i]
    elif df_datos["Year"][i] ==1993:
        año_1993 += df_datos["Deaths"][i]
    elif df_datos["Year"][i] ==1994:
        año_1994 += df_datos["Deaths"][i]
    elif df_datos["Year"][i] ==1995:
        año_1995 += df_datos["Deaths"][i]
    elif df_datos["Year"][i] ==1996:
        año_1996 += df_datos["Deaths"][i]
    elif df_datos["Year"][i] ==1997:
        año_1997 += df_datos["Deaths"][i]
    elif df_datos["Year"][i] ==1998:
        año_1998 += df_datos["Deaths"][i]
    elif df_datos["Year"][i] ==1999:
        año_1999 += df_datos["Deaths"][i]
    elif df_datos["Year"][i] ==2000:
        año_2000 += df_datos["Deaths"][i]
    elif df_datos["Year"][i] ==2001:
        año_2001 += df_datos["Deaths"][i]
    elif df_datos["Year"][i] ==2002:
        año_2002 += df_datos["Deaths"][i]
    elif df_datos["Year"][i] ==2003:
        año_2003 += df_datos["Deaths"][i]
    elif df_datos["Year"][i] ==2004:
        año_2004 += df_datos["Deaths"][i]
    elif df_datos["Year"][i] ==2005:
        año_2005 += df_datos["Deaths"][i]
    elif df_datos["Year"][i] ==2006:
        año_2006 += df_datos["Deaths"][i]
    elif df_datos["Year"][i] ==2007:
        año_2007 += df_datos["Deaths"][i]
    elif df_datos["Year"][i] ==2008:
        año_2008 += df_datos["Deaths"][i]
    elif df_datos["Year"][i] ==2009:
        año_2009 += df_datos["Deaths"][i]
    elif df_datos["Year"][i] ==2010:
        año_2010 += df_datos["Deaths"][i]
    elif df_datos["Year"][i] ==2011:
        año_2011 += df_datos["Deaths"][i]
    elif df_datos["Year"][i] ==2012:
        año_2012+= df_datos["Deaths"][i]
    elif df_datos["Year"][i] ==2013:
        año_2013 += df_datos["Deaths"][i]
    elif df_datos["Year"][i] ==2014:
        año_2014 += df_datos["Deaths"][i]
    elif df_datos["Year"][i] ==2015:
        año_2015 += df_datos["Deaths"][i]
    elif df_datos["Year"][i] ==2016:
        año_2016 += df_datos["Deaths"][i]
    elif df_datos["Year"][i] ==2017:
        año_2017 += df_datos["Deaths"][i]
    elif df_datos["Year"][i] ==2018:
        año_2018 += df_datos["Deaths"][i]
    elif df_datos["Year"][i] ==2019:
        año_2019 += df_datos["Deaths"][i]

muertes_año =[    año_1990,
    año_1991,
    año_1992,
    año_1993,
    año_1994,
    año_1995,
    año_1996,
    año_1997,
    año_1998,
    año_1999,
    año_2000,
    año_2001,
    año_2002,
    año_2003,
    año_2004,
    año_2005,
    año_2006,
    año_2007,
    año_2008,
    año_2009,
    año_2010,
    año_2011,
    año_2012,
    año_2013,
    año_2014,
    año_2015,
    año_2016,
    año_2017,
    año_2018,
    año_2019]
años =[1990,
    1991, 
    1992, 
    1993, 
    1994, 
    1995, 
    1996, 
    1997, 
    1998, 
    1999, 
    2000, 
    2001, 
    2002, 
    2003, 
    2004, 
    2005, 
    2006, 
    2007, 
    2008, 
    2009, 
    2010, 
    2011, 
    2012, 
    2013, 
    2014, 
    2015, 
    2016, 
    2017, 
    2018, 
    2019 ]
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('darkgrid')
plt.xticks(rotation=90)

x = años
y = muertes_año

sns.barplot(x, y)
plt.savefig('diagrama-barras-muertes-años.png')
plt.show()
#for i in range (len(df_datos["Year"])):
#  print(df_datos["Year"][i])

valores = muertes_año
nombres =años
colores = ["#55CBCD","#FFDAC1","#FFB5E8"]
plt.pie(valores, labels=nombres, autopct="%0.1f %%", colors=colores)
plt.savefig('diagrama-sectores.png')
plt.show()

print(muertes_año)



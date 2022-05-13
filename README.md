# Trabajo-final

## FASE 0:

Para entregr nuestro trabajo hemos creado un repositorio en GitHub con la siguiente dirección: https://github.com/acasasaez/Trabajo-final.git

Para el trabajo final de Estructura de datos y algoritmos 1 se nos pedía elegir un dataset para analizar sus datos y finalmente terminar elaborando una web con los mismos.

Nuestro grupo de trabajo ha elegido el siguiente tema "Muertes por accidente de tráfico de 1990 a 2019". 

Nuestro dataset contiene los siguientes datos: 
  
  1)Los países
  
  2)El año 
  
  3)Los fallecidos por año por esta causa
  
  4)El sentido de conducción (si se conduce por carril derecho o izquierdo) 
 
Por lo tanto, nuestro trabajo consistirá en estudiar cómo han fluctuado las muertes por accidente de tráfico en los distintos países y lanzar pequeñas hipótesis de por qué han variado de este modo. 

El motivo por el que hemos elegido este tema es que creemos importante concienciar a la sociedad de la gran cantidad de accidententes mortales de tráfico. También, nos gustaría que una vez estudiados los datos seamos capaces de quizás plantear alguna pequeña solución al problema.


## FASE 1:
Este es el figma de la  fase 1
https://www.figma.com/proto/tdUlObQZ2jRCbjouVwrEio/app-cars-(Community)?node-id=2%3A4&scaling=scale-down&page-id=0%3A1&starting-point-node-id=2%3A4&show-proto-sidebar=1

## FASE 2
```
#Importamos la librería pandas 
import pandas as pd 
import numpy as np 
df_datos = pd.read_csv(r"output.csv") 
# Leemos el archivo csv
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
    if df_datos["Year"][i] == 1990:
        año_1990 += df_datos["Deaths"][i]
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

media_muertes = np.mean(df_datos["Deaths"])
print(muertes_año)
print("La media anual de muertes es: ", media_muertes)

```
Grárico sectores Muerte/ Año

![diagrama-sectores](https://user-images.githubusercontent.com/91721826/168242713-6b620b8a-2fe7-47c2-83ec-375e9a0129cf.png)

Gráfico barras Muerte/Año

![diagrama-barras-muertes-años](https://user-images.githubusercontent.com/91721826/168242822-8fac4410-aab9-4fd1-943b-dd106ff3e4b1.png)


## FASE 3
https://pineapple-tide-breath.glitch.me/
```
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <link
      href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css"
      rel="stylesheet"
      integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3"
      crossorigin="anonymous"
    />
    <link
      rel="icon"
      href="https://fonts.googleapis.com/css?family=Fjalla+One|Noto&display=swap"
      rel="stylesheet"
    />

    <title>Hello world!</title>

    <!-- import the webpage's stylesheet -->
    <link rel="stylesheet" href="/style.css" />
  </head>
  <body>
    <header>
      <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <a class="navbar-brand" href="#">LOGO</a>
        <ul class="nav">
          <li class="nav-item active">
            <a class="nav-link" href="#">Inicio<span class="re-only"></span></a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Ubicación</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Sobre nosotros</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#"> Contacto </a>
          </li>
        </ul>
      </nav>
      <div
        class="cover d-flex justify-content-center align-items-center flex-column"
      >
        <h1>MyA</h1>

        <p>Viaja seguro</p>
        <button class="btn btn-dark">Conoce Más</button>
      </div>
    </header>
    <section>
      <div class="row justify-content-center">
        <div class="col-9 col-sm">
          <div class="container mt-5 mb-5">
            <div class="card" ç>
              <img
                src="https://cdn.glitch.global/c0947262-9e6d-4821-b14f-9d336da6cf5f/thumbnails%2Fdiagrama-barras-muertes-a%C3%B1os.png?1652400198893"
                class="card-img-top"
                alt="..."
              />
              <div class="card-body">
                <h5 class="card-title">¿Tranquildad al volante?</h5>
                <p class="card-text">
                  Las estadísticas no fallan y es innegable el peligro que
                  corremos cada vez que salimos a la carretera.
                </p>
              </div>
            </div>
          </div>
        </div>
        <div class="col-9 col-sm-6 col-lg-5 ">
          <div class="container mt-5 mb-5">
            <div class="card">
              <img
                src="https://cdn.glitch.global/c0947262-9e6d-4821-b14f-9d336da6cf5f/thumbnails%2Fdiagrama-sectores.png?1652400815352"
                class="card-img-top"
                alt="..."
              />
              <div class="card-body">
                <h5 class="card-title">¿Por qué nosotros?</h5>
                <p class="card-text">
                  En MyA contamos con una amplia plantilla de analistas
                  especializados que se encargan de estudiar cuál es el plan de
                  seguro que más le conviene a cada prototipo de conductor.
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    <section>
      <div class="container mt-5 mb-5">
        <div class ="row">
          <div class="col-9 col-sm-6 col-lg-5 ">
          <img src ="https://cdn.glitch.global/c0947262-9e6d-4821-b14f-9d336da6cf5f/IMG-7413.JPG?v=1652425233630"/>
        </div>
        <div class="col-9 col-sm-6 col-lg-5 ">
          <p>
          <h3>
            Inicia tu viaje de la manera más segura
          </h3>
          </p>
          <p>
            Deje su correo electrónico y contactaremos con usted 
          </p>
          </div>
          </div>
        <form action="">
          <label for="email">Correo electrónico:</label>

          <div class="d-flex flex-file mr-2">
            <div class="fore-group">
             

              <input type="email" id="email" class="fore-control" />
            </div>
            <button type="submit" class="btn btn-primary">Enviar</button>
          </div>
        </form>
      </div>
    </section>
  </body>
</html>
```

```



body {
  margin: 1rem;
  font-family: sans-serif;
  line-height: 1.5;}



.cover{height: 400px;
  color:orange;
background-image:url(https://cdn.glitch.global/c0947262-9e6d-4821-b14f-9d336da6cf5f/imagen.jpg?v=1652398537432);
background-size:cover;
background-position: center;
background-color:rgba(0,0,0,0.5);
background-blend-mode:darken}

.card {border: 0! important;
box-shadow:0 4px 6 px -1px(0,0,0,0.1), 0 2px 4px -1px rgba(0,0,0,0.06)}


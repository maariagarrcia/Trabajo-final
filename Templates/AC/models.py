from django import models 

class Coche (models.Model):
    codigo = models.Charfield(max_length =3, primary_key = True) 
    nombre =models.Charfield(max_length =45)
    numeros_matricula =models.PositiveSmallIntergerfield(default =10)
    letras_matricula =models.Charfield(max_length =45)

class cliente(models.Model):
    numero_dni =models.PositiveSmallIntergerfield(default =8, primary_key = True)
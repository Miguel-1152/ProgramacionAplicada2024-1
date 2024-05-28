# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1FENegezFiyDaAWMPPSzKHsVnniSRZKPd
"""

# PUNTO 1
from google.colab import drive
import pandas as pd
drive.mount('/content/drive')
file_path = '/content/drive/My Drive/ABC - Sales.csv'
ventas = pd.read_csv(file_path)

# PUNTO 2
ventas.head(12)

# PUNTO 3
ventas.tail(15)

# PUNTO 4
StoreLoc = ventas['store_location']
print (StoreLoc)

# PUNTO 5
IdComprador = ventas['cust_id']
print (IdComprador)

# PUNTO 6
IdVenta = ventas['sale_id']
print (IdVenta)

# PUNTO 7
StoreLoc_1=StoreLoc.sort_values(ascending=False)
print (StoreLoc_1)

# PUNTO 8
Idcomprador_1=IdComprador.sort_values(ascending=False)
print(Idcomprador_1)

# PUNTO 9
IdVenta_1=IdVenta.sort_values(ascending=False)
print(IdVenta_1)

# PUNTO 10
nombres_columnas = ['product', 'qty', 'store_location']
columnas = ventas[nombres_columnas]
print (columnas)

# PUNTO 11
valores_nulos = ventas.isnull().sum()
print(valores_nulos)

# PUNTO 12
productos_vendidos = ventas.groupby('product')['qty'].sum()
print(productos_vendidos)

# PUNTO 13
ventas.groupby('prod_id')['qty'].sum()

# PUNTO 14
ventas.sort_values(by='prod_id')

# PUNTO 15
ventas.sort_values(by='cust_id')

# PUNTO 16
ventas.sort_values(by=['cust_id', 'prod_id'])

# PUNTO 17
ventas.sort_index(ascending=False)

# PUNTO 18
ventasOptimizado = ventas.drop_duplicates()
ventasOptimizado

# PUNTO 19
mi_lista = [164, 220, 340, 452, 578]
mi_serie = pd.Series(mi_lista)
mi_serie

# PUNTO 20
datos = {
    'Nombre': ['Juan', 'Camilo', 'Miguel', 'Kevin'],
    'Edad': [48, 13, 35, 21],
    'Profesión': ['Futbolista', 'Estudiante', 'Ingeniero', 'Vendedor']
}
Dataframe = pd.DataFrame(datos)

print(Dataframe)

# PUNTO 18
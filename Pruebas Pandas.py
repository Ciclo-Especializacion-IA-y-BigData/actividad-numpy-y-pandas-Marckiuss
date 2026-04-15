from operator import index
import pandas as pd
import numpy as np

mydataset = {"cars": ["BMW", "Volvo", "Ford"], "passings": [3, 7, 2]}

midataset = pd.DataFrame(mydataset)
print("**imprime el DataFrame entero**")
print(midataset)
print(" ")
print("Versión panda: ", pd.__version__)
print(" ")
print("______")

a = [1, 2, 3]
miSeries = pd.Series(a)
miSeries2 = pd.Series(a, index = ["a","b","c"]) 

print("**imprime el valor de la posición indicada del array**")
print(miSeries[1])
print(" ")
print("**imprime el valor de la serie a partir del índice indicado**")
print(miSeries2["b"])
print(" ")
print("__________")
print(" ")

data = {
  "AI Model": ["Regresión lineal", "Regresión lógica", "Clasificación"],
  "Accuracy": [0.82, 0.8, 0.7]
}

midataframe = pd.DataFrame(data,index = ["a","b","c"])
print("modelos de IA y su precisión")
print(" ")
print(midataframe)

print("")
print("Práctica 1")
print("")

AIModels = {
    "AI Model": ["Regresión Lineal", "Regresión Lógica", "Red Neuronal"],
    "Accuracy": [0.82, 0.8, 0.96]
}

AIModelsDataFrame = pd.DataFrame(AIModels,index = ["a","b","c"])


AIModelsFiltro = AIModelsDataFrame[AIModelsDataFrame["Accuracy"] > 0.85]
print(AIModelsFiltro)




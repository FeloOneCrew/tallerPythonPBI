from generators.generadorDatosApple import generarDatosApple
import pandas as pd

def analizarDatosApple():
    datos= generarDatosApple()
    tabla=pd.DataFrame(datos,columns=["Tipo Producto","categoria"])
    tabla.to_csv("./data/DatosProductosApple.csv",index=False)
analizarDatosApple()
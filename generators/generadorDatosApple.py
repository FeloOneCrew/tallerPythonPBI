import random

def generarDatosApple():
    Productos = ["Música","TV","Aplicaciones","PC","Celulares","Tablets", "Accesorios"]
    datos =[]
    for Producto in Productos:
        dataApple = {}
        categoria = random.choice(["Plus", "Mega", "Basic"])
        ProductoApple = [Producto,categoria]
        datos.append(ProductoApple)
    
    return datos

print(generarDatosApple())
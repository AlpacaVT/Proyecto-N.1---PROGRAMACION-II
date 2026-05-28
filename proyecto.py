# -------------------------------------
# -------------------------------------
#  ------PROYECTO DE PROMACION--------
#  --INTEGRANTES: Vicente Huilcaman--
# ------------------------------------
# ------------------------------------

import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import os
import numpy as np

# ------------------------------------
# Muestra el nombre de los archivos que se encuentran en el directorio
# ------------------------------------
def buscar_archivos():
    archivos = []

    for archivo in os.listdir():
        if archivo.endswith(".npy"):
            archivos.append(archivo)

    return archivos

# ------------------------------------
# Carga un archivo.np ingresado como parametro
# ------------------------------------
def cargar_senal(nombre_archivo):
    senal = np.load(nombre_archivo)
    return senal.tolist()

# ------------------------------------
# Filtra los datos de una señal para devolverla como una señal media movil
# ------------------------------------
def pasar_a_media_movil(señal):
    señal_media_movil = []
    for i in range(len(señal)):
        if i-7 < 0:
            promedio = señal[0]
        elif i+7 > len(señal) - 1:
            promedio = señal[-1]
        else:
            promedio = (señal[i-3] + señal[i-2] + señal[i-1] + señal[i] + señal[i+1] + señal[i+2] + señal[i+3])/7
        señal_media_movil.append(promedio)
    return señal_media_movil

# ------------------------------------
# Filtra los datos de una señal para devolverla como una señal mediana movil
# ------------------------------------
def pasar_a_mediana_movil(señal):
    señal_mediana = []
    radio = 3 
    
    for i in range(len(señal)):
        inicio = max(0, i - radio)
        fin = min(len(señal), i + radio + 1)
        
        temp = sorted(señal[inicio:fin])
        
        señal_mediana.append(temp[3])
        
    return señal_mediana

# ------------------------------------
# Analiza una señal y devuelve la desviacion estandar de esta
# ------------------------------------
def desviacion_estandar(señal):
    promedio = sum(señal) / len(señal)
    desviacion_estandar = []
    for i in señal:
        i -= promedio
        desviacion_estandar.append(i**2)
    prom_desv = sum(desviacion_estandar) / len(desviacion_estandar)
    prom_desv = prom_desv**0.5
    return prom_desv


# ------------------------------------
# Funciones de botones
# ------------------------------------

# Dibuja la señal original
def mostrar_señal(event):

    linea.set_ydata(y)

    linea.set_label("Señal Original")
    texto_box.set_text("Señal original")
    ax.legend()

    plt.draw()

# Dibuja la señal media movil
def mostrar_media(event):

    linea.set_ydata(pasar_a_media_movil(y))

    linea.set_label("Señal filtrada")
    texto_box.set_text("Filtro Media Movil")
    ax.legend()

    plt.draw()

#Dibuja la señal mediana movil
def mostrar_mediana(event):

    linea.set_ydata(pasar_a_mediana_movil(y))

    linea.set_label("Señal Filtrada")
    texto_box.set_text("Filtro Mediana Movil")
    ax.legend()

    plt.draw()

# Muestra las estadisticas de la señal dibujada
def estadisticas(event):
    maximo = max(linea.get_ydata())
    minimo = min(linea.get_ydata())
    promedio = sum(linea.get_ydata())/len(linea.get_ydata())   
    texto_box.set_text(f"ESTADISTICAS\n\nValor maximo: {maximo}\nValor minimo: {minimo}\nPromedio: {promedio}\nDesviacion Estandar: {desviacion_estandar(linea.get_ydata())}")
    plt.draw()
    
# ------------------------------------
# Muestra todos los Archivos enumerados en la terminal
# ------------------------------------
archivos_npy = (buscar_archivos())
for i in range(1, len(archivos_npy) + 1):
    print(f"{i}. {archivos_npy[i-1]}")

#Seleccion del Usuario sobre que archivo cargar
Seleccion = int(input("Selecciona el archivo que quieres cargar: "))

print(f"Se ha seleccionado el archivo {archivos_npy[Seleccion-1]}")
y = cargar_senal(archivos_npy[Seleccion-1])

#asigna la cantidad de valores que se ordenaran en x respecto a los de y
x = []
for i in range(len(y)):
    x.append(i)

fig, ax = plt.subplots()

# espacio para botones
plt.subplots_adjust(bottom=0.25)

# muestra la señal original
linea, = ax.plot(x, y)
ax.set_title("Señal")
ax.set_ylabel("Amplitud")
ax.grid()

# ------------------------------------
# Crear botones
# ------------------------------------
ax_btn1 = plt.axes([0.05, 0.05, 0.2, 0.08])
ax_btn2 = plt.axes([0.28, 0.05, 0.2, 0.08])
ax_btn3 = plt.axes([0.51, 0.05, 0.2, 0.08])
ax_btn4 = plt.axes([0.74, 0.05, 0.2, 0.08])

btn_O = Button(ax_btn1, "Señal original")
btn_media = Button(ax_btn2, "Filtro media movil")
btn_mediana = Button(ax_btn3, "Filtro mediana movil")
btn_estadisticas = Button(ax_btn4, "Estadisticas")

#Cambios de eventos segun el boton presionado
btn_O.on_clicked(mostrar_señal)
btn_media.on_clicked(mostrar_media)
btn_mediana.on_clicked(mostrar_mediana)
btn_estadisticas.on_clicked(estadisticas)
texto_box = ax.text(
        0.02,
        0.95,
        "",
        transform=ax.transAxes,
        verticalalignment="top",
        bbox=dict(boxstyle="round", facecolor="white", alpha=0.9)
    )

plt.show()









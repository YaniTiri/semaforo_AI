import cv2
import os
import random
import numpy as np

def capturarFotos(num_fotos, carpeta_destino):
    #ruta carpeta imagenes:
    os.makedirs(carpeta_destino, exist_ok=True)

    #inicializar la webcam para capturar 
    camara = cv2.VideoCapture(0) 

    #setear tamaño de foto
    camara.set(cv2.CAP_PROP_FRAME_WIDTH,640)
    camara.set(cv2.CAP_PROP_FRAME_HEIGHT,360)

    for i in range(1, num_fotos +1):
       
        #capturar imagen con la webcam
        ret, frame = camara.read() #hace que la variable de la imagen pase a ser frame

        if not ret:
            print("Error al capturar la imagen")
            break
        
        #mostrar foto
        cv2.imshow("foto", frame)
        cv2.waitKey(0)
        print("Imagen ", i, ":")
        catalogarColores(frame)
        
        #guardar foto
        imagenNombre="foto"+str(i)+".jpg"
        imagen2_ruta=os.path.join(carpeta_destino, imagenNombre)
        cv2.imwrite(imagen2_ruta, frame)
       
        cv2.destroyAllWindows()
    camara.release()
    cv2.destroyAllWindows()

def catalogarColores(img):

    ##############################
    #rangos para detectar colores:
    ##############################
    #rojo
    bajo_rojo= np.array([0,0,100])
    alto_rojo= np.array([100,100,255])
    #amarillo
    #bajo_amarillo= np.array([0,150,220])
    #alto_amarillo=np.array([90,200,255])
    bajo_amarillo= np.array([0,200,200])
    alto_amarillo=np.array([50,255,255])
    #verde
    bajo_verde= np.array([0,170,0])
    alto_verde=np.array([100,255,100])
    #bajo_verde= np.array([0,100,0])
    #alto_verde=np.array([100,255,100])
    ##############################
   

    #detectar mascaras de color:
    mascara_rojo= cv2.inRange(img, bajo_rojo, alto_rojo)
    mascara_amarillo= cv2.inRange(img, bajo_amarillo, alto_amarillo)
    mascara_verde=cv2.inRange(img, bajo_verde, alto_verde)

    #mascaras segun cantidad de pixeles para evitar errores
    cant_pix_rojo=np.sum(mascara_rojo == 255)
    cant_pix_amarillo=np.sum(mascara_amarillo == 255)
    cant_pix_verde=np.sum(mascara_verde == 255)
    
    pixeles_colores = [
        ("El color es ROJO", cant_pix_rojo),
        ("El color es AMARILLO", cant_pix_amarillo),
        ("El color es VERDE", cant_pix_verde)
    ]
    # Ordenar la lista en base a la cantidad de píxeles (segundo valor de cada tupla)
    pixeles_colores_ordenados = sorted(pixeles_colores, key=lambda x: x[1], reverse=True)
    
    print(pixeles_colores_ordenados[0][0])
                



# Llamar a la función para capturar y guardar fotos

directorio= 'capturas'
capturarFotos(10, directorio)

import cv2
import os
import random
import numpy as np

#ruta carpeta imagenes:
carpeta= 'img'

#obtener archivos de la ruta carpeta
archivos= os.listdir(carpeta)

#filtrar solo archivos de fotos segun extensiones de imagen
imagenes= [archivo for archivo in archivos if archivo.endswith(('.png', '.jpg', '.jpeg'))]

#print(imagenes)

##############################
#rangos para detectar colores:
##############################
#rojo
bajo_rojo= np.array([0,0,100])
alto_rojo= np.array([100,100,255])
#amarillo
bajo_amarillo= np.array([0,150,220])
alto_amarillo=np.array([90,200,255])
#bajo_amarillo= np.array([0,200,200])
#alto_amarillo=np.array([50,255,255])
#verde
bajo_verde= np.array([0,170,0])
alto_verde=np.array([100,255,100])
#bajo_verde= np.array([0,100,0])
#alto_verde=np.array([100,255,100])
##############################
contador=0

if len(imagenes)== 0:
    print("No se encontró ninguna imagen en la carpeta")
else:
    #BUCLE para que haga 5 veces:
    while contador < 5:
        contador+=1
        
        #aleatoriedad de la imagen:
        imagenRandom= random.choice(imagenes)

        #leer imagen
        imagen_ruta=os.path.join(carpeta, imagenRandom)
        img=cv2.imread(imagen_ruta)

        #mostrar imagen si carga correctamente
        if img is not None:


            #detectar mascaras de color:
            mascara_rojo= cv2.inRange(img, bajo_rojo, alto_rojo)
            mascara_amarillo= cv2.inRange(img, bajo_amarillo, alto_amarillo)
            mascara_verde=cv2.inRange(img, bajo_verde, alto_verde)

            #semaforo_rojo = np.any(mascara_rojo > 0)
            #semaforo_amarillo = np.any(mascara_amarillo > 0)
            #semaforo_verde = np.any(mascara_verde > 0)

            #mascaras segun cantidad de pixeles para evitar errores
            cant_pix_rojo=np.sum(mascara_rojo == 255)
            cant_pix_amarillo=np.sum(mascara_amarillo == 255)
            cant_pix_verde=np.sum(mascara_verde == 255)

            cv2.imshow('Imagen aleatoria', img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

            #print("rojo: ",cant_pix_rojo)
            #print("amarillo: ", cant_pix_amarillo)
            #print("verde: ", cant_pix_verde) 




            if cant_pix_rojo > 500:
                print("El semáforo está en ROJO - ¡Detenerse!")

                #para ver la mascara del color:            
                cv2.imshow('Mascara color rojo', mascara_rojo)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

            elif cant_pix_amarillo>500:
                print("El semáforo está en AMARILLO - ¡Atención!")

                #para ver la mascara del color:
                cv2.imshow('Mascara color amarillo', mascara_amarillo)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

            elif cant_pix_verde>500:
                print("El semaforo está en VERDE - ¡Avanzar!")

                #para ver la mascara del color:
                cv2.imshow('Mascara color verde', mascara_verde)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

            else:
                print("El semáforo está ROTO???")
        else:
            print("No se pudo cargar la imagen")




# Detección de COLORES del Semáforo

Este repositorio contiene dos ejercicios relacionados con la detección de imágenes y el análisis de colores. El primero se enfoca en mostrar imágenes de semáforos de forma aleatoria desde una carpeta local. El segundo utiliza la webcam para capturar fotos y luego analizar los colores predominantes en cada imagen (rojo, amarillo y verde) para detectar los colores de un semáforo.

## Ejercicio 1: Detección Aleatoria de Imágenes de Semáforos

### Descripción

El primer ejercicio consiste en seleccionar y mostrar aleatoriamente imágenes de semáforos desde una carpeta local. Estas imágenes pueden ser de semáforos en diferentes estados (rojo, amarillo o verde).

### Características principales

1. Las imágenes son cargadas automáticamente desde una carpeta específica en el directorio local.
2. El script selecciona y muestra una imagen de manera aleatoria utilizando la biblioteca OpenCV (`cv2`).
3. La selección aleatoria se realiza iterando sobre todas las imágenes disponibles en la carpeta.

## Ejercicio 2: Detección de Colores de Semáforos en Fotos Tomadas con la Webcam

### Descripción

El segundo ejercicio captura 5 fotos utilizando la webcam y analiza la presencia de colores predominantes (rojo, amarillo y verde) en cada imagen. El objetivo es simular la detección de los colores de un semáforo para determinar cuál es el color predominante en la imagen capturada.

### Características principales

1. Toma 5 fotos con la webcam y las guarda en una carpeta local.
2. Analiza los colores predominantes en las imágenes para detectar rojo, amarillo y verde.
3. Utiliza la función `cv2.inRange` para crear máscaras de color y detectar la cantidad de píxeles que corresponden a cada color.
4. Los resultados muestran cuál color (rojo, amarillo o verde) predomina en cada imagen.

### Instrucciones de uso

1. Asegúrate de que tu webcam esté conectada y funcionando.
2. Ejecuta el script para capturar 5 fotos y guardarlas en una carpeta.
3. El código analizará las fotos y determinará qué color predomina en cada una.

## Requisitos

- **Python** 3.x
- **Bibliotecas**:
  - `opencv-python`
  - `numpy`

Para instalar las dependencias, puedes ejecutar:

```bash
pip install opencv-python numpy


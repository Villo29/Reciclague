import tensorflow as tf
import numpy as np
import cv2

def preprocesar_imagen(imagen):
    if imagen is None or imagen.size == 0:
        raise ValueError("La imagen pasada al preprocesamiento esta vacai o tiene tamamo 0.")

    imagen = cv2.resize(imagen, (300, 300))
    imagen = np.expand_dims(imagen, axis=0)
    imagen = imagen.astype(np.float32)
    imagen /= 255.0
    return imagen

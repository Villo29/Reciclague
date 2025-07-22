import tensorflow as tf
import numpy as np

def cargar_modelo():

    interpreter = tf.lite.Interpreter(model_path="/home/pi/Desktop/Recicla.ia/modelos/model.tflite")
    interpreter.allocate_tensors()
    return interpreter

def predecir_residuo(interpreter, imagen):
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    interpreter.set_tensor(input_details[0]['index'], imagen)
    interpreter.invoke()

    output_data = interpreter.get_tensor(output_details[0]['index'])
    prediccion = np.argmax(output_data, axis=1)

    with open("/home/pi/Desktop/Recicla.ia/modelos/labels.txt", "r") as f:
        class_labels = f.read().splitlines()

    tipo_residuo = class_labels[prediccion[0]]
    return tipo_residuo
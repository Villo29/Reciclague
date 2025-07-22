from procesamiento_imagen.procesamiento import preprocesar_imagen
from modelo.modelo_tflite import cargar_modelo, predecir_residuo
from leds_servos.leds_servos import configurar_pines, mover_servo, limpiar_gpio
import cv2
import time

def detectar_movimiento():

    configurar_pines()
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: No se pudo acceder a la camara.")
        return

    interpreter = cargar_modelo()

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error al capturar la imagen.")
            continue

        if frame is None or frame.size == 0:
            print("Error: La imagen capturada esta vacia o tiene tamano 0.")
            continue

        cv2.imshow("Deteccion de Movimiento", frame)

        tecla = cv2.waitKey(1) & 0xFF
        if tecla == 32:
            print("Capturando imagen!")

            try:
                if frame is None or frame.size == 0:
                    raise ValueError("La imagen capturada esta vacia o no tiene tamano valido.")

                imagen_preprocesada = preprocesar_imagen(frame)
                tipo_residuo = predecir_residuo(interpreter, imagen_preprocesada)

                print(f"Tipo de residuo detectado: {tipo_residuo}")

                mover_servo(tipo_residuo)

            except Exception as e:
                print(f"Error durante el preprocesamiento o prediccin: {e}")

        if tecla == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    limpiar_gpio()

if __name__ == "__main__":
    detectar_movimiento()
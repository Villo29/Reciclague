import RPi.GPIO as GPIO
import time


SERVO_ROJO_PIN = 18
SERVO_VERDE_PIN = 23

def configurar_pines():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SERVO_ROJO_PIN, GPIO.OUT)
    GPIO.setup(SERVO_VERDE_PIN, GPIO.OUT)

    global servo_rojo, servo_verde
    servo_rojo = GPIO.PWM(SERVO_ROJO_PIN, 50)
    servo_verde = GPIO.PWM(SERVO_VERDE_PIN, 50)
    servo_rojo.start(0)
    servo_verde.start(0)

def mover_servo(categoria):
    if categoria == "pet":
        print("Abriendo tapa para PET")
        servo_rojo.ChangeDutyCycle(7)  # Abrir tapa (90 grados)
        time.sleep(1)
        servo_rojo.ChangeDutyCycle(0)
        time.sleep(15)
        print("Cerrando tapa para PET")
        servo_rojo.ChangeDutyCycle(2)
        time.sleep(1)
        servo_rojo.ChangeDutyCycle(0)
    elif categoria == "unicel":
        print("Abriendo tapa para Unicel")
        servo_verde.ChangeDutyCycle(7)  # Abrir tapa (90 grados)
        time.sleep(1)
        servo_verde.ChangeDutyCycle(0)
        time.sleep(15)
        print("Cerrando tapa para Unicel")
        servo_verde.ChangeDutyCycle(2)
        time.sleep(1)
        servo_verde.ChangeDutyCycle(0)


def limpiar_gpio():
    servo_rojo.stop()
    servo_verde.stop()
    GPIO.cleanup()

from machine import Pin
import time

# Variables globales
counter = 0
button_pressed = False
last_A = 1
last_B = 1

# Gestion du signal A (front)
def callback_A(pin):
    global counter, last_A, last_B
    a = pin.value()
    b = pin_B.value()
    if a != last_A:  # Changement détecté
        if b != a:
            counter += 1
        else:
            counter -= 1
        print("Position :", counter)
    last_A = a

# Gestion du bouton poussoir
def callback_button(pin):
    global button_pressed
    if pin.value() == 0:  # Appui détecté (actif bas)
        if not button_pressed:
            print("Bouton appuyé !")
            button_pressed = True
    else:
        button_pressed = False

# Configuration des pins
pin_A = Pin(14, Pin.IN, Pin.PULL_UP)
pin_B = Pin(27, Pin.IN, Pin.PULL_UP)
button = Pin(26, Pin.IN, Pin.PULL_UP)

# Attacher les interruptions
pin_A.irq(trigger=Pin.IRQ_RISING | Pin.IRQ_FALLING, handler=callback_A)
button.irq(trigger=Pin.IRQ_FALLING | Pin.IRQ_RISING, handler=callback_button)

# Boucle passive
while True:
    time.sleep_ms(50)  # Pour laisser la place aux interruptions

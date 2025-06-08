# main.py - Configuración principal
from ursina import *
from math import sin, pi
import time as tm
from elementos.juego import MiJuego
from elementos.menu import Menu

# Variables globales de estado
en_pausa = False
juego = None
menu = None


def input(key):
    global en_pausa
    
    if key == '1':
        en_pausa = not en_pausa
        menu.mostrar() if en_pausa else menu.ocultar()
        return
    
    # Pasar todos los inputs al juego
    juego.input(key)
    
    if not en_pausa:
        juego.manejar_input_jugador(key)

app = Ursina(
    title='Mi viaje a la UES v1',
    size=(1280, 720),
    fullscreen=False,
    vsync=True
)


# Configuración inicial
window.fullscreen = False


AmbientLight(color=color.rgba(200, 200, 200, 0.9))

sun_light = DirectionalLight()
sun_light.look_at(Vec3(1, -1, 1))
sun_light.shadow_resolution = (1024, 1024)
sun_light.shadows = True

spotlight = PointLight(parent=camera, color=color.white, shadows=True)
spotlight.position = (0, 5, 8)
spotlight.look_at((0, 0, 5))
spotlight.radius = 10
spotlight.intensity = 2


juego = MiJuego()
menu = Menu(juego)

mouse.locked = True
mouse.visible = False

Sky() # Cielo por defecto

app.run()
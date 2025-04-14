# main.py - Configuración principal
from ursina import *
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
    title='Juego FPS Interactivo',
    size=(1280, 720),
    fullscreen=False,
    vsync=True
)

juego = MiJuego()
menu = Menu(juego)

mouse.locked = True
mouse.visible = False

app.run()
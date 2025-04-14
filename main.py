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

class DayNightConfig:
    CYCLE_DURATION = 300       # 5 minutos (300 segundos)
    DAY_COLOR = color.rgb(200, 220, 255)     # Luz diurna azulada
    NIGHT_COLOR = color.rgb(30, 30, 60)      # Luz nocturna
    SUNRISE_COLOR = color.rgb(255, 140, 0)   # Naranja atardecer
    START_TIME = tm.time()


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
scene.fog_density = 0.03
scene.fog_color = color.gray

# Sistema de iluminación
sun = DirectionalLight()
sun.look_at(Vec3(1, -1, 0))

# Cielo con textura estándar de Ursina
sky = Sky(texture='sky_sunset')


def update():
    # Cálculo del tiempo transcurrido
    elapsed = tm.time() - DayNightConfig.START_TIME
    cycle_progress = (elapsed % DayNightConfig.CYCLE_DURATION) / DayNightConfig.CYCLE_DURATION
    
    # Movimiento solar y rotación del cielo
    sun_angle = cycle_progress * 360
    sun.rotation_y = sun_angle
    sun.rotation_x = 30 + 60 * sin(cycle_progress * pi)
    sky.rotation_y = sun_angle  # El cielo gira con el sol
    
    # Intensidad luminica base
    light_intensity = sin(cycle_progress * pi)
    
    # Iluminación ambiental
    scene.ambient_color = lerp(
        DayNightConfig.NIGHT_COLOR,
        DayNightConfig.DAY_COLOR,
        light_intensity
    )
    
    # Efectos de atardecer/amanecer
    if 0.2 < cycle_progress < 0.3 or 0.7 < cycle_progress < 0.8:
        sun.color = DayNightConfig.SUNRISE_COLOR
        scene.fog_color = lerp(color.gray, DayNightConfig.SUNRISE_COLOR, 0.5)
    else:
        sun.color = lerp(
            DayNightConfig.NIGHT_COLOR,
            DayNightConfig.DAY_COLOR,
            light_intensity
        )
        scene.fog_color = lerp(color.dark_gray, color.light_gray, light_intensity)
    
    # Intensidad de niebla dinámica
    scene.fog_density = 0.01 + (0.06 * (1 - light_intensity))



juego = MiJuego()
menu = Menu(juego)

mouse.locked = True
mouse.visible = False

app.run()
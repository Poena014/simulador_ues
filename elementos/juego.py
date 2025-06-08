from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import os

from .textoemergente import TextPopup
from .minimapa import Minimap
from .escena1 import cargar_escena

class MiJuego(Entity):
    def __init__(self):
        super().__init__()
        self.jugador = None
        self.popup = None

        self.instrucciones = Text(
            text="Presiona 1 para ver el menú\nClick derecho para ver mensaje\nUsa + y - para zoom de cámara",
            origin=(-.5, .5),
            position=(0.4, 0.45),  # Derecha
            scale=1.2,
            background=True
        )
        # Texto para mostrar el último botón presionado (parte inferior izquierda)
        self.texto_boton = Text(
            text="Inicio..                            ",
            origin=(-.5, -.5),
            position=(-0.8, -0.45, -0.01),  # Un poco delante del fondo
            scale=(1.2, 1.2),
            background=True,
            color=color.yellow
        )

        self.inicializar_mundo()
        
        ruta_minimapa = r"img\mapav2simuladorues.png" 
        ruta_indicador = r"img\indicador.png" 
        
        
        self.inicializar_jugador()
        Minimap(
            player=self.jugador,
            map_scale=Vec2(0.45, 0.35),
            bg_texture=ruta_minimapa,
            icon_texture=ruta_indicador,
            scroll_factor=0.05 # Cambiar velocidad de desplazamiento del minimapa
        )


    def inicializar_jugador(self):
        self.jugador = FirstPersonController(
            mouse_sensitivity=Vec2(60, 60),
            position=(0, 0, -10)
        )
        self.jugador.speed = 5
        self.jugador.jump_height = 3

    def inicializar_mundo(self):
        self.objetos_escena = cargar_escena()
        # Si necesitas manipular los objetos, puedes acceder a self.objetos_escena

    def manejar_input_jugador(self, key):
        self.jugador.input(key)

    def input(self, key):
        mensaje = ""
        if key == '+':
            camera.fov = max(20, camera.fov - 5)
            mensaje = "Zoom +"
        if key == '-':
            camera.fov = min(120, camera.fov + 5)
            mensaje = "Zoom -"
        if key == 'right mouse down':
            self.mostrar_popup()
            mensaje = "Click derecho: mensaje"
        if key == 'left mouse down' or key == 'escape':
            self.cerrar_popup()
            mensaje = "Cerrar mensaje"
        if key == '1':
            mensaje = "Menú"

        # Solo muestra mensaje si hay acción
        self.texto_boton.text = mensaje

        # Borra el mensaje después de 1 segundo si hay mensaje
        if mensaje:
            invoke(setattr, self.texto_boton, 'text', '', delay=1)

    def mostrar_popup(self):
        if self.popup:
            destroy(self.popup)
            
        hit_info = raycast(self.jugador.camera_pivot.world_position, 
                         self.jugador.camera_pivot.forward, 
                         distance=50)
        
        if hit_info.hit:
            self.crear_popup(hit_info.entity)

    # juego.py (Fragmento modificado)
    def crear_popup(self, objeto):
        texto_final = obtener_texto_objeto(objeto.name)
        print(objeto.name, texto_final)
        self.popup = TextPopup(texto_final)

   
    def cerrar_popup(self):
        if self.popup:
            destroy(self.popup)
            self.popup = None

    def update(self):
        if hasattr(self, 'plataforma'):
            self.plataforma.rotation_y += 30 * time.dt

def obtener_texto_objeto(nombre):
    carpeta = os.path.join(os.path.dirname(__file__), 'textos')
    archivo = os.path.join(carpeta, f"{nombre.lower()}.txt")
    if os.path.exists(archivo):
        with open(archivo, encoding='utf-8') as f:
            return f.read().replace('\\n', '\n')  # Soporta saltos de línea escritos como \n
    else:
        return f"Objeto: {nombre}\n(No hay descripción disponible)"
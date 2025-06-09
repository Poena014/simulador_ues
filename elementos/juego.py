from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import os

from .textoemergente import TextPopup
from .minimapa import Minimap
from .escena1 import cargar_escena as cargar_escena1
from .escena2 import cargar_escena2

class MiJuego(Entity):
    def __init__(self):
        super().__init__()
        self.jugador = None
        self.popup = None
        self.minimapa = None
        self.escena_actual = 1  # Por defecto, escena 1

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

        # Indicador de posición del jugador (esquina inferior derecha)
        self.indicador_posicion = Text(
            text="x: 0.0  y: 0.0  z: 0.0                ",
            origin=(0.5, -0.5),
            position=(0.7, -0.48),  # Ajusta para la esquina inferior derecha
            scale=1.1,
            background=True,
            color=color.azure
        )

        self.cargar_escena(1)  # Carga la escena 1 por defecto

    def cargar_escena(self, numero):
        # Limpia objetos anteriores si existen
        if hasattr(self, 'objetos_escena') and self.objetos_escena:
            for obj in self.objetos_escena:
                destroy(obj)
        if self.minimapa:
            destroy(self.minimapa)
            self.minimapa = None

        # Carga la escena seleccionada
        if numero == 1:
            self.objetos_escena = cargar_escena1()
            self.inicializar_jugador()
            self.minimapa = Minimap(
                player=self.jugador,
                map_scale=Vec2(0.45, 0.35),
                bg_texture=r"img\mapav2simuladorues.png",
                icon_texture=r"img\indicador.png",
                scroll_factor=0.05
            )
            self.escena_actual = 1
        elif numero == 2:
            self.objetos_escena = cargar_escena2()
            self.inicializar_jugador()
            # No se crea minimapa en la escena 2
            self.escena_actual = 2

    def inicializar_jugador(self):
        self.jugador = FirstPersonController(
            mouse_sensitivity=Vec2(60, 60),
            position=(0, 0, -10)
        )
        self.jugador.speed = 12
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

        # Actualiza el indicador de posición del jugador
        if self.jugador:
            pos = self.jugador.position
            self.indicador_posicion.text = f"X: {pos.x:.2f}  Z: {pos.y:.2f}  Y: {pos.z:.2f}"

def obtener_texto_objeto(nombre):
    carpeta = os.path.join(os.path.dirname(__file__), 'textos')
    archivo = os.path.join(carpeta, f"{nombre.lower()}.txt")
    if os.path.exists(archivo):
        with open(archivo, encoding='utf-8') as f:
            return f.read().replace('\\n', '\n')  # Soporta saltos de línea escritos como \n
    else:
        return f"Objeto: {nombre}\n(No hay descripción disponible)"
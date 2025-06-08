from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

from .textoemergente import TextPopup
from .minimapa import Minimap
from .escena1 import cargar_escena

class MiJuego(Entity):
    def __init__(self):
        super().__init__()
        self.jugador = None
        self.popup = None

        self.inicializar_mundo()
        
        ruta_minimapa = r"img\mapav2simuladorues.png" 
        ruta_indicador = r"img\indicador.png" 
        
        
        self.inicializar_jugador()
        Minimap(
            player=self.jugador,
            map_scale=Vec2(0.45, 0.35),
            bg_texture=ruta_minimapa,
            icon_texture=ruta_indicador,
        )


    def inicializar_jugador(self):
        self.jugador = FirstPersonController(
            mouse_sensitivity=Vec2(60, 60),
            position=(0, 0, 0)
        )
        self.jugador.speed = 5
        self.jugador.jump_height = 3

    def inicializar_mundo(self):
        self.objetos_escena = cargar_escena()
        # Si necesitas manipular los objetos, puedes acceder a self.objetos_escena

    def manejar_input_jugador(self, key):
        self.jugador.input(key)

    def input(self, key):
        if key == 'right mouse down':
            self.mostrar_popup()
            
        if key == 'left mouse down' or key == 'escape':
            self.cerrar_popup()

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

        texto_final= f"Objeto: {objeto.name}"
        
        self.popup = TextPopup(texto_final)

   
    def cerrar_popup(self):
        if self.popup:
            destroy(self.popup)
            self.popup = None

    def update(self):
        if hasattr(self, 'plataforma'):
            self.plataforma.rotation_y += 30 * time.dt
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

from .textoemergente import TextPopup

class MiJuego(Entity):
    def __init__(self):
        super().__init__()
        self.jugador = None
        self.popup = None
        self.inicializar_jugador()
        self.inicializar_mundo()

    def inicializar_jugador(self):
        self.jugador = FirstPersonController(
            mouse_sensitivity=Vec2(60, 60),
            position=(0, 2, 0)
        )
        self.jugador.speed = 8
        self.jugador.jump_height = 3

    def inicializar_mundo(self):
        # Cielo
        Sky(texture='sky_sunset')
        
        # Suelo
        Entity(
            model='plane',
            texture='grass',
            scale=100,
            collider='mesh',
            texture_scale=(10, 10))
        
        # Objetos interactivos
        self.crear_objetos_basicos()
        self.crear_plataforma_rotante()

    def crear_objetos_basicos(self):
        # Cubo rojo
        Entity(
            name='Cubo Rojo Misterioso',
            model='cube',
            color=color.red,
            position=(5, 0.5, 5),
            scale=(2, 1, 2),
            collider='box',
            texture='white_cube')
        
        # Cubo azul
        Entity(
            name='Monumento Azul',
            model='cube',
            color=color.blue,
            position=(-5, 1.5, 8),
            scale=(3, 3, 3),
            collider='box',
            texture='brick')
        
        # Esfera verde
        Entity(
            name='Esfera Energética',
            model='sphere',
            color=color.green,
            position=(0, 1, 15),
            scale=2,
            collider='sphere',
            texture='shore')

    def crear_plataforma_rotante(self):
        self.plataforma = Entity(
            name='Plataforma Giratoria',
            model='cube',
            color=color.orange,
            position=(0, 1, 30),
            scale=(10, 0.5, 10),
            collider='box',
            texture='white_cube')
        
        Entity(
            model='sphere',
            color=color.cyan,
            parent=self.plataforma,
            position=(0, 1, 0),
            scale=1.5,
            collider='sphere')

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
            
        hit_info = raycast(
            self.jugador.camera_pivot.world_position,
            self.jugador.camera_pivot.forward,
            distance=50,
            ignore=(self.jugador,))
        
        if hit_info.hit:
            self.crear_popup(hit_info.entity)

    # juego.py (Fragmento modificado)
    def crear_popup(self, objeto):

 
        text_content = """
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor 
        incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud 
        exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure 
        dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
        Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit 
        anim id est laborum. Sed ut perspiciatis unde omnis iste natus error sit voluptatem 
        accusantium doloremque laudantium.
        """
        self.popup = TextPopup(text_content)

        

        

   
   
    def cerrar_popup(self):
        if self.popup:
            destroy(self.popup)
            self.popup = None

    def update(self):
        if hasattr(self, 'plataforma'):
            self.plataforma.rotation_y += 30 * time.dt
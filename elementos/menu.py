# menu.py - Sistema de menú completo
from ursina import *

class Menu(Entity):
    def __init__(self, juego):
        super().__init__(
            parent=camera.ui,
            model='quad',
            color=color.blue,
            scale=(2, 2),
            enabled=False,
            z=-10
        )
        self.juego = juego
        
        # Contenedor central
        self.contenedor = Entity(parent=self, scale=(0.6, 0.7), color=color.blue)
        
        # Elementos del menú
        self.titulo = Text(
            parent=self.contenedor,
            text='MENÚ PRINCIPAL',
            scale=1.8,
            y=0.35,
            origin=(0, 0.5)
        )
        
        self.boton_continuar = Button(
            parent=self.contenedor,
            text='Continuar (1)',
            color=color.green.tint(-0.1),
            scale=(0.4, 0.08),
            y=0.1,
            on_click=self.continuar)
        
        self.boton_salir = Button(
            parent=self.contenedor,
            text='Salir del Juego',
            color=color.red.tint(-0.1),
            scale=(0.4, 0.08),
            y=-0.1,
            on_click=self.salir)
    
    def mostrar(self):
        self.enabled = True
        mouse.locked = False
        mouse.visible = True
        self.juego.jugador.enabled = False
    
    def ocultar(self):
        self.enabled = False
        mouse.locked = True
        mouse.visible = False
        self.juego.jugador.enabled = True
    
    def continuar(self):
        self.ocultar()
        global en_pausa
        en_pausa = False
    
    def salir(self):
        application.quit()
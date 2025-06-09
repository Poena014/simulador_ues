# menu.py - Sistema de menú completo
from ursina import *

class Menu(Entity):
    def __init__(self, juego):
        super().__init__(
            parent=camera.ui,
            model='quad',
            color=color.rgba(0, 0, 0, 180),  # Fondo negro semitransparente
            scale=(2, 2),
            enabled=False,
            z=-10
        )
        self.juego = juego
        
        # Contenedor central
        self.contenedor = Entity(parent=self, scale=(0.6, 0.7), color=color.rgba(0, 0, 0, 200))  # Fondo del contenedor negro semitransparente
        
        # Elementos del menú
        self.titulo = Text(
            parent=self.contenedor,
            text='MENÚ PRINCIPAL',
            scale=1.8,
            y=0.28,  # Un poco más abajo
            origin=(0, 0.5),
            color=color.white  # Letras blancas
        )
        
        self.boton_escena1 = Button(
            parent=self.contenedor,
            text='Ir a Escena 1',
            color=color.green.tint(0.2),
            highlight_color=color.green.tint(0.4),
            pressed_color=color.green.tint(0.1),
            disabled_color=color.green.tint(0.1),
            scale=(0.4, 0.08),
            y=0.13,
            on_click=self.ir_a_escena1,
            text_color=color.white
        )
        
        self.boton_escena2 = Button(
            parent=self.contenedor,
            text='Ir a Escena 2',
            color=color.azure.tint(0.2),
            highlight_color=color.azure.tint(0.4),
            pressed_color=color.azure.tint(0.1),
            disabled_color=color.azure.tint(0.1),
            scale=(0.4, 0.08),
            y=0.01,
            on_click=self.ir_a_escena2,
            text_color=color.white
        )

        self.boton_opciones = Button(
            parent=self.contenedor,
            text='Opciones',
            color=color.orange.tint(0.2),
            highlight_color=color.orange.tint(0.4),
            pressed_color=color.orange.tint(0.1),
            disabled_color=color.orange.tint(0.1),
            scale=(0.4, 0.08),
            y=-0.11,
            on_click=self.mostrar_opciones,
            text_color=color.white
        )
        
        self.boton_salir = Button(
            parent=self.contenedor,
            text='Salir del Juego',
            color=color.red.tint(0.2),
            highlight_color=color.red.tint(0.4),
            pressed_color=color.red.tint(0.1),
            disabled_color=color.red.tint(0.1),
            scale=(0.4, 0.08),
            y=-0.23,
            on_click=self.salir,
            text_color=color.white
        )

    def mostrar_controles(self):
        print("Mostrar controles...")  # Aquí puedes mostrar una ventana o popup de controles

    def mostrar_opciones(self):
        print("Mostrar opciones...")  # Aquí puedes mostrar una ventana o popup de opciones

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

    def ir_a_escena1(self):
        self.juego.cargar_escena(1)
        self.ocultar()

    def ir_a_escena2(self):
        self.juego.cargar_escena(2)
        self.ocultar()
from ursina import *

class TextPopup(Entity):
    def __init__(self, text_content):
        super().__init__(
            parent=camera.ui,
            model='quad',
            color=color.rgba(0, 0, 0, 0.95),
            scale=(0.55, 0.4),
            position=(0, 0.1),
            z=-1
        )
        
        # Texto principal
        self.text_entity = Text(
            parent=self,
            text=text_content,
            scale=(2,2,1),
            origin=(0, 0),
            color=color.white
        )
        
        # # Ajustar tamaño del fondo al texto
        # self.scale_x = max(self.text_entity.width * 0.025, 0.6)
        
        # self.scale_y = max(len(text_content.split('\n'))) * 0.05 + 0.2
        
        # # Botón de cierre proporcional
        # self.setup_close_button()
        
        # # Borde de referencia
        # self.add_debug_border()


    # def setup_close_button(self):
    #     # Botón con proporción relativa al contenedor
    #     btn_scale = self.CONTAINER_WIDTH * 0.12
    #     Button(
    #         parent=self,
    #         text='✕',
    #         color=color.white,
    #         position=(self.CONTAINER_WIDTH/2 - 0.04, self.CONTAINER_HEIGHT/2 - 0.04),
    #         scale=(btn_scale, btn_scale),
    #         on_click=lambda: destroy(self),
    #         text_scale=1.5
    #     )

    # def add_debug_border(self):
    #     Entity(
    #         parent=self,
    #         model=Quad(mode='line', thickness=2),
    #         color=color.rgba(255, 255, 255, 100),
    #         scale=(1.02, 1.02),
    #         z=-0.1
    #     )


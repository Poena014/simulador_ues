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
        
        # Constantes de proporción basadas en el tamaño del contenedor
        self.CONTAINER_WIDTH = 0.55
        self.CONTAINER_HEIGHT = 0.4
        self.TEXT_SCALE = 0.018  # Calculado experimentalmente para 0.55 de ancho
        self.LINE_HEIGHT = self.TEXT_SCALE * 13.5  # Proporción áurea aplicada
        self.PADDING_X = 0.03  # 5% del ancho del contenedor
        self.PADDING_Y = 0.035  # 8% del alto del contenedor
        
        # Variables calculadas
        self.max_line_width = self.CONTAINER_WIDTH - 2 * self.PADDING_X
        self.max_vertical_lines = int((self.CONTAINER_HEIGHT - 2 * self.PADDING_Y) / self.LINE_HEIGHT)
        
        # Sistema de texto
        self.setup_text(text_content)
        
        # Botón de cierre proporcional
        self.setup_close_button()
        
        # Borde de referencia
        self.add_debug_border()

    def setup_text(self, text_content):
        lines = self.wrap_text(text_content)
        start_y = (self.CONTAINER_HEIGHT/2) - self.PADDING_Y
        
        for i, line in enumerate(lines[:self.max_vertical_lines]):
            Text(
                text=line,
                parent=self,
                scale=self.TEXT_SCALE,
                position=(
                    -self.CONTAINER_WIDTH/2 + self.PADDING_X,
                    start_y - i * self.LINE_HEIGHT
                ),
                origin=(-0.5, 0.5),
                color=color.white
            )

    def wrap_text(self, text):
        words = text.replace('\n', ' ').split()
        lines = []
        current_line = []
        
        for word in words:
            test_line = ' '.join(current_line + [word])
            line_width = Text.get_width(test_line) * self.TEXT_SCALE
            
            if line_width <= self.max_line_width:
                current_line.append(word)
            else:
                lines.append(' '.join(current_line))
                current_line = [word]
        
        if current_line:
            lines.append(' '.join(current_line))
        
        return lines

    def setup_close_button(self):
        # Botón con proporción relativa al contenedor
        btn_scale = self.CONTAINER_WIDTH * 0.12
        Button(
            parent=self,
            text='✕',
            color=color.white,
            position=(self.CONTAINER_WIDTH/2 - 0.04, self.CONTAINER_HEIGHT/2 - 0.04),
            scale=(btn_scale, btn_scale),
            on_click=lambda: destroy(self),
            text_scale=1.5
        )

    def add_debug_border(self):
        Entity(
            parent=self,
            model=Quad(mode='line', thickness=2),
            color=color.rgba(255, 255, 255, 100),
            scale=(1.02, 1.02),
            z=-0.1
        )


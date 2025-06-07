from ursina import *

app = Ursina(broken_renderer=True)  # Intenta con renderizador alternativo

# Piso con todas las opciones de solución
piso = Entity(
    model='plane',
    texture='white_cube',
    scale=10,
    double_sided=True,
    visible=True,
    collider='box'
)

# Cámara simple en lugar de EditorCamera
camera.position = (0, 5, -15)
camera.look_at((0,0,0))

# Añadir ejes de referencia

Grid(10, 10)  # Rejilla adicional para referencia

app.run()
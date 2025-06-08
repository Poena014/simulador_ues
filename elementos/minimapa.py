from ursina import *

class Minimap(Entity):
    def __init__(self, player, bg_texture='mapa_fia', icon_texture='icono_jugador', bg_position=Vec2(-0.7, 0.3), map_scale=Vec2(0.3, 0.3), zoom=0.2, scroll_factor=0.01):
        super().__init__()
        self.player = player
        self.zoom = zoom  # Porcentaje del mapa visible (0.2 = 20%)
        self.bg_scale = map_scale
        self.scroll_factor = scroll_factor  # Factor de reducción de desplazamiento

        # UVs iniciales centrados
        self.uv_center = Vec2(0.5, 0.5)
        self.uv_size = self.zoom

        # Fondo del minimapa como quad con UVs personalizados (sin modificar proporciones del scale)
        self.minimap_bg = Entity(
            parent=camera.ui,
            model=Mesh(
                vertices=[Vec3(-.5,-.5,0), Vec3(.5,-.5,0), Vec3(.5,.5,0), Vec3(-.5,.5,0)],
                uvs=self._get_uvs(self.uv_center, self.uv_size),
                triangles=[0,1,2, 2,3,0],
                mode='triangle'
            ),
            texture=bg_texture,
            position=bg_position,
            scale=map_scale  # Solo para tamaño visual, no afecta el recorte de la textura
        )

        self.player_icon = Entity(
            parent=self.minimap_bg,
            model='circle',
            texture=icon_texture,
            scale=(0.1, 0.1),
        )

        self.uv_center_actual = Vec2(0.5, 0.5)  # Centro actual mostrado
        self.offset = Vec2(0, 0)  # Nuevo: acumulador de desplazamiento
        self.suavizado = 1 # Entre 0 (no se mueve) y 1 (salta directo). Más bajo = más lento

    def _get_uvs(self, center, size):
        # Calcula los UVs para mostrar solo una parte de la textura
        half = size / 2
        u0, v0 = center.x - half, center.y - half
        u1, v1 = center.x + half, center.y + half
        return [(u0, v0), (u1, v0), (u1, v1), (u0, v1)]

    def update(self):
        self.player_icon.rotation_z = -self.player.rotation_y

        # Mapea la posición del jugador directamente a UVs (ajusta el factor para tu experiencia)
        # Por ejemplo, cada 1 unidad en el mundo mueve 0.01 en UV
        factor = 0.002  # Ajusta este valor para la sensibilidad del desplazamiento

        u = 0.5 + self.player.x * factor
        v = 0.5 + self.player.z * factor

        # Limita al rango visible del minimapa
        half_size = self.uv_size / 2
        u = clamp(u, half_size, 1 - half_size)
        v = clamp(v, half_size, 1 - half_size)

        # Actualiza los UVs del quad para mover la "ventana" (recorte de la textura)
        self.minimap_bg.model.uvs = self._get_uvs(Vec2(u, v), self.uv_size)
        self.minimap_bg.model.generate()


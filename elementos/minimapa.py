from ursina import *

class Minimap(Entity):
    def __init__(self, player, map_scale=Vec2(0.45, 0.35), bg_texture='mapa_fia', icon_texture='icono_jugador', bg_position=(-0.7, 0.3), bg_scale=(0.3, 0.3)):
        super().__init__()
        self.player = player
        self.map_scale = map_scale
        
        # Fondo del minimapa
        self.minimap_bg = Entity(
            parent=camera.ui,
            model='quad',
            texture=bg_texture,
            scale=bg_scale,
            position=bg_position
        )
        
        # Ícono del jugador en el minimapa
        self.player_icon = Entity(
            parent=self.minimap_bg,
            model='quad',
            texture=icon_texture,
            scale=(0.1, 0.1),
            position=(0, 0)
        )
        
    def update(self):
        if self.player and isinstance(self.player.position, Vec3):
            self.player_icon.x = self.player.position.x * self.map_scale.x*0.1
            self.player_icon.y = self.player.position.z * self.map_scale.y*0.1
            self.player_icon.rotation_z = -self.player.rotation_y
        else:
            print("⚠️ El objeto 'player.position' no es un Vec3:", self.player.position)
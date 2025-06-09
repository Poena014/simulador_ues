from ursina import *

def cargar_arboles():
    arboles=[]
    
    # Definición de los arboles
    
    arbol_1 = Entity(
        model='tripo_convert_aba66a69-45fd-4baa-b625-7ae8a34771e7.obj',
        texture=load_texture('tripo_image_aba66a69-45fd-4baa-b625-7ae8a34771e7_0.jpg'),
        scale=9,
        position=Vec3(35, 5, 12),
        rotation_y=0
    )
    
    arboles.append(arbol_1)
        #arboles que estan ala par del edificio A
    arbol_2 = Entity(
        model='tripo_convert_b68a70a1-05d1-449b-ac0e-2b2583790c71.obj',
        texture=load_texture('tripo_image_b68a70a1-05d1-449b-ac0e-2b2583790c71_0.jpg'),
        scale=9.5,
        position=Vec3(56, 5 -27),
        rotation_y=30
    )
    
    arboles.append(arbol_2)

    arbol_3 = Entity(
        model='tripo_convert_ccd064cd-74e9-4315-872f-cc5250e4820a.obj',
        texture=load_texture('tripo_image_ccd064cd-74e9-4315-872f-cc5250e4820a_0.jpg'),
        scale=9.5,
        position=Vec3(66, 5, -25),
        rotation_y=60
    )
    arboles.append(arbol_3)
    arbol_4 = Entity(
        model='tripo_convert_ccd064cd-74e9-4315-872f-cc5250e4820a.obj',
        texture=load_texture('tripo_image_ccd064cd-74e9-4315-872f-cc5250e4820a_0.jpg'),
        scale=9.5,
        position=Vec3(64, 5, -34),
        rotation_y=60
    )
    arboles.append(arbol_4)
    #arboles que estan en medio del edificio A y el marmol
    arbol_5 = Entity(
        model='tripo_convert_ccd064cd-74e9-4315-872f-cc5250e4820a.obj',
        texture=load_texture('tripo_image_ccd064cd-74e9-4315-872f-cc5250e4820a_0.jpg'),
        scale=15,
        position=Vec3(21, 8, -27),
        rotation_y=60
    )
    arboles.append(arbol_5)
    jardin4 = Entity(
        model='plane', 
        texture='grass', 
        scale=1,
        position=(21, 0.1, -27),
    )
    
    arboles.append(jardin4)
#arboles frente a academica
    arbol_6 = Entity(
        model='tripo_convert_ccd064cd-74e9-4315-872f-cc5250e4820a.obj',
        texture=load_texture('tripo_image_ccd064cd-74e9-4315-872f-cc5250e4820a_0.jpg'),
        scale=12,
        position=Vec3(-20, 6, 17.53),
        rotation_y=60
    )
    arboles.append(arbol_6)
    jardin6 = Entity(
        model='plane', 
        texture='grass', 
        scale=3,
        position=(-20, 0.1, 17.53),
    )
    arbol_7 = Entity(
        model='tripo_convert_ccd064cd-74e9-4315-872f-cc5250e4820a.obj',
        texture=load_texture('tripo_image_ccd064cd-74e9-4315-872f-cc5250e4820a_0.jpg'),
        scale=9.5,
        position=Vec3(-24, 5, 17.54),
        rotation_y=60
    )
    arboles.append(arbol_7)
    jardin7 = Entity(
        model='plane', 
        texture='grass', 
        scale=3,
        position=(-24, 0.1, 17.54),
    )
    arbol_8 = Entity(
        model='tripo_convert_ccd064cd-74e9-4315-872f-cc5250e4820a.obj',
        texture=load_texture('tripo_image_ccd064cd-74e9-4315-872f-cc5250e4820a_0.jpg'),
        scale=9.5,
        position=Vec3(-22.05, 5, 17.54),
        rotation_y=60
    )
    arboles.append(arbol_8)
    jardin8 = Entity(
        model='plane', 
        texture='grass', 
        scale=3,
        position=(-22.05, 0.1, 17.54),
    )
    arbol_9 = Entity(
        model='tripo_convert_ccd064cd-74e9-4315-872f-cc5250e4820a.obj',
        texture=load_texture('tripo_image_ccd064cd-74e9-4315-872f-cc5250e4820a_0.jpg'),
        scale=9.5,
        position=Vec3(-22.12, 5, 15.74),
        rotation_y=60
    )
    arboles.append(arbol_9)
    jardin9 = Entity(
        model='plane', 
        texture='grass', 
        scale=3,
        position=(-22.12, 0.1, 15.74),
    )
    arbol_10 = Entity(
        model='tripo_convert_ccd064cd-74e9-4315-872f-cc5250e4820a.obj',
        texture=load_texture('tripo_image_ccd064cd-74e9-4315-872f-cc5250e4820a_0.jpg'),
        scale=9.5,
        position=Vec3(2.70, 6, -15.79),
        rotation_y=60
    )
    arboles.append(arbol_10)
    jardin10 = Entity(
        model='plane', 
        texture='grass', 
        scale=3,
        position=(23.70, 0.1, -15.79),
    )
    arbol_11 = Entity(
        model='tripo_convert_ccd064cd-74e9-4315-872f-cc5250e4820a.obj',
        texture=load_texture('tripo_image_ccd064cd-74e9-4315-872f-cc5250e4820a_0.jpg'),
        scale=9.5,
        position=Vec3(12.07, 5, 24.38),
        rotation_y=60
    )
    arboles.append(arbol_11)
    jardin11 = Entity(
        model='plane', 
        texture='grass', 
        scale=3,
        position=(12.07, 0.1, 24.38),
    )

    #par de la asociacion 
    arbol_12 = Entity(
        model='tripo_convert_ccd064cd-74e9-4315-872f-cc5250e4820a.obj',
        texture=load_texture('tripo_image_ccd064cd-74e9-4315-872f-cc5250e4820a_0.jpg'),
        scale=(15,5,8),
        position=Vec3(27, 3, 73),
        rotation_y=60
    )
    arboles.append(arbol_12)
    arbol_13 = Entity(
        model='tripo_convert_ccd064cd-74e9-4315-872f-cc5250e4820a.obj',
        texture=load_texture('tripo_image_ccd064cd-74e9-4315-872f-cc5250e4820a_0.jpg'),
        scale=9.5,
        position=Vec3(19.01, 5, 20.25),
        rotation_y=60
    )
    arboles.append(arbol_13)
    jardin13 = Entity(
        model='plane', 
        texture='grass', 
        scale=3,
        position=(19.01, 0.1, 20.25),
    )
    arbol_14 = Entity(
        model='tripo_convert_ccd064cd-74e9-4315-872f-cc5250e4820a.obj',
        texture=load_texture('tripo_image_ccd064cd-74e9-4315-872f-cc5250e4820a_0.jpg'),
        scale=9.5,
        position=Vec3(48.28, 5, 36.35),
        rotation_y=60
    )
    arboles.append(arbol_14)
    jardin14 = Entity(
        model='plane', 
        texture='grass', 
        scale=3,
        position=(48.28, 0.1, 36.35),
    )
    #arboles frente al marmol y ala par
    arbol_15 = Entity(
        model='tripo_convert_ccd064cd-74e9-4315-872f-cc5250e4820a.obj',
        texture=load_texture('tripo_image_ccd064cd-74e9-4315-872f-cc5250e4820a_0.jpg'),
        scale=9.5,
        position=Vec3(-8.85, 5, -20.99),
        rotation_y=60
    )
    arboles.append(arbol_14)
    jardin15 = Entity(
        model='plane', 
        texture='grass', 
        scale=3,
        position=(-8.85, 0.1, -20.99),
    )
    arbol_16 = Entity(
        model='tripo_convert_ccd064cd-74e9-4315-872f-cc5250e4820a.obj',
        texture=load_texture('tripo_image_ccd064cd-74e9-4315-872f-cc5250e4820a_0.jpg'),
        scale=9.5,
        position=Vec3(-18.27, 5, -36.71),
        rotation_y=60
    )
    arboles.append(arbol_14)
    jardin16 = Entity(
        model='plane', 
        texture='grass', 
        scale=3,
        position=(-18.27, 0.1, -36.71),
    )
    arbol_17 = Entity(
        model='tripo_convert_ccd064cd-74e9-4315-872f-cc5250e4820a.obj',
        texture=load_texture('tripo_image_ccd064cd-74e9-4315-872f-cc5250e4820a_0.jpg'),
        scale=9.5,
        position=Vec3(-22.77, 5, -36.60),
        rotation_y=60
    )
    arboles.append(arbol_14)
    jardin17 = Entity(
        model='plane', 
        texture='grass', 
        scale=3,
        position=(-22.77, 0.1, -36.60),
    )
    arbol_18 = Entity(
        model='tripo_convert_ccd064cd-74e9-4315-872f-cc5250e4820a.obj',
        texture=load_texture('tripo_image_ccd064cd-74e9-4315-872f-cc5250e4820a_0.jpg'),
        scale=9.5,
        position=Vec3(-17.68, 5, -41.83),
        rotation_y=60
    )
    arboles.append(arbol_14)
    jardin18 = Entity(
        model='plane', 
        texture='grass', 
        scale=3,
        position=(-17.68, 0.1, -41.83),
    )
    return arboles
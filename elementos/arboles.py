from ursina import *

def cargar_arboles():
    arboles=[]
    
    # Definición de los arboles
    
    arbol_1 = Entity(
        model='tripo_convert_aba66a69-45fd-4baa-b625-7ae8a34771e7.obj',
        texture=load_texture('tripo_image_aba66a69-45fd-4baa-b625-7ae8a34771e7_0.jpg'),
        scale=10,
        position=Vec3(35, 5, 12),
        rotation_y=0
    )
    
    arboles.append(arbol_1)

    arbol_2 = Entity(
        model='tripo_convert_b68a70a1-05d1-449b-ac0e-2b2583790c71.obj',
        texture=load_texture('tripo_image_b68a70a1-05d1-449b-ac0e-2b2583790c71_0.jpg'),
        scale=10,
        position=Vec3(56, 5 -27),
        rotation_y=30
    )
    
    arboles.append(arbol_2)

    arbol_3 = Entity(
        model='tripo_convert_ccd064cd-74e9-4315-872f-cc5250e4820a.obj',
        texture=load_texture('tripo_image_ccd064cd-74e9-4315-872f-cc5250e4820a_0.jpg'),
        scale=10,
        position=Vec3(66, 5, -25),
        rotation_y=60
    )
    arboles.append(arbol_3)
    arbol_4 = Entity(
        model='tripo_convert_ccd064cd-74e9-4315-872f-cc5250e4820a.obj',
        texture=load_texture('tripo_image_ccd064cd-74e9-4315-872f-cc5250e4820a_0.jpg'),
        scale=10,
        position=Vec3(64, 5, -34),
        rotation_y=60
    )
    arboles.append(arbol_4)
    arbol_5 = Entity(
        model='tripo_convert_ccd064cd-74e9-4315-872f-cc5250e4820a.obj',
        texture=load_texture('tripo_image_ccd064cd-74e9-4315-872f-cc5250e4820a_0.jpg'),
        scale=10,
        position=Vec3(21, 5, -27),
        rotation_y=60
    )
    arboles.append(arbol_5)
    arbol_6 = Entity(
        model='tripo_convert_ccd064cd-74e9-4315-872f-cc5250e4820a.obj',
        texture=load_texture('tripo_image_ccd064cd-74e9-4315-872f-cc5250e4820a_0.jpg'),
        scale=10,
        position=Vec3(10, 5, -32),
        rotation_y=60
    )
    arboles.append(arbol_6)
    arbol_7 = Entity(
        model='tripo_convert_ccd064cd-74e9-4315-872f-cc5250e4820a.obj',
        texture=load_texture('tripo_image_ccd064cd-74e9-4315-872f-cc5250e4820a_0.jpg'),
        scale=10,
        position=Vec3(-10, 5, -21),
        rotation_y=60
    )
    arboles.append(arbol_7)
    arbol_8 = Entity(
        model='tripo_convert_ccd064cd-74e9-4315-872f-cc5250e4820a.obj',
        texture=load_texture('tripo_image_ccd064cd-74e9-4315-872f-cc5250e4820a_0.jpg'),
        scale=10,
        position=Vec3(-18, 5, -35),
        rotation_y=60
    )
    arboles.append(arbol_8)
    arbol_9 = Entity(
        model='tripo_convert_ccd064cd-74e9-4315-872f-cc5250e4820a.obj',
        texture=load_texture('tripo_image_ccd064cd-74e9-4315-872f-cc5250e4820a_0.jpg'),
        scale=10,
        position=Vec3(-26, 5, -34.99),
        rotation_y=60
    )
    arboles.append(arbol_9)
    arbol_10 = Entity(
        model='tripo_convert_ccd064cd-74e9-4315-872f-cc5250e4820a.obj',
        texture=load_texture('tripo_image_ccd064cd-74e9-4315-872f-cc5250e4820a_0.jpg'),
        scale=10,
        position=Vec3(33, 6, -16),
        rotation_y=60
    )
    arboles.append(arbol_10)
    arbol_11 = Entity(
        model='tripo_convert_ccd064cd-74e9-4315-872f-cc5250e4820a.obj',
        texture=load_texture('tripo_image_ccd064cd-74e9-4315-872f-cc5250e4820a_0.jpg'),
        scale=10,
        position=Vec3(38, 5, -2),
        rotation_y=60
    )
    arboles.append(arbol_11)

    #par de la asociacion 
    arbol_12 = Entity(
        model='tripo_convert_ccd064cd-74e9-4315-872f-cc5250e4820a.obj',
        texture=load_texture('tripo_image_ccd064cd-74e9-4315-872f-cc5250e4820a_0.jpg'),
        scale=(15,5,8),
        position=Vec3(27, 3, 73),
        rotation_y=60
    )
    arboles.append(arbol_12)


    
    return arboles
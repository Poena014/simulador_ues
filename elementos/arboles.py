from ursina import *

def cargar_arboles():
    arboles=[]
    
    # Definición de los arboles
    
    arbol_1 = Entity(
        model='tripo_convert_aba66a69-45fd-4baa-b625-7ae8a34771e7.obj',
        texture=load_texture('tripo_image_aba66a69-45fd-4baa-b625-7ae8a34771e7_0.jpg'),
        scale=2.5,
        position=Vec3(-12, 1.5, -12),
        rotation_y=0
    )
    
    arboles.append(arbol_1)

    arbol_izquierda_2 = Entity(
        model='tripo_convert_b68a70a1-05d1-449b-ac0e-2b2583790c71.obj',
        texture=load_texture('tripo_image_b68a70a1-05d1-449b-ac0e-2b2583790c71_0.jpg'),
        scale=2.5,
        position=Vec3(-13.5, 1.5, -12.5),
        rotation_y=30
    )
    
    arboles.append(arbol_izquierda_2)

    arbol_izquierda_3 = Entity(
        model='tripo_convert_ccd064cd-74e9-4315-872f-cc5250e4820a.obj',
        texture=load_texture('tripo_image_ccd064cd-74e9-4315-872f-cc5250e4820a_0.jpg'),
        scale=2.5,
        position=Vec3(-11, 1.5, -11.5),
        rotation_y=60
    )
    arboles.append(arbol_izquierda_3)
    
    
    
    return arboles
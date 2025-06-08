from ursina import *

def cargar_mesas():
    mesas=[]
    
    # Definición de las mesas
    
    mesa3 = Entity(
        model='tripo_convert_cb71c3ca-ecec-4c0b-81b2-0c942de3af25.obj',
        texture=load_texture('tripo_image_cb71c3ca-ecec-4c0b-81b2-0c942de3af25_0.jpg'),
        specular_map=load_texture('tripo_image_cb71c3ca-ecec-4c0b-81b2-0c942de3af25_Roughness.jpg'),
        reflection_map=load_texture('tripo_image_cb71c3ca-ecec-4c0b-81b2-0c942de3af25_Metallic.jpg'),
        normal_map=load_texture('tripo_image_cb71c3ca-ecec-4c0b-81b2-0c942de3af25_2.jpg'),
        scale=2.5,
        position=Vec3(-28, 3, -15),
        rotation_y=15
    )
    
    mesas.append(mesa3)

    mesa4 = Entity(
        model='tripo_convert_2d49c5fb-c113-423c-b66a-88ebf97a811f.obj',
        texture=load_texture('tripo_image_2d49c5fb-c113-423c-b66a-88ebf97a811f_0.jpg'),
        specular_map=load_texture('tripo_image_2d49c5fb-c113-423c-b66a-88ebf97a811f_Roughness.jpg'),
        reflection_map=load_texture('tripo_image_2d49c5fb-c113-423c-b66a-88ebf97a811f_Metallic.jpg'),
        normal_map=load_texture('tripo_image_2d49c5fb-c113-423c-b66a-88ebf97a811f_2.jpg'),
        scale=2.5,
        position=Vec3(-4.5, 0.5, 4),
        rotation_y=-10
    )
    mesas.append(mesa4)
    
    
    return mesas
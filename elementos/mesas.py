from ursina import *

def cargar_mesas():
    mesas=[]
    
    # Definición de las mesas
    
    mesa3_2 = Entity(
        model='tripo_convert_cb71c3ca-ecec-4c0b-81b2-0c942de3af25.obj',
        texture=load_texture('tripo_image_cb71c3ca-ecec-4c0b-81b2-0c942de3af25_0.jpg'),
        specular_map=load_texture('tripo_image_cb71c3ca-ecec-4c0b-81b2-0c942de3af25_Roughness.jpg'),
        reflection_map=load_texture('tripo_image_cb71c3ca-ecec-4c0b-81b2-0c942de3af25_Metallic.jpg'),
        normal_map=load_texture('tripo_image_cb71c3ca-ecec-4c0b-81b2-0c942de3af25_2.jpg'),
        scale=3,
        position=(32,0.5,3),
    )
    
    mesas.append(mesa3_2)
    
    mesa3_3 = Entity(
        model='tripo_convert_cb71c3ca-ecec-4c0b-81b2-0c942de3af25.obj',
        texture=load_texture('tripo_image_cb71c3ca-ecec-4c0b-81b2-0c942de3af25_0.jpg'),
        specular_map=load_texture('tripo_image_cb71c3ca-ecec-4c0b-81b2-0c942de3af25_Roughness.jpg'),
        reflection_map=load_texture('tripo_image_cb71c3ca-ecec-4c0b-81b2-0c942de3af25_Metallic.jpg'),
        normal_map=load_texture('tripo_image_cb71c3ca-ecec-4c0b-81b2-0c942de3af25_2.jpg'),
        scale=3,
        position=(41,0.5,22),
    )
    
    mesas.append(mesa3_3)
    
    mesa3_4 = Entity(
        model='tripo_convert_cb71c3ca-ecec-4c0b-81b2-0c942de3af25.obj',
        texture=load_texture('tripo_image_cb71c3ca-ecec-4c0b-81b2-0c942de3af25_0.jpg'),
        specular_map=load_texture('tripo_image_cb71c3ca-ecec-4c0b-81b2-0c942de3af25_Roughness.jpg'),
        reflection_map=load_texture('tripo_image_cb71c3ca-ecec-4c0b-81b2-0c942de3af25_Metallic.jpg'),
        normal_map=load_texture('tripo_image_cb71c3ca-ecec-4c0b-81b2-0c942de3af25_2.jpg'),
        scale=3,
        position=(41,0.5,18.5),
    )
    
    mesas.append(mesa3_4)
    
    mesav1_4 = Entity(
        model='tripo_convert_cb71c3ca-ecec-4c0b-81b2-0c942de3af25.obj',
        texture=load_texture('tripo_image_cb71c3ca-ecec-4c0b-81b2-0c942de3af25_0.jpg'),
        specular_map=load_texture('tripo_image_cb71c3ca-ecec-4c0b-81b2-0c942de3af25_Roughness.jpg'),
        reflection_map=load_texture('tripo_image_cb71c3ca-ecec-4c0b-81b2-0c942de3af25_Metallic.jpg'),
        normal_map=load_texture('tripo_image_cb71c3ca-ecec-4c0b-81b2-0c942de3af25_2.jpg'),
        scale=3,
        position=(62, 0.5 ,62),
    )
    
    mesas.append(mesav1_4)
    
    
    
    
    

    mesa4 = Entity(
        model='tripo_convert_2d49c5fb-c113-423c-b66a-88ebf97a811f.obj',
        texture=load_texture('tripo_image_2d49c5fb-c113-423c-b66a-88ebf97a811f_0.jpg'),
        specular_map=load_texture('tripo_image_2d49c5fb-c113-423c-b66a-88ebf97a811f_Roughness.jpg'),
        reflection_map=load_texture('tripo_image_2d49c5fb-c113-423c-b66a-88ebf97a811f_Metallic.jpg'),
        normal_map=load_texture('tripo_image_2d49c5fb-c113-423c-b66a-88ebf97a811f_2.jpg'),
        scale=2.5,
        position=Vec3(77,0.5,97),
    )
    mesas.append(mesa4)
    
    mesav2_1 = Entity(
        model='tripo_convert_2d49c5fb-c113-423c-b66a-88ebf97a811f.obj',
        texture=load_texture('tripo_image_2d49c5fb-c113-423c-b66a-88ebf97a811f_0.jpg'),
        specular_map=load_texture('tripo_image_2d49c5fb-c113-423c-b66a-88ebf97a811f_Roughness.jpg'),
        reflection_map=load_texture('tripo_image_2d49c5fb-c113-423c-b66a-88ebf97a811f_Metallic.jpg'),
        normal_map=load_texture('tripo_image_2d49c5fb-c113-423c-b66a-88ebf97a811f_2.jpg'),
        scale=2.5,
        position=Vec3(77,0.5,94),
    )
    mesas.append(mesav2_1)
    
    referencia1=Entity(model='cube', texture='brick', scale=5, position=(48.17,1,53.5))  # Plano con textura de ladrillos
    mesas.append(referencia1)
    
    
    return mesas
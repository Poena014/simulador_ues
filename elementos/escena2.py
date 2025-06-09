from ursina import *
import random

def cargar_escena2():
    objetos = []

    # Suelo
    terreno_tierra = Entity(
        model='plane',
        texture='rocky_terrain_02_diff_4k.jpg',
        scale=50,
        color=color.white,
        collider='box',
        position=(0, 0, 0)
    )
    objetos.append(terreno_tierra)

    # Modelo central
    central_model = Entity(
        model='tripo_convert_aee6c7c4-7f9e-474a-ae24-ba97855e0542.obj',
        texture=load_texture('tripo_image_aee6c7c4-7f9e-474a-ae24-ba97855e0542_0.jpg'),
        normal_map=load_texture('tripo_image_aee6c7c4-7f9e-474a-ae24-ba97855e0542_2.jpg'),
        specular_map=load_texture('tripo_image_aee6c7c4-7f9e-474a-ae24-ba97855e0542_Roughness.jpg'),
        reflection_map=load_texture('tripo_image_aee6c7c4-7f9e-474a-ae24-ba97855e0542_Metallic.jpg'),
        scale=3.0,
        position=Vec3(0, 1.50, 0),
        rotation_y=270
    )
    objetos.append(central_model)

    def generar_posicion_aleatoria(rango=25, min_dist=5):
        while True:
            x = random.uniform(-rango, rango)
            z = random.uniform(-rango, rango)
            pos = Vec3(x, 0, z)
            if distance(pos, central_model.position) > min_dist:
                return pos

    modelos_arboles = [
        {
            "model": 'tripo_convert_aba66a69-45fd-4baa-b625-7ae8a34771e7.obj',
            "texture": 'tripo_image_aba66a69-45fd-4baa-b625-7ae8a34771e7_0.jpg'
        },
        {
            "model": 'tripo_convert_b68a70a1-05d1-449b-ac0e-2b2583790c71.obj',
            "texture": 'tripo_image_b68a70a1-05d1-449b-ac0e-2b2583790c71_0.jpg'
        },
        {
            "model": 'tripo_convert_ccd064cd-74e9-4315-872f-cc5250e4820a.obj',
            "texture": 'tripo_image_ccd064cd-74e9-4315-872f-cc5250e4820a_0.jpg'
        }
    ]

    # Árboles
    for arbol in modelos_arboles:
        for _ in range(50):
            posicion = generar_posicion_aleatoria()
            arbol_ent = Entity(
                model=arbol["model"],
                texture=load_texture(arbol["texture"]),
                scale=2.5,
                position=posicion + Vec3(0, 1.5, 0),
                rotation_y=random.uniform(0, 360)
            )
            objetos.append(arbol_ent)

    modelos_mesas = [
        {
            "model": 'tripo_convert_cb71c3ca-ecec-4c0b-81b2-0c942de3af25.obj',
            "texture": 'tripo_image_cb71c3ca-ecec-4c0b-81b2-0c942de3af25_0.jpg',
            "specular_map": 'tripo_image_cb71c3ca-ecec-4c0b-81b2-0c942de3af25_Roughness.jpg',
            "reflection_map": 'tripo_image_cb71c3ca-ecec-4c0b-81b2-0c942de3af25_Metallic.jpg',
            "normal_map": 'tripo_image_cb71c3ca-ecec-4c0b-81b2-0c942de3af25_2.jpg',
            "rotacion_base": 15
        },
        {
            "model": 'tripo_convert_2d49c5fb-c113-423c-b66a-88ebf97a811f.obj',
            "texture": 'tripo_image_2d49c5fb-c113-423c-b66a-88ebf97a811f_0.jpg',
            "specular_map": 'tripo_image_2d49c5fb-c113-423c-b66a-88ebf97a811f_Roughness.jpg',
            "reflection_map": 'tripo_image_2d49c5fb-c113-423c-b66a-88ebf97a811f_Metallic.jpg',
            "normal_map": 'tripo_image_2d49c5fb-c113-423c-b66a-88ebf97a811f_2.jpg',
            "rotacion_base": -10
        }
    ]

    # Mesas
    for mesa in modelos_mesas:
        for _ in range(7):
            posicion = generar_posicion_aleatoria()
            mesa_ent = Entity(
                model=mesa["model"],
                texture=load_texture(mesa["texture"]),
                specular_map=load_texture(mesa["specular_map"]),
                reflection_map=load_texture(mesa["reflection_map"]),
                normal_map=load_texture(mesa["normal_map"]),
                scale=2.5,
                position=posicion + Vec3(0, 0.5, 0),
                rotation_y=mesa["rotacion_base"] + random.uniform(-30, 30)
            )
            objetos.append(mesa_ent)

    return objetos

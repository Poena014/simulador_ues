from ursina import *
import os
from .mesas import cargar_mesas
from .arboles import cargar_arboles
from .basureros import cargar_basureros

def obtener_ruta_modelo(nombre_modelo):
    import os
    return os.path.abspath(
        os.path.join("..", "simulador_ues\modelos", f"{nombre_modelo}")
    )

def cargar_escena():
    objetos = []
    # Ejemplo de objetos, agrega los que quieras
    suelo = Entity(
        model='plane',
        texture='walk3',
        scale=325,
        collider='box',
        texture_scale=(10, 10)
    )
    objetos.append(suelo)
    
    
    jardin1 = Entity(
        model='plane', 
        texture='grass', 
        scale=(15, 1, 30),
        position=(28, 0.1, 4),
    )
    
    objetos.append(jardin1)
    
    
    jardin2 = Entity(
        model='plane', 
        texture='tierra3', 
        texture_scale=(1, 1),
        scale=(11, 1, 6),
        position=(15, 0.1, -11),
    )
    
    objetos.append(jardin2)
    
    jardin3 = Entity(
        model='plane', 
        texture='grass', 
        scale=(13, 1, 8),
        position=(-16, 0.1, -11),
    )
    
    objetos.append(jardin3)
    
    jardin4 = Entity(
        model='plane', 
        texture='grass', 
        scale=(13, 1, 8),
        position=(-25, 0.1, 25),
    )
    
    objetos.append(jardin4)
    
    
    

    dona = Entity(
        name='dona',
        model='dona',
        position=(-3, 6, 4),
        scale=8,
        collider='box',
    )
    objetos.append(dona)

    # marmol = Entity(
    #     name='marmol',
    #     model='Marvin',
    #     position=(3, 4, 6),
    #     scale=5,
    #     collider='box',
    # )
    # objetos.append(marmol)
    
    simularAcademica = Entity(
        name='Cubo Rojo Misterioso',
        model='Bicerrectoria',
        position=(2, 8, 43),
        scale=18,
        collider='box',
    )
    objetos.append(simularAcademica)
    
        
    simularEdificioB = Entity(
        name='prueba',
        model='tripo_convert_60c755c2-5aa5-4751-b100-d350fada5a69.obj',
        texture=load_texture('tripo_image_60c755c2-5aa5-4751-b100-d350fada5a69_0.jpg'),
        normal_map=load_texture('tripo_image_60c755c2-5aa5-4751-b100-d350fada5a69_2.jpg'),
        specular_map=load_texture('tripo_image_60c755c2-5aa5-4751-b100-d350fada5a69_Roughness.jpg'),
        position=(65, 6.5, 15),
        rotation=(0, -90, 0),  # (X, Y, Z)
        scale=18,
        collider='box',
    )
    objetos.append(simularEdificioB)

    simularEdificioC = Entity(
        name='prueba',
        model='tripo_convert_60c755c2-5aa5-4751-b100-d350fada5a69.obj',
        texture=load_texture('tripo_image_60c755c2-5aa5-4751-b100-d350fada5a69_0.jpg'),
        normal_map=load_texture('tripo_image_60c755c2-5aa5-4751-b100-d350fada5a69_2.jpg'),
        specular_map=load_texture('tripo_image_60c755c2-5aa5-4751-b100-d350fada5a69_Roughness.jpg'),
        position=(78, 6.5, 50),
        rotation=(0, -90, 0),  # (X, Y, Z)
        scale=18,
        collider='box',
    )
    objetos.append(simularEdificioC)
    
    
    simularEdificioD = Entity(
        name='prueba',
        model='tripo_convert_60c755c2-5aa5-4751-b100-d350fada5a69.obj',
        texture=load_texture('tripo_image_60c755c2-5aa5-4751-b100-d350fada5a69_0.jpg'),
        normal_map=load_texture('tripo_image_60c755c2-5aa5-4751-b100-d350fada5a69_2.jpg'),
        specular_map=load_texture('tripo_image_60c755c2-5aa5-4751-b100-d350fada5a69_Roughness.jpg'),
        position=(98, 6.5, 97),
        rotation=(0, -90, 0),  # (X, Y, Z)
        scale=18,
        collider='box',
    )
    objetos.append(simularEdificioD)
    

    edificioA = Entity(
        name='edificioa',
        model='tripo_convert_f41604c9-e459-4596-a9ab-28cc206424e5.obj',
        texture=load_texture('tripo_image_f41604c9-e459-4596-a9ab-28cc206424e5_0.jpg'),
        specular_map=load_texture('tripo_image_f41604c9-e459-4596-a9ab-28cc206424e5_Roughness.jpg'),
        reflection_map=load_texture('tripo_image_f41604c9-e459-4596-a9ab-28cc206424e5_Metallic.jpg'),
        normal_map=load_texture('tripo_image_f41604c9-e459-4596-a9ab-28cc206424e5_2.jpg'),
        scale=18,
        position=(40, 7.5, -28),
        rotation_y=90,
        collider='box',
    )
    objetos.append(edificioA)


    edificio_marmol  = Entity(
        name='marmol',
        model='tripo_convert_e8b2b1e5-bcd9-4d97-bd22-b546fd7e2e53.obj',
        texture=load_texture('tripo_image_e8b2b1e5-bcd9-4d97-bd22-b546fd7e2e53_0.jpg'),
        specular_map=load_texture('tripo_image_e8b2b1e5-bcd9-4d97-bd22-b546fd7e2e53_Roughness.jpg'),
        reflection_map=load_texture('tripo_image_e8b2b1e5-bcd9-4d97-bd22-b546fd7e2e53_Metallic.jpg'),
        normal_map=load_texture('tripo_image_e8b2b1e5-bcd9-4d97-bd22-b546fd7e2e53_2.jpg'),
        scale=18,
        position=(-3, 4, -35),  # Posición a la izquierda (ajusta el valor -3 si quieres más separación)
        rotation_y=180,
        collider='box',

    )
    objetos.append(edificio_marmol)
    
    
    #Agreagando modelo de edificios

    
    
    arquitectura = Entity(
        model='tripo_convert_18172944-0c20-4a95-89a7-9ce8c63a095b.obj',
        texture=load_texture('tripo_image_18172944-0c20-4a95-89a7-9ce8c63a095b_0.jpg'),
        specular_map=load_texture('tripo_image_18172944-0c20-4a95-89a7-9ce8c63a095b_Roughness.jpg'),
        reflection_map=load_texture('tripo_image_18172944-0c20-4a95-89a7-9ce8c63a095b_Metallic.jpg'),
        normal_map=load_texture('tripo_image_18172944-0c20-4a95-89a7-9ce8c63a095b_2.jpg'),
        scale=20,
        position=(125, 7, 115),
        rotation=(0, 0, 0),  # (X, Y, Z),
        collider='box',
    )
    
    objetos.append(arquitectura)
    
    Hidrante = Entity(
        model='tripo_convert_2c66711a-fbb4-47bb-9d56-a3dcd632778b.obj',
        texture=load_texture('tripo_image_2c66711a-fbb4-47bb-9d56-a3dcd632778b_0.jpg'),
        specular_map=load_texture('tripo_image_2c66711a-fbb4-47bb-9d56-a3dcd632778b_Roughness.jpg'),
        reflection_map=load_texture('tripo_image_2c66711a-fbb4-47bb-9d56-a3dcd632778b_Metallic.jpg'),
        normal_map=load_texture('tripo_image_2c66711a-fbb4-47bb-9d56-a3dcd632778b_2.jpg'),
        scale=3,  # Ajusta el tamaño según sea necesario
        position=(-15, 1.2,-5),  # Cambia la posición si quieres colocarlo en otro lugar
        rotation_y=180,
        collider='box',
    )
    
    objetos.append(Hidrante)
    

    
    edificio_industrial = Entity(
        model='tripo_convert_f6b6a061-bda8-4c8d-b21a-00dd714ed850.obj',
        texture=load_texture('tripo_image_f6b6a061-bda8-4c8d-b21a-00dd714ed850_0.jpg'),
        normal_map=load_texture('tripo_image_f6b6a061-bda8-4c8d-b21a-00dd714ed850_2.jpg'),
        specular_map=load_texture('tripo_image_f6b6a061-bda8-4c8d-b21a-00dd714ed850_Roughness.jpg'),
        reflection_map=load_texture('tripo_image_f6b6a061-bda8-4c8d-b21a-00dd714ed850_Metallic.jpg'),
        scale=(18,18,36),
        position=Vec3(143.5, 8, 162),  # puedes ajustar esta posición si hay colisiones
        rotation_y=-90
    )
    
    objetos.append(edificio_industrial)
    
    casa_asociaciones = Entity(
        model='tripo_convert_2c4f5f80-fd91-4cf6-99f9-d7d3c1f8a457.obj',
        texture=load_texture('tripo_image_2c4f5f80-fd91-4cf6-99f9-d7d3c1f8a457_0.jpg'),
        normal_map=load_texture('tripo_image_2c4f5f80-fd91-4cf6-99f9-d7d3c1f8a457_2.jpg'),
        specular_map=load_texture('tripo_image_2c4f5f80-fd91-4cf6-99f9-d7d3c1f8a457_Roughness.jpg'),
        reflection_map=load_texture('tripo_image_2c4f5f80-fd91-4cf6-99f9-d7d3c1f8a457_Metallic.jpg'),
        scale=10,
        position=Vec3(13, 1.5, 79.5),  # Puedes ajustar la posición según tu escena
        rotation_y=180
    )
    
    mecanica1= Entity(
        name='edificioa',
        model='tripo_convert_f41604c9-e459-4596-a9ab-28cc206424e5.obj',
        texture=load_texture('tripo_image_f41604c9-e459-4596-a9ab-28cc206424e5_0.jpg'),
        specular_map=load_texture('tripo_image_f41604c9-e459-4596-a9ab-28cc206424e5_Roughness.jpg'),
        reflection_map=load_texture('tripo_image_f41604c9-e459-4596-a9ab-28cc206424e5_Metallic.jpg'),
        normal_map=load_texture('tripo_image_f41604c9-e459-4596-a9ab-28cc206424e5_2.jpg'),
        scale=(18,18, 34),
        position=(39.5, 7.5, 112.83),
        rotation_y=-90,
        collider='box',
    )
    objetos.append(mecanica1)


    
    
    
    objetos.append(casa_asociaciones)
    
    objetos.extend(cargar_mesas())
    objetos.extend(cargar_arboles())
    objetos.extend(cargar_basureros())
    
    return objetos
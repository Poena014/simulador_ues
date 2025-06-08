from ursina import *
import os

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
        texture='grass',
        scale=100,
        collider='mesh',
        texture_scale=(10, 10)
    )
    objetos.append(suelo)

    dona = Entity(
        name='Cubo Rojo Misterioso',
        model='dona',
        position=(-3, 4, 4),
        scale=5,
        collider='box',
    )
    objetos.append(dona)
    
    simularAcademica = Entity(
        name='Cubo Rojo Misterioso',
        model='Bicerrectoria',
        position=(2, 4, 43),
        scale=10,
        collider='box',
    )
    objetos.append(simularAcademica)
    
        
    simularEdificioA = Entity(
        name='prueba',
        model='tripo_convert_60c755c2-5aa5-4751-b100-d350fada5a69.obj',
        texture=load_texture('tripo_image_60c755c2-5aa5-4751-b100-d350fada5a69_0.jpg'),
        normal_map=load_texture('tripo_image_60c755c2-5aa5-4751-b100-d350fada5a69_2.jpg'),
        specular_map=load_texture('tripo_image_60c755c2-5aa5-4751-b100-d350fada5a69_Roughness.jpg'),
        position=(51, 3.5, 15),
        rotation=(0, -90, 0),  # (X, Y, Z)
        scale=10,
        collider='box',
    )
    objetos.append(simularEdificioA)
    
    
    
    # dona = Entity(
    #     model='../pruebas/dona_prueba.gltf',  # Ruta al modelo de la dona
    #     scale=1,
    #     #texture='textura.png',
    #     collider='mesh'  # Collider basado en la malla del modelo
    # )
    # objetos.append(dona)
    
    # arbol1  =  Entity(model='Tree1.obj', texture='render1hdcool', scale=0.5)
    
    # objetos.append(arbol1)

    
    

    # Agrega aquí más objetos...

    return objetos
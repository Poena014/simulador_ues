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

    cubo_rojo = Entity(
        name='Cubo Rojo Misterioso',
        model='cube',
        color=color.red,
        position=(5, 0.5, 5),
        scale=(2, 1, 2),
        collider='box',
        texture='white_cube'
    )
    objetos.append(cubo_rojo)
    
    # dona = Entity(
    #     model='../pruebas/dona_prueba.gltf',  # Ruta al modelo de la dona
    #     scale=1,
    #     #texture='textura.png',
    #     collider='mesh'  # Collider basado en la malla del modelo
    # )
    # objetos.append(dona)
    
    arbol1  = Entity(
        model='../pruebas/Tree1.gltf',  # Ruta al modelo de la dona
        scale=1,
        position=(5, 0, 5),
        #texture='textura.png',
        collider='box'  # Collider basado en la malla del modelo
    )
    
    objetos.append(arbol1)
    
    concha  = Entity(
        model='../pruebas/Concha1.glb',  # Ruta al modelo de la dona
        scale=1,
        #EJE X, Z, Y
        position=(10, 0, 5),
        #texture='textura.png',
        collider='box'  # Collider basado en la malla del modelo
    )
    
    objetos.append(concha)
    
    

    # Agrega aquí más objetos...

    return objetos
# maquina de flexiones.py

from sesion_flexiones import Usuario, Objetivo, SesionDeFlexiones

# Creamos un usuario
mi_usuario = Usuario("Carlos", 25, "12345678")

# Creamos un objetivo de flexiones
mi_objetivo = Objetivo(30)

# Creamos una sesión de flexiones para ese usuario
mi_sesion = SesionDeFlexiones(mi_usuario, mi_objetivo)

# Iniciamos el proceso de sesión, simulando el flujo como en el ejemplo del horno
print(f"Bienvenido, {mi_usuario.get_nombre()}.\nEstado inicial de la sesión:")
print(mi_sesion)

# Simulamos la realización de flexiones y controlamos el estado
try:
    for _ in range(30):  # Hacemos 30 flexiones, completando el objetivo
        mi_sesion.agregar_flexion()
        print(f"Progreso de flexiones: {mi_sesion}")
except RuntimeError as e:
    print(e)

# Verificamos el estado de la sesión al final
print("\nEstado final de la sesión:")
print(mi_sesion)

# Verificamos si el usuario es mayor de edad
if mi_usuario.es_mayor_edad():
    print(f"{mi_usuario.get_nombre()} es mayor de edad.")
else:
    print(f"{mi_usuario.get_nombre()} es menor de edad.")

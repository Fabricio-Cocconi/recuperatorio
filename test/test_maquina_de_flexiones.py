# test_maquina_de_flexiones.py

import pytest
from sesion_flexiones import Usuario, Objetivo, SesionDeFlexiones

def test_flujo_maquina_de_flexiones():
    # Creamos el usuario y el objetivo
    mi_usuario = Usuario("Carlos", 25, "12345678")
    mi_objetivo = Objetivo(30)
    mi_sesion = SesionDeFlexiones(mi_usuario, mi_objetivo)

    # Verificamos que el estado inicial de la sesión es "Iniciada"
    assert mi_sesion.get_estado_sesion() == "Iniciada"

    # Realizamos 30 flexiones y verificamos que la sesión se completa
    for _ in range(30):
        mi_sesion.agregar_flexion()

    assert mi_sesion.get_estado_sesion() == "Finalizada"

    # Verificamos que se han realizado exactamente 30 flexiones
    assert mi_sesion.get_flexiones_realizadas() == 30

    # Verificamos si el usuario es mayor de edad
    assert mi_usuario.es_mayor_edad() == True  # El usuario tiene 25 años, es mayor de edad

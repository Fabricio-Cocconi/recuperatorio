# test_sesion_flexiones.py

import pytest
from sesion_flexiones import Usuario, Objetivo, SesionDeFlexiones

def test_usuario():
    usuario = Usuario("Carlos", 25, "12345678")

    assert usuario.get_nombre() == "Carlos"
    assert usuario.es_mayor_edad() == True  # Usuario mayor de edad

def test_objetivo():
    objetivo = Objetivo(30)
    
    assert objetivo.get_flexiones() == 30  # El objetivo son 30 flexiones

def test_sesion_flexiones():
    usuario = Usuario("Carlos", 25, "12345678")
    objetivo = Objetivo(30)
    sesion = SesionDeFlexiones(usuario, objetivo)
    
    # Estado inicial de la sesión
    assert sesion.get_estado_sesion() == "Iniciada"
    
    # Simulación de flexiones
    for _ in range(30):
        sesion.agregar_flexion()
    
    # Después de 30 flexiones, la sesión debe estar finalizada
    assert sesion.get_estado_sesion() == "Finalizada"

def test_sesion_flexiones_exceder():
    usuario = Usuario("Carlos", 25, "12345678")
    objetivo = Objetivo(10)  # Solo 10 flexiones en el objetivo
    sesion = SesionDeFlexiones(usuario, objetivo)
    
    # Intentamos agregar 11 flexiones
    for _ in range(10):
        sesion.agregar_flexion()
    
    with pytest.raises(RuntimeError):
        sesion.agregar_flexion()  # Debería lanzar un error porque la sesión ya está finalizada

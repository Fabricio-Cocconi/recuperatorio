# sesion_flexiones.py

class Usuario:
    def __init__(self, nombre, edad, DNI):
        self.__nombre = nombre
        self.__edad = edad
        self.__DNI = DNI

    def get_nombre(self):
        return self.__nombre

    def es_mayor_edad(self):
        return self.__edad >= 18

    def __str__(self):
        return f"Usuario: {self.__nombre}, Edad: {self.__edad}, DNI: {self.__DNI}"


class Objetivo:
    def __init__(self, flexiones):
        self.__flexiones = flexiones

    def get_flexiones(self):
        return self.__flexiones

    def __str__(self):
        return f"Objetivo: {self.__flexiones} flexiones"


class SesionDeFlexiones:
    def __init__(self, usuario, objetivo):
        self.__usuario = usuario
        self.__objetivo = objetivo
        self.__flexiones_realizadas = 0
        self.__estado_sesion = "Iniciada"

    def agregar_flexion(self):
        if self.__estado_sesion == "Iniciada":
            self.__flexiones_realizadas += 1
            if self.__flexiones_realizadas >= self.__objetivo.get_flexiones():
                self.__estado_sesion = "Finalizada"
        else:
            raise RuntimeError("La sesión ya está finalizada.")

    def get_estado_sesion(self):
        return self.__estado_sesion

    def __str__(self):
        estado_objetivo = "Alcanzado" if self.__estado_sesion == "Finalizada" else "No Alcanzado"
        return (f"{self.__usuario.get_nombre()}\n"
                f"Flexiones realizadas: {self.__flexiones_realizadas}\n"
                f"Objetivo: {self.__objetivo.get_flexiones()} flexiones\n"
                f"Estado de la sesión: {self.__estado_sesion}\n"
                f"Estado del objetivo: {estado_objetivo}")

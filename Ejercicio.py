# IMPORTAR UNA CLASE DE UN MÓDULO, CREAR UNA INSTANCIA DE LA CLASE Y LLAMAR UN MÉTODO
#
from Cl_persona import Cl_persona

#per = Cl_persona("Ricardo", "González")
#per.saludo()
#
# HERENCIA
class Cl_estudiante(Cl_persona):
    def __init__(self, nombre, apellido, carrera, semestre):
        super().__init__(nombre, apellido)
        self.carrera = carrera
        self.semestre = semestre

    def darDatos(self):
        print(f'''
              ¿Hola! Mi nombre es {self.nombre} {self.apellido}, 
              y soy estudiante de {self.carrera} del semestre {self.semestre}
            ''')

per = Cl_estudiante("Ricardo", "González", "Informática", 4)
per.darDatos()
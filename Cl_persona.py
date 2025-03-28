class Cl_persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def saludo(self):
            print(f"¡Hola!, yo soy {self.nombre} {self.apellido}")
    
#per = Cl_persona("Ricardo", "González")
#per.saludo()

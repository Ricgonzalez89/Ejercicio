class Cl_personaDescriptor:
     
    def __set_name__(self, owner, name):
         self.nombre_publico = name
         self.nombre_privado = "_" + name
    
    def __get__(self, instance, owner=None):
       print(f"Getter llamado para el atributo: {self.nombre_publico}")
       valor = getattr(instance, self.nombre_privado)
       return valor
    
    def __set__(self, instance, value):
       print(f"Setter llamado para el atributo: {self.nombre_publico}")
       setattr(instance, self.nombre_privado, value)

    def __delete__(self, instance):
        print(f"Delete llamado para el atributo {self.nombre_publico}")
        delattr(instance, self.nombre_privado)

class Cl_persona:

    nombre = Cl_personaDescriptor()
    apellido = Cl_personaDescriptor()
    edad = Cl_personaDescriptor()

    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def saludo(self):
            print(f"¡Hola!, yo soy {self.nombre} {self.apellido} y tengo {self.edad} años.")
    
per = Cl_persona("Ricardo", "González", 21)
per.saludo()

print(per.nombre)
del per.edad
print(vars(per))

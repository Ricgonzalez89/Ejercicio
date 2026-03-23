# Clase Descriptora: Permite gestionar el acceso a los atributos de la clase Cl_persona.
class Cl_personaDescriptor:
     
    # Método especial: Permite saber el atributo específico al que se asocia el descriptor. 
    # owner -> Clase donde se usa el descriptor.
    # name -> Nombre de la variable de clase a la que se asocia el descriptor.
    def __set_name__(self, owner, name):
         self.nombre_publico = name
         self.nombre_privado = "_" + name
    
    # Getter: Llamado al retornar el valor de un atributo de una instancia.
    def __get__(self, instance, owner=None):
       print(f"Getter llamado para el atributo: {self.nombre_publico}")
       valor = getattr(instance, self.nombre_privado)
       return valor
    
    # Setter: Llamado al definir el valor de un atributo de una instancia.
    def __set__(self, instance, value):
       print(f"Setter llamado para el atributo: {self.nombre_publico}")
       setattr(instance, self.nombre_privado, value)

    # Delete: Invocado al eliminar un atributo de una clase.
    def __delete__(self, instance):
        print(f"Delete llamado para el atributo {self.nombre_publico}")
        delattr(instance, self.nombre_privado)

# Clase destino, donde se implementan los descriptores.
class Cl_persona:

    # Variables de clase. Son las instancias de la clase descriptora, una por cada atributo.
    # Cuando se acceda a alguno de los atributos, el intérprete buscará los métodos de los
    # descriptores, no los predeterminados.
    nombre = Cl_personaDescriptor()
    apellido = Cl_personaDescriptor()
    edad = Cl_personaDescriptor()

    # Cosntructor de la clase Cl_persona. Sus atributos tienen el mismo nombre que las variables
    # anteriores.
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    # Método común, usa los valores de los tres atributos de Cl_persona.
    def saludo(self):
            print(f"¡Hola!, yo soy {self.nombre} {self.apellido} y tengo {self.edad} años.")
    
# Creación de una instancia de Cl_persona e invocación de su método común.
per = Cl_persona("Ricardo", "González", 21)
per.saludo()

# Ejemplos varios del acceso a atributos y las variables de la instancia.
print(per.nombre)
del per.edad
print(vars(per))

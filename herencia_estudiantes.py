# Clase base: Estudiante
class Estudiante:
    """
    Clase base que representa a un estudiante general.
    Contiene atributos comunes como nombre, edad y matrícula.
    """
    def __init__(self, nombre, edad, matricula):
        self.nombre = nombre
        self.edad = edad
        self.matricula = matricula

    def mostrar_informacion(self):
        """
        Método para mostrar la información general del estudiante.
        Puede ser sobrescrito por las subclases si necesitan mostrar más datos.
        """
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Matrícula: {self.matricula}")


# Clase derivada: EstudianteUniversitario
class EstudianteUniversitario(Estudiante):
    """
    Clase derivada que hereda de Estudiante.
    Representa a un estudiante universitario con carrera y semestre.
    """
    def __init__(self, nombre, edad, matricula, carrera, semestre):
        super().__init__(nombre, edad, matricula)  # Reutiliza constructor de la clase base
        self.carrera = carrera
        self.semestre = semestre

    def mostrar_informacion(self):
        """
        Sobrescribe el método mostrar_informacion para incluir más datos.
        """
        super().mostrar_informacion()
        print(f"Carrera: {self.carrera}")
        print(f"Semestre: {self.semestre}")

    def cambiar_semestre(self, nuevo_semestre):
        """
        Método exclusivo de esta subclase para cambiar el semestre.
        """
        self.semestre = nuevo_semestre
        print(f"El semestre ha sido actualizado a: {self.semestre}")


# Clase derivada: EstudiantePreparatoria
class EstudiantePreparatoria(Estudiante):
    """
    Clase derivada que hereda de Estudiante.
    Representa a un estudiante de preparatoria con especialidad.
    """
    def __init__(self, nombre, edad, matricula, especialidad):
        super().__init__(nombre, edad, matricula)
        self.especialidad = especialidad

    def mostrar_informacion(self):
        """
        Método sobrescrito para agregar la especialidad del estudiante de preparatoria.
        """
        super().mostrar_informacion()
        print(f"Especialidad: {self.especialidad}")

    def cambiar_especialidad(self, nueva_especialidad):
        """
        Método exclusivo para cambiar la especialidad.
        """
        self.especialidad = nueva_especialidad
        print(f"La especialidad ha sido cambiada a: {self.especialidad}")


# Función principal: aquí se prueban las clases
def main():
    print("=== Estudiante Universitario ===")
    uni = EstudianteUniversitario("Ana López", 20, "U001", "Ingeniería en Software", 4)
    uni.mostrar_informacion()
    print("\nActualizando semestre...")
    uni.cambiar_semestre(5)

    print("\n=== Estudiante de Preparatoria ===")
    prep = EstudiantePreparatoria("Carlos Ruiz", 17, "P045", "Físico-Matemáticas")
    prep.mostrar_informacion()
    print("\nCambiando especialidad...")
    prep.cambiar_especialidad("Químico-Biológicas")


# Ejecutar el programa
if __name__ == "__main__":
    main()

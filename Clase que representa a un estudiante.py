# Clase que representa a un estudiante
class Estudiante:
    def __init__(self, nombre, edad, matricula):
        # Constructor de la clase Estudiante
        self.nombre = nombre
        self.edad = edad
        self.matricula = matricula

    def mostrar_informacion(self):
        # Método que muestra los datos del estudiante
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Matrícula: {self.matricula}")

    def actualizar_edad(self, nueva_edad):
        # Método para actualizar la edad del estudiante
        self.edad = nueva_edad
        print(f"Edad actualizada a: {self.edad}")


# Función principal del programa
def main():
    # Instanciación de objetos
    estudiante1 = Estudiante("Ana López", 20, "A001")
    estudiante2 = Estudiante("Carlos Ruiz", 22, "A002")

    # Mostrar información de los estudiantes
    print("Información del Estudiante 1:")
    estudiante1.mostrar_informacion()

    print("\nInformación del Estudiante 2:")
    estudiante2.mostrar_informacion()

    # Actualizar edad del segundo estudiante
    print("\nActualizando edad del Estudiante 2...")
    estudiante2.actualizar_edad(23)


# Verifica que se ejecute solo si es el programa principal
if __name__ == "__main__":
    main()

def programacion_tradicional():
    """
    Implementación usando Programación Tradicional.
    """

    # Función para ingresar las temperaturas diarias
    def ingresar_temperaturas():
        temperaturas = []
        for i in range(7):  # 7 días de la semana
            temp = float(input(f"Ingrese la temperatura del día {i + 1} (Tradicional): "))
            temperaturas.append(temp)
        return temperaturas

    # Función para calcular el promedio semanal
    def calcular_promedio(temperaturas):
        return sum(temperaturas) / len(temperaturas)

    # Ejecución del enfoque tradicional
    print("\n=== Promedio Semanal del Clima (Programación Tradicional) ===")
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    print(f"El promedio semanal de temperaturas es: {promedio:.2f} °C\n")


class ClimaSemanal:
    """
    Implementación usando Programación Orientada a Objetos.
    """

    def __init__(self):
        # Lista para almacenar las temperaturas diarias
        self.temperaturas = []

    def ingresar_temperaturas(self):
        """Método para ingresar las temperaturas diarias."""
        for i in range(7):  # 7 días de la semana
            temp = float(input(f"Ingrese la temperatura del día {i + 1} (POO): "))
            self.temperaturas.append(temp)

    def calcular_promedio(self):
        """Método para calcular el promedio semanal."""
        if not self.temperaturas:
            raise ValueError("No hay temperaturas ingresadas.")
        return sum(self.temperaturas) / len(self.temperaturas)


def programacion_poo():
    """
    Ejecución usando Programación Orientada a Objetos.
    """
    print("\n=== Promedio Semanal del Clima (Programación Orientada a Objetos) ===")
    clima = ClimaSemanal()  # Crear instancia de la clase
    clima.ingresar_temperaturas()
    promedio = clima.calcular_promedio()
    print(f"El promedio semanal de temperaturas es: {promedio:.2f} °C\n")


def main():
    """
    Menú principal para seleccionar el enfoque a ejecutar.
    """
    while True:
        print("=== Comparación de Programación Tradicional y POO ===")
        print("1. Programación Tradicional")
        print("2. Programación Orientada a Objetos")
        print("3. Salir")
        opcion = input("Seleccione una opción (1-3): ")

        if opcion == "1":
            programacion_tradicional()
        elif opcion == "2":
            programacion_poo()
        elif opcion == "3":
            print("¡Gracias por usar el programa!")
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.\n")


if __name__ == "__main__":
    main()

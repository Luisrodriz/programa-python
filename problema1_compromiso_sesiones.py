"""
Universidad Nacional Abierta y a Distancia - UNAD
Curso: Fundamentos de Programación (213022)
Fase 5 - Evaluación Final POA
Problema 1: Nivel de compromiso de sesiones de clientes

Autor: Luis Ariel Rodríguez Paredes
"""

# ---------------------------------------------------------------
# CONSTANTES (umbrales de la lógica de negocio)
# ---------------------------------------------------------------
DURACION_ALTA = 180   # segundos: para "Alto" la duración debe ser MAYOR a este valor
CLICS_ALTOS = 8       # clics: para "Alto" los clics deben ser MAYORES a este valor
DURACION_BAJA = 60    # segundos: "Bajo" si la duración es MENOR a este valor
CLICS_BAJOS = 3       # clics: "Bajo" si los clics son MENORES a este valor


# ---------------------------------------------------------------
# MÓDULO (función) que clasifica el compromiso de UNA sesión
# ---------------------------------------------------------------
def clasificar_compromiso(duracion, clics):
    """Recibe la duración (segundos) y el número de clics de una sesión
    y devuelve "Alto", "Medio" o "Bajo"."""
    if duracion > DURACION_ALTA and clics > CLICS_ALTOS:
        return "Alto"
    elif duracion < DURACION_BAJA or clics < CLICS_BAJOS:
        return "Bajo"
    else:
        return "Medio"


# ---------------------------------------------------------------
# PROGRAMA PRINCIPAL
# ---------------------------------------------------------------
def main():
    # Matriz de datos: [ID del Cliente, Duración (segundos), Número de clics]
    sesiones = [
        [101, 240, 12],   # Alto
        [102, 45, 10],    # Bajo (duración < 60)
        [103, 120, 5],    # Medio
        [104, 500, 20],    # Bajo (clics < 3)
        [105, 181, 9],    # Alto (justo por encima de los límites)
        [106, 180, 8],    # Medio (justo en el límite, no supera)
        [107, 60, 3],     # Medio (justo en el límite, no es menor)
    ]

    # Contadores para el resumen final
    cantidad_alto = 0
    cantidad_medio = 0
    cantidad_bajo = 0

    # Encabezado del informe
    print("=" * 40)
    print("   INFORME DE COMPROMISO DE SESIONES")
    print("=" * 40)
    print(f"{'ID Cliente':<12}{'Clasificación':<15}")
    print("-" * 40)

    # Recorrer la matriz fila por fila (estructura repetitiva)
    for fila in sesiones:
        id_cliente = fila[0]
        duracion = fila[1]
        clics = fila[2]

        clasificacion = clasificar_compromiso(duracion, clics)

        print(f"{id_cliente:<12}{clasificacion:<15}")

        # Actualizar contadores
        if clasificacion == "Alto":
            cantidad_alto += 1
        elif clasificacion == "Medio":
            cantidad_medio += 1
        else:
            cantidad_bajo += 1

    # Resumen
    print("-" * 40)
    print(f"Total de sesiones: {len(sesiones)}")
    print(f"Alto: {cantidad_alto} | Medio: {cantidad_medio} | Bajo: {cantidad_bajo}")


# Punto de entrada del programa
if __name__ == "__main__":
    main()

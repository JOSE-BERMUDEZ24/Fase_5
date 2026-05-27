# Curso: Fundamentos de Programación (Código: 213022)
# Fase 5 - Evaluación Final POA

def clasificar_jornada(nombre, lunes, martes, viernes):
    """
    Módulo para calcular la suma de horas semanales y clasificar la jornada.
    """
    # Lógica de negocio: Calcular la suma de horas
    total_horas = lunes + martes + viernes
    
    # Clasificar según el umbral de 40 horas
    if total_horas > 40:
        clasificacion = "Sobretiempo"
    else:
        clasificacion = "Horario Estándar"
        
    return total_horas, clasificacion

def menu_principal():
    # Datos Iniciales: Matriz con 4 recursos y sus horas (Lu, Ma, Vi)
    # Formato: [Nombre, Lunes, Martes, Viernes]
    matriz_recursos = [
        ["Ana Martínez", 8, 9, 8],
        ["Carlos Pérez", 12, 15, 14],
        ["Luisa Gómez", 8, 8, 8],
        ["Jorge Ruiz", 10, 12, 20]
    ]
    
    print("=" * 60)
    print("      INFORME DE CONTROL DE HORAS SEMANALES")
    print("=" * 60)
    print(f"{'Nombre':<18}{'Total Horas':<15}{'Clasificación':<18}")
    print("-" * 60)
    
    # Estructura repetitiva para recorrer la matriz
    for recurso in matriz_recursos:
        nombre = recurso[0]
        lu = recurso[1]
        ma = recurso[2]
        vi = recurso[3]
        
        # Llamado al módulo / función
        total, clase = clasificar_jornada(nombre, lu, ma, vi)
        
        # Salida de datos requerida
        print(f"{nombre:<18}{total:<15}{clase:<18}")
        
    print("=" * 60)

if __name__ == "__main__":
    menu_principal()
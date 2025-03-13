import math

def is_equal(x, y, epsilon=1e-9):
    return abs(x - y) < epsilon

def calculate_angles(a, b, c):
    # Calcula los ángulos usando la Ley de Cosenos con protección para valores fuera de rango
    def safe_acos(value):
        return math.acos(max(min(value, 1.0), -1.0))
    
    angle_a = math.degrees(safe_acos((b**2 + c**2 - a**2) / (2 * b * c)))
    angle_b = math.degrees(safe_acos((a**2 + c**2 - b**2) / (2 * a * c)))
    angle_c = math.degrees(safe_acos((a**2 + b**2 - c**2) / (2 * a * b)))
    
    return angle_a, angle_b, angle_c

def main():
    sides = list(map(float, input("Ingrese los tres lados del triángulo separados por espacios: ").split()))
    
    if len(sides) != 3:
        print("Error: Debe ingresar exactamente tres valores.")
        return
    
    a, b, c = sides
    if any(side <= 0 for side in sides):
        print("Error: Todos los lados deben ser valores positivos.")
        return
    
    sorted_sides = sorted(sides)
    a_sorted, b_sorted, c_sorted = sorted_sides
    
    if a_sorted + b_sorted <= c_sorted:
        print("Los lados ingresados no forman un triángulo válido.")
        return
    
    # Determinar tipo por lados
    if is_equal(a_sorted, b_sorted) and is_equal(b_sorted, c_sorted):
        side_type = "Equilátero"
    elif is_equal(a_sorted, b_sorted) or is_equal(b_sorted, c_sorted):
        side_type = "Isósceles"
    else:
        side_type = "Escaleno"
    
    # Calcular ángulos
    angle_a, angle_b, angle_c = calculate_angles(a_sorted, b_sorted, c_sorted)
    
    # Determinar tipo por ángulos
    max_angle = max(angle_a, angle_b, angle_c)
    epsilon = 1e-5
    
    if abs(max_angle - 90.0) < epsilon:
        angle_type = "Rectángulo"
    elif max_angle > 90.0:
        angle_type = "Obtusángulo"
    else:
        angle_type = "Acutángulo"
    
    # Imprimir resultados
    print("\nResultados:")
    print(f"Lados: {a}, {b}, {c}")
    print(f"Ángulos: {angle_a:.2f}°, {angle_b:.2f}°, {angle_c:.2f}°")
    print(f"Clasificación por lados: {side_type}")
    print(f"Clasificación por ángulos: {angle_type}")

if __name__ == "__main__":
    main()
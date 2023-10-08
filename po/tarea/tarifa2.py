def calcular_tarifa(dia_semana, tiempo_estacionado):
    # Definir las tarifas por día de la semana
    tarifas = {
        "lunes": 2.00,
        "martes": 2.00,
        "miércoles": 2.00,
        "jueves": 2.50,
        "viernes": 2.50,
        "sábado": 3.00,
        "domingo": 3.00
    }
    
    # Definir el límite de tiempo establecido (en minutos)
    tiempo_limite = 60
    
    # Validar que el día de la semana sea válido
    dia_semana = dia_semana.lower()
    if dia_semana not in tarifas:
        return "Error: Día de la semana no válido"
    
    # Validar que el tiempo estacionado sea un número positivo
    if tiempo_estacionado < 0:
        return "Error: El tiempo estacionado debe ser un número positivo"
    
    # Validar si se supera el límite de tiempo
    if tiempo_estacionado > tiempo_limite:
        return "Error: Se ha excedido el límite de tiempo establecido"
    
    # Calcular la tarifa basada en el tiempo estacionado
    tarifa_por_hora = tarifas[dia_semana]
    total_a_pagar = tarifa_por_hora
    
    return total_a_pagar

try:
    # Solicitar al usuario el día de la semana y el tiempo estacionado en minutos
    dia_semana = input("Ingrese el día de la semana: ")
    tiempo_estacionado = int(input("Ingrese el tiempo estacionado en minutos: "))
    
    # Calcular y mostrar la tarifa
    resultado = calcular_tarifa(dia_semana, tiempo_estacionado)
    print(f"Total a pagar: ${resultado:.2f}")
except ValueError:
    print("Error: Ingrese un valor numérico válido para el tiempo estacionado.")

    #este codigo lo hice adicional, solo prueba. 

    #leider manuel blanco

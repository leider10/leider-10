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
    
    # ingresar que el día de la semana sea válido
    dia_semana = dia_semana.lower()
    if dia_semana not in tarifas:
        return "Error: Día de la semana no válido"
    
    # Calcular la tarifa basada en el tiempo estacionado
    tarifa_por_hora = tarifas[dia_semana]
    fraccion_de_hora = tiempo_estacionado % 60 > 5
    
    if fraccion_de_hora:
        tiempo_estacionado += 60 - (tiempo_estacionado % 60)
    
    total_a_pagar = (tiempo_estacionado // 60) * tarifa_por_hora
    
    return total_a_pagar

try:
    # Solicitar al usuario el día de la semana y el tiempo estacionado en minutos
    dia_semana = input("Ingrese el día de la semana: ")
    tiempo_estacionado = int(input("Ingrese el tiempo estacionado en minutos: "))

    # Calcular y mostrar la tarifa
    resultado = calcular_tarifa(dia_semana, tiempo_estacionado)
    print(f"Total a pagar: ${resultado:.2f}")
except ValueError:
    print("Error: Ingrese un valor válido para el tiempo estacionado.")

    #leider manuel blanco
    
def optimizar_pipeline(suites, tiempo_maximo):
    """
    Algoritmo de Programación Dinámica: El Problema de la Mochila (0/1 Knapsack)
    Problema a solucionar: Maximizar el valor de cobertura de pruebas automatizadas
    sin exceder un límite de tiempo estricto en el pipeline.
    """
    n = len(suites)
    
    # 1. Definición del estado o subproblemas (Matriz dp)
    dp = [[0 for _ in range(tiempo_maximo + 1)] for _ in range(n + 1)]

    # 2. Manejo de los casos base:
    for i in range(1, n + 1):
        nombre, tiempo, valor = suites[i-1]
        for w in range(1, tiempo_maximo + 1):
            if tiempo <= w:
                # 4. Relación de recurrencia
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-tiempo] + valor)
            else:
                dp[i][w] = dp[i-1][w]

    # 5. Reconstrucción de la solución para identificar las herramientas elegidas
    resultado_maximo = dp[n][tiempo_maximo]
    tiempo_restante = tiempo_maximo
    suites_seleccionadas = []

    for i in range(n, 0, -1):
            if resultado_maximo <= 0:
                break
            if resultado_maximo == dp[i-1][tiempo_restante]:
                continue
            else:
                suites_seleccionadas.append(suites[i-1])
                nombre, tiempo, valor = suites[i-1]
                resultado_maximo -= valor
                tiempo_restante -= tiempo

        tiempo_usado = sum([s[1] for s in suites_seleccionadas])

        # Formatear la lista de diccionarios para la respuesta
        suites_formateadas = [
            {"suite": s[0], "tiempo_minutos": s[1], "valor_mitigacion": s[2]}
            for s in reversed(suites_seleccionadas) # Invertir para mantener orden lógico
        ]

        return dp[n][tiempo_maximo], suites_formateadas, tiempo_usado
    
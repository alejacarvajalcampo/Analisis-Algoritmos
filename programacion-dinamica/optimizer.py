# optimizer.py

def optimizar_pipeline(suites, tiempo_maximo):
    """
    Algoritmo de Programación Dinámica: El Problema de la Mochila (0/1 Knapsack)
    """
    n = len(suites)
    
    dp = [[0 for _ in range(tiempo_maximo + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        nombre, tiempo, valor = suites[i-1]
        for w in range(1, tiempo_maximo + 1):
            if tiempo <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-tiempo] + valor)
            else:
                dp[i][w] = dp[i-1][w]

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
    
    suites_formateadas = [
        {"suite": s[0], "tiempo_minutos": s[1], "valor_mitigacion": s[2]} 
        for s in reversed(suites_seleccionadas)
    ]
    
    return dp[n][tiempo_maximo], suites_formateadas, tiempo_usado
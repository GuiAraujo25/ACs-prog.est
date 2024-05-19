def calcular_fracao_populacao():
    import sys
    input = sys.stdin.read
    from collections import defaultdict

    data = input().strip().split("\n")
    N = int(data[0].strip())
    
    index = 2
    resultados = []

    for _ in range(N):
        especies = defaultdict(int)
        total_arvores = 0

        while index < len(data) and data[index].strip():
            especie = data[index].strip()
            especies[especie] += 1
            total_arvores += 1
            index += 1
        
        index += 1  

        resultado = []
        for especie in sorted(especies):
            fracao = (especies[especie] / total_arvores) * 100
            resultado.append(f"{especie} {fracao:.4f}")
        
        resultados.append("\n".join(resultado))

    print("\n\n".join(resultados))

calcular_fracao_populacao()
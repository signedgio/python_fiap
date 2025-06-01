# SmartWind Guardian:

print("Digite as leituras de vento, direção e umidade.")
print("Digite 'sair' para encerrar.")

velocidades = []
direcoes = []
umidades = []
leituras_criticas = 0

while True:
    entrada = input("Velocidade do vento (ou 'sair'): ")
    if entrada.lower() == 'sair':
        break

    vento = float(entrada)
    direcao1 = int(input("Direção anterior do vento em graus: "))
    direcao2 = int(input("Direção atual do vento em graus: "))
    umidade = float(input("Umidade do ar em porcentagem: "))

    if direcao1 > direcao2:
        direcao_total = direcao1 - direcao2
    else:
        direcao_total = direcao2 - direcao1

    # listas:
    velocidades.append(vento)
    direcoes.append(direcao_total)
    umidades.append(umidade)

    if vento > 75:
        print("Condição crítica: o vento está acima de 75km/h. Tome cuidado!")
    else:
        print("Tudo certo por aqui :)")

    if direcao_total > 100:
        print("Condição crítica: a direção do vento está acima de 100 graus. Tome cuidado!")
    else:
        print("Tudo certo por aqui :)")

    if umidade < 20:
        print("Condição crítica: a umidade está abaixo de 20%. Tome cuidado!")
    elif umidade > 95:
        print("Condição crítica: a umidade está acima de 95%. Tome cuidado!")
    else:
        print("Tudo certo por aqui :)")

    if vento > 75 or direcao_total > 100 or umidade < 20 or umidade > 95:
        print("Alerta: Condições de vento severo identificadas!\n")
        leituras_criticas += 1
    else:
        print("Sistema estável. Nenhuma anomalia detectada.\n")

if len(velocidades) == 0:
    print("Nenhuma leitura foi feita.")
else:
    n = len(velocidades)

    # Calcula médias
    media_vento = sum(velocidades) / n
    media_direcao = sum(direcoes) / n
    media_umidade = sum(umidades) / n

    # Desvio padrão:
    dp_vento = (sum((v - media_vento) ** 2 for v in velocidades) / n) ** 0.5
    dp_direcao = (sum((d - media_direcao) ** 2 for d in direcoes) / n) ** 0.5
    dp_umidade = (sum((u - media_umidade) ** 2 for u in umidades) / n) ** 0.5

    # Estado geral
    porcentagem_critica = (leituras_criticas / n) * 100
    estado = "Instável" if porcentagem_critica > 40 else "Estável"

    # Tendência da velocidade do vento
    if velocidades[-1] > velocidades[0]:
        tendencia = "Aumentando"
    elif velocidades[-1] < velocidades[0]:
        tendencia = "Diminuindo"
    else:
        tendencia = "Estável"

    print(f"Total de leituras: {n}")
    print(f"Leituras críticas: {leituras_criticas} ({porcentagem_critica:.1f}%)")
    print(f"Estado Geral: {estado}\n")

    print(f"Média do vento: {media_vento:.2f} km/h | Desvio padrão: {dp_vento:.2f}")
    print(f"Mínimo / Máximo vento: {min(velocidades)} / {max(velocidades)}\n")

    print(f"Média da variação da direção: {media_direcao:.2f}° | Desvio padrão: {dp_direcao:.2f}")
    print(f"Mínimo / Máximo variação da direção: {min(direcoes)} / {max(direcoes)}\n")

    print(f"Média da umidade: {media_umidade:.2f}% | Desvio padrão: {dp_umidade:.2f}")
    print(f"Mínimo / Máximo umidade: {min(umidades)} / {max(umidades)}\n")

    print(f"Tendência da velocidade do vento: {tendencia}")


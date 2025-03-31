distancia = float(input("qual é a distância a ser percorrida em km?: "))
velocidade_media= float(input("qual a velocidade do veículo em km/h?: "))

tempo = distancia / velocidade_media
print(f"este é o tempo do percurso: {tempo:.2f} horas" )
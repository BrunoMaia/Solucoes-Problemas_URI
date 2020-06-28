''' De volta à faculdade de física

Uma partícula tem velocidade inicial e aceleração constante. Se a sua velocidade após certo momento é v então qual será seu deslocamento no dobro deste tempo?
'''
# equação => s' = s + v.dt
# dt = 2 * t 
# cria o loop de verificação e retorna o resultado para cada linha
while True:
    try:
        entrada = input()
        entrada = (entrada.split())
        velocidade = int(entrada[0])
        tempo = int(entrada[1])
        if (velocidade >= -100 and velocidade <= 100) and (tempo >= 0 and tempo <=200):
            resultado = int(velocidade*(tempo*2))
            print(resultado)
        else:
            raise ValueError
    except EOFError:
        break
    

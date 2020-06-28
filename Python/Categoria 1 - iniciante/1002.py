'''Área do círculo'''
PI = 3.14159
raio = round((float(input())),2)

def CalculaAreaCirculo(pi:float, raio:float):
    area = (raio**2)*pi
    area = round(area,4)
    return ('A={:.4f}'.format(area))

print(CalculaAreaCirculo(PI,raio))
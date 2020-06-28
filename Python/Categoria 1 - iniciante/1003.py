'''Soma Simples'''
A = int(input())
B = int(input())

def CalculaSomaSimples(a: int, b: int):
    resultado = int(a+b)
    return('SOMA = {}'.format(resultado))

print(CalculaSomaSimples(A,B))

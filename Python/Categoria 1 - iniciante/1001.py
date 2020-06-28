'''
Primeiro exercício
'''
A = int(input())
B = int(input())
def CalculaSoma(A: int, B:int):
    resultado = int(A + B)
    return ('X = {}'.format(resultado))
print(CalculaSoma(A,B))

def soma_pascal(vetor):
    n = len(vetor)
    soma = 0
    for i in range(n):
        # range(n) -> [0, 1, 2, .. n]
        soma = soma + vetor[i]
    return soma

def soma_python(vetor):
    soma = 0
    for valor in vetor:
        soma += valor
    return soma

def soma_python2(vetor):
    sum(vetor)


def soma_python3(vetor):
    return sum(valor for valor in vetor)


#3
#def soma_elegante():
    #

vetor = [1, 2, 3, 4, 5, -1]
soma_pascal_ = soma_pascal(vetor)
print('A soma pascal do vetor eh', soma_pascal_)

soma_python_ = soma_python(vetor)
print('A soma python do vetor eh', soma_python_)



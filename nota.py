NF = input('Entre com a nota final do aluno: ')
print('Nota final do aluno', NF)
tipo_da_nf = type(NF)
# print('Tipo do NF', tipo_da_nf)
# print('Tipo do NF', type(NF))

NF = float(NF)
# print('Tipo do NF', type(NF))

# MF = input('digite um valor: ')
# print('Nota do aluno', MF)


if NF >= 6.0:
    print('aprovado')
else:
    print('Aluno precisa de uma nota de exame')
    MF = input('Nota do final do aluno: ')
    print('Nota do final do aluno', MF)
    if MF >= 5.0:
        print('aprovado')



#elif MF >= 5.0:
#    print('aprovado')
#else:
#    print('reprovado')


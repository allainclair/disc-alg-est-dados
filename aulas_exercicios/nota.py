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
    print('Aluno precisa de uma nota de media final')
    MF = input('Media do final do aluno: ')
    print('Nota da Media Final do aluno', MF)
    # MF = float(MF)
    if float(MF) >= 5.0:
        print('aprovado')
    else:
        print('reprovado')


#elif MF >= 5.0:
#    print('aprovado')
#else:
#    print('reprovado')

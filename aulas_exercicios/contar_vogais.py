# import consoantes

string = 'uma string com vogais'
string = 'aaaaaeee'
total_vogais = 0

for vogal in ['a', 'e', 'i', 'o', 'u']:
    total_vogais = total_vogais + string.count(vogal)

print(total_vogais)

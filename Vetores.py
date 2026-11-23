#Vetores - Prova de Versionamento

ds = 1
c = []
#C0 = Seg, C1 = Ter, C2 = Qua, C3 = Qui, C4 = Sex
d = 0
tc = 0
r1 = 0
md = 0

print('Iniciando programa de registro de chamadas\n')


while d != 5:
    print('(Dia 1 = Segunda, Dia 2 = Terça e assim por diante) \n')
    r1 = (int(input(f'Digite o número de chamadas no dia da semana número {ds}: \n')))
    if r1 >= 0:
        ds += 1
        d += 1
        print('Número de chamadas registrado com sucesso \n')
        tc += r1
        c.append(r1)

    else:
        print('Digite um número acima de 0!')
        break

cm = tc/5
mc = max(c)
dmm = []
print(f'O total de chamados na semana foi de: {tc}')
print(f'A média de chamados na semana foi de: {cm}')

if mc == c[0]:
    print(f'O dia com maior número de chamados na semana foi: Segunda')

elif mc == c[1]:
    print(f'O dia com maior número de chamados na semana foi: Terça')

elif mc == c[2]:
    print(f'O dia com maior número de chamados na semana foi: Quarta')

elif mc == c[3]:
    print(f'O dia com maior número de chamados na semana foi: Quinta')

elif mc == c[4]:
    print(f'O dia com maior número de chamados na semana foi: Sexta')

else:
    print('Tivemos um empate!')

if cm < c[0]:
    dmm.append('Segunda')

if cm < c[1]:
    dmm.append('Terça')

if cm < c[2]:
    dmm.append('Quarta')

if cm < c[3]:
    dmm.append('Quinta')

if cm < c[4]:
    dmm.append('Sexta')

print(f'Os dias que tiveram seu número de chamados maiores que a média da semana foram: {dmm}')












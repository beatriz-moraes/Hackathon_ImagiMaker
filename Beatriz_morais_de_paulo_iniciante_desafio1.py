numeros = [0, 0, 0, 0, 0]
num_mmc = numeros

#recebendo números
for i in range(0, 5):
    numeros[i] = float(input('Digite o {}º valor: ' . format(i+1)))
    if numeros[i] > 10000:
        print('Meu programa não é obrigado a calcular isso!')
        exit()
    if numeros[i] < 0 or numeros[i] % 1:
        print('Não é possivél calcular M.M.C e M.D.C com os números fornecidos.')
        exit()
    else:
        numeros[i] = int(numeros[i])

#descobrindo o menor e maior
menor = numeros[0]
maior = numeros[0]
primos = ''
for i in range(0, 5):
    if numeros[i] < menor:
        menor = numeros[i]
    if numeros[i] > maior:
        maior = numeros[i]

    #Verificando se os números digitados são primos.
    cont = 0
    for c in range(2, numeros[i]):
        if (numeros[i] % c) == 0:
            cont = cont + 1
    if cont == 0:
        primos += str(numeros[i]) + ','
if primos == '':
    print('Nenhum número lido é primo')
else:
    print('Os números primos são = ', primos.rstrip(','))

#calculando MDC
mdc = 1
for i in range(1, menor + 1):
   if numeros[0] % i == 0 and numeros[1] % i == 0 and numeros[2] % i == 0 and numeros[3] % i == 0 and numeros[4] % i == 0:
        mdc = i
print('MDC = ', mdc)

#Calculando MMC
mmc = 1
mmc_encontrado = False
num_mmc = numeros
aux = numeros
for i in range(2, maior):
   #verifica se é numero primo
    cont = 0
    for c in range(2, i):
      if (i % c) == 0:
          cont = cont + 1

    # se for primo
    if cont == 0:
        continuar = True
        while continuar:
            if num_mmc[0] == 1 and num_mmc[1] == 1 and num_mmc[2] == 1 and num_mmc[3] == 1 and num_mmc[4] == 1:
                #se já tiver encontrado o MMC o cálculo para de ser executado.
                mmc_encontrado = True
                continuar = False
            elif num_mmc[0] % i != 0 and num_mmc[1] % i != 0 and num_mmc[2] % i != 0 and num_mmc[3] % i != 0 and num_mmc[4] % i != 0:
                #Se alguma divisão tiver resto diferente de zero avança para dividir para o proximo primo.
                continuar = False
            else:
                for c in range(0, 5):
                    if num_mmc[c] % i == 0:
                        aux[c] = num_mmc[c] / i
                    else:
                        #se a divisão não tiver resto zero mantem o número atual.
                        aux[c] = num_mmc[c]
                num_mmc = aux
                mmc = mmc * i

    if mmc_encontrado:
        #se o mmc já foi encontrado para de executar o primeiro for.
        break
print('MMC = ', mmc)

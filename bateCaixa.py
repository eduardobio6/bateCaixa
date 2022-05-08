#Calculadora para bater o caixa
pedi_caixa = float(input('Qual o valor que esta pedindo no seu caixa?: '))
fundo_caixa = float(input('Quanto tem no fundo do seu caixa?: '))

#Variaveis para verificar a quantidade de notas
notas_200 = int(input('Quantas notas de 200 tem em seu caixa?: '))
notas_100 = int(input('Quantas notas de 100 tem em seu caixa?: '))
notas_50 = int((input('Quantas notas de 50 tem em seu caixa?: ')))
notas_20 = int(input('Quantas notas de 20 tem em seu caixa?: '))
notas_10 = int(input('Quantas notas de 10 tem em seu caixa?: '))
notas_5 = int(input('Quantas notas de 5 tem em seu caixa?: '))
notas_2 = int(input('Quantas notas de 2 tem em seu caixa?: '))

#SOMA DAS NOTAS
soma_200 = 200 * notas_200
soma_100 = 100 * notas_100
soma_50 = 50 * notas_50
soma_20 = 20 * notas_20
soma_10 = 10 * notas_10
soma_5 = 5 * notas_5
soma_2 = 2 * notas_2
total_notas = soma_2 + soma_5 + soma_10 + soma_20 + soma_50 + soma_100 + soma_200

#Verifica se tem moedas no caixa
verifica_moeda = input('Há moedas no seu caixa? (DIGITE "S" PARA SIM E "N" PARA NÃO ):')

#if para liberar as somas das moedas
if verifica_moeda == 's' or verifica_moeda == 'S':
    moeda_1 = int(input('Quantas moedas de 1 real tem no seu caixa?: '))
    moeda_050 = int(input('Quantas moedas de 0,50 centavos tem no seu caixa?: '))
    moeda_025 = int(input('Quantas moedas de 0,25 centavos tem no seu caixa?: '))
    moeda_010 = int(input('Quantas moedas de 0,10 centavos tem no seu caixa?: '))
    moeda_005 = int(input('Quantas moedas de 0,05 centavos tem no seu caixa?: '))

    soma_1 = 1 * moeda_1
    soma_050 = 0.50 * moeda_050
    soma_025 = 0.25 * moeda_025
    soma_010 = 0.10 * moeda_010
    soma_005 = 0.05 * moeda_005
    total_moedas = soma_1 + soma_050 + soma_025 + soma_010 + soma_005

    total_caixa1 = (total_notas + total_moedas) - fundo_caixa

    #Verifica se há alguma sobra no caixa
    sobra_caixa_neg = total_caixa1 - pedi_caixa

    #verifica se os valores estao batendo com o que foi pedido no caixa
    if total_caixa1 < pedi_caixa:
        print(f'O valor total do seu caixa foi de {total_caixa1:.2f}R$ e há {sobra_caixa_neg:.2f}R$ faltado em seu caixa.\n')
        print('VERIFIQUE!!!!!!!!!!!!!!!!')
    elif total_caixa1 > pedi_caixa:
        print(f'O valor total do seu caixa foi de {total_caixa1:.2f}R$ e há {sobra_caixa_neg:.2f}R$ sobrando em seu caixa.\n')
        print('VERIFIQUE!!!!!!!!!!!!!!!!')
    else:
        print(f'PARABENS os valores do caixa estão batendo, O valor total do seu caixa foi de {total_caixa1:.2f}R$ .\n')
elif verifica_moeda == 'n' or verifica_moeda == "N":
    total_caixa2 = total_notas - fundo_caixa
    sobra_caixa_neg = total_caixa2 - pedi_caixa

    if total_caixa2 < pedi_caixa:
        print(f'O valor total do seu caixa foi de {total_caixa2:.2f}R$ e á {sobra_caixa_neg:.2f}R$ faltando em seu caixa.\n')
        print('VERIFIQUE!!!!!!!!!!!!!!!!')
    elif total_caixa2 > pedi_caixa:
        print(f'O valor total do seu caixa foi de {total_caixa2:.2f}R$ e á {sobra_caixa_neg:.2f}R$ sobrando em seu caixa.\n')
        print('VERIFIQUE!!!!!!!!!!!!!!!!')
    else:
        print(f'PARABENS os valores do caixa estão batendo, O valor total do seu caixa foi de {total_caixa2:.2f}R$ .\n')
else:
    print("DADOS INVALIDOS!!!!")



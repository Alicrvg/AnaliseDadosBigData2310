#RESOLUÇÃO EXERCICIO 05 DA LISTA 05
#Primeiro passo: identificar as variaveis
# nota_1= 8
# nota_2= 4
# nota_op=
# media= (nota_1+nota_2)/2
# resultado=
# if nota_op==-1

# nota1=float(input('priemira nota'))
# nota2=float(input('segunda nota'))
# optativa=float(input('Tem nota optativa?'))

# if optativa== -1:
#     media=(nota1+nota2)/2
# else:
#     if optativa>nota1:
#         media=(optativa+nota2)/2
#     else:
#         media=(optativa+nota1)/2

# if media>=6.0:
#     resultado='APROVADO'
# elif media >= 3.0:
#     resultado= 'RECUPERAÇÃO'
# else:
#     resultado= 'REPROVADO'

# print(f'Média final:{media}, resultado:{resultado}')

# #abs:obriga a ser apenas valores absolutos

#RESOLUÇÃO EXERCICIO 01 LISTA 04
lamp=0
POTENCIA= 3                #VARIAVEL CONSTANTE
largura= float(input('largura'))
comprimento=float(input('comprimento:'))

area=largura*comprimento
lampadas=area/POTENCIA

print(f'São necessárias {round(lampadas)} lâmpadas para iluminar um cômodos de {area}m2')

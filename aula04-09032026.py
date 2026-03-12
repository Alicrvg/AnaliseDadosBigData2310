#Condição pro carro andar
carro=False
combustivel=False
if not carro and not combustivel:
    print("Meu fusquinha funciona")
else:
    print("Nao sobrou nada pro fusquinha.")

semana= int(input("informe o dia"))
if semana == 1:
    print("Domingo")
elif semana == 2:
    print("Segunda-feira")
elif semana == 3:
    print("Terça-feira")
elif semana == 4:
 print("Quarta-feira")
elif semana == 5:
 print("Quinta-feira")
elif semana == 6:
 print("Sexta-feira")
elif semana == 7:
 print("Sábado")
else: # O 'else' funciona como o 'default'
 print("Dia inválido")

try:
    mes=int(input("informe um mes"))
    match mes:
        case 1:
            print("Janeiro")
        case 2:
            print("Fevereiro")
        case 3:
            print("Março")
        case 4:
            print("Abril")
        case 5:
            print("Maio")
        case 6:
            print("Junho")
        case 7:
            print("Julho")
        case 8:
            print("Agosto")
        case 9:
            print("Setembro")
        case 10:
            print("Outubro")
        case 11:
            print("Novembro")
        case 12:
            print("Dezembro")
        case _: # O underline ( _ ) funciona como o 'default' ou 'else'
            print("Mês inválido")

except ValueError:
    print("Entrada vinlaida.Por Favor, digite um numero valido")
except SyntaxError
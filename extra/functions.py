
def soma(st1,nd2):
    total = float(st1) + float(nd2)
    return total
def subtracao(st1,nd2):
    total = float(st1) - float(nd2)
    return total
def multiplicacao(st1,nd2):
    total = float(st1) * float(nd2)
    return total
def divisao(st1,nd2):
    total = float(st1) / float(nd2)
    return total
def potencia(st1,nd2):
    total = float(st1) ** float(nd2)
    return total


num1 = input('Enter the first number: ')
op = input('Operation: [+], [-], [*], [/], [^]: ')
num2 = input('Enter the second number: ')


try:
    num1 = float(num1)
    num2 = float(num2)

    if op == '+':
        print(soma(num1,num2))
    elif op == '-':
        print(subtracao(num1,num2))
    elif op == '*':
        print(multiplicacao(num1,num2))
    elif op == '/':
        print(divisao(num1,num2))
    elif op == '^':
        print(potencia(num1.num2))
    else:
        print('Invalid operator')
        exit()
except:
    print('Invalid operation')
    exit()

#Estruturas condicionais
#IF | ELSE | ELIF

#SINTAXE

#Exercício 2
#Criar um programa que some 5% de bônus ao salario de um vendedor quando ele atingir a meta em 105%
#Suponha que:
# Maria vendeu R$1700
# Meta: R$1600
# Salario: R$ 5400

# Sabendo das seguintes regras Atingimento = (Valor vendido/meta)*100
# Bônus = salario base*(5/100)
# Salario final = Salario Base + Bônus

#Variáveis

venderdor = "Maria"
valor_vendido = 1550
meta = 1600
salario_base = 5400
bonus = 5

#Calculo atingimento
atingimento = (valor_vendido/meta)*100

if (atingimento >= 105):
    bonus_realizado = salario_base*(bonus/100)
    salario_final = salario_base + bonus_realizado
    print("Nome: ",venderdor)
    print("Atingimento: ",atingimento)
    print("Salario Final: ",salario_final)
else:
    print(venderdor,"Não Atingiu a meta bônus pois"," seu atingimento foi de %",atingimento)


#Operadores Lógicos
# AND - E - Se todas as informações forem verdadeiras retorna verdadeiro se não retorna falso
# OR - OU - Se uma das condições for verdadeiras retorna verdadeiro se todas forem falsar retorna falso
# NOT - Inverte o resultado do AND e do OR 

#EXERCÍCIO 3
#Ajustando o EXERCÍCIO 1, utilizando a estrutura condicional e operadores lógicos

#RELEMBRANDO AS REGRAS DO EXERCÍCIO 1
#AS regras para identificar o melhor custo-benefício são:
# 1 - Litro do leite tem que ser inferior a R$ 7,00
# 2 - Prazo de validade tem que ser superior a 6 meses

#Criar variáveis do custo-benefício
litro = 7
validade = 6

#Validar os dados da Empresa 1
litro_empresa1 = 7.5
validade_empresa1 = 12

#Validar os dados da Empresa 2
litro_empresa2 = 6.99
validade_empresa2 = 7

#Validar os dados da Empresa 3
litro_empresa3 = 6
validade_empresa3 = 3

if (litro_empresa1<litro and validade_empresa1>validade): #Verificando Empresa 1
    print("Empresa 1 é a vencedora! Litro:", litro_empresa1,"Validade:",validade_empresa1)
elif (litro_empresa2<litro and validade_empresa2>validade): #Verificando Empresa 2
    print("Empresa 2 é a vencedora! Litro:", litro_empresa2,"Validade:",validade_empresa2)
elif (litro_empresa3<litro and validade_empresa3>validade): #Verificando Empresa 3
    print("Empresa 3 é a vencedora! Litro:", litro_empresa3,"Validade:",validade_empresa3)
else:
    print("Nenhuma empresa atendeu as condições exigidas!")

# Interação dos Usuários com o Script
# INPUT é uma Função que cria a possibilidade dos usuários interagirem com o Script
# o Input recebe valores como String por padrão
# Para que ele receba valores inteiros deve-se usar aninhamento de funções

#Exemplo Texto padrão
# input("Qual seu nome?")

#Exemplo para Inteiro
#int(input("qual a sua idade?"))

#Exemplo para Decimal
#float(input("qual a sua altura?"))

# Exercício 4 - Ajustando o Exercício 3, para solicitar os dados das empresas!

#Solicitando dados das concorrentes

nome_concorrente = input("Nome da Concorrente")

litro_concorrente = float(input("Valor do litro R$"))

validade_concorrente = int(input("Validade concorrente"))

if (litro_concorrente < litro and validade_concorrente > validade):
    print(nome_concorrente,"Atende aos requisitos de compra",litro_concorrente,"Validade",validade_concorrente,"meses")
else:
    print("Nenhuma empresa atendeu as condições exigidas!")

#Armazenando Dados inseridos pelos Usuários
#Usando variavel Lista

#A lista é delimitado pelos sinais "[" "]" e dados pertencentes a lista, estarão separados por ","
#Os dados de uma lista devem ser manipulados, utilizando MÉTODOs específicos da lista
#Uma lista pode armazenar diversos tipos de dados como textos e numeros mas a boa prática é
#criar uma lista para cada tipo de dado por categoria por exemplo

#EXERCICIO - 5 - Ajustar o exercício 4, para armazenar os valores inseridos
#Para utilizar uma lista ela deve ser criada vazia

#Criando Listas - Criação de Lista só é executada uma vez, pois se executar mais vezes ela se esvazia

lista_concorrentes_atendem = []
lista_litro_atendem = []
lista_validade_atendem = []

lista_concorrentes_nao_atendem = []
lista_litro_nao_atendem = []
lista_validade_nao_atendem = []



nome_concorrente = input("Nome da Concorrente")

litro_concorrente = float(input("Valor do litro R$"))

validade_concorrente = int(input("Validade concorrente"))

if (litro_concorrente < litro and validade_concorrente > validade):
    print(nome_concorrente,"Atende aos requisitos de compra",litro_concorrente,"Validade",validade_concorrente,"meses")

#Para guardar os dados usa-se o método .append

    lista_concorrentes_atendem.append
    lista_litro_atendem.append
    lista_validade_atendem.append
else:
    print("Nenhuma empresa atendeu as condições exigidas!")
    lista_concorrentes_nao_atendem.append
    lista_litro_nao_atendem.append
    lista_validade_nao_atendem.append

print("Registro dos dados das concorrentes que atedem aos requisitos!")
print("Concorrentes:", lista_concorrentes_atendem)
print("Valor do litro(R$):",lista_litro_atendem)
print("Validade em meses:", lista_validade_atendem)
print("---")
print("Registro dos dados das concorrentes que NÃO atedem aos requisitos!")
print("Concorrentes:", lista_concorrentes_nao_atendem)
print("Valor do litro(R$):",lista_litro_nao_atendem)
print("Validade em meses:", lista_validade_nao_atendem)

#Manipulando dados nas listas
#Remover os dados da Empresa 7, de suas listas
#Removendo nome

lista_concorrentes_atendem.pop(2)

#Removendo litro

lista_litro_atendem.pop(2)

#removendo validade

lista_validade_atendem.pop(2)

#Alterando valor do litro

lista_litro_atendem[1]=6

#EXERCÍCIO 6 - VERIFICANDO QUAL A MELHOR EMPRESA, DENTRE TODAS AS EMPRESA QUE ATENDEM
#PARA CENÁRIOS COMO ESTE, SEGUIR AS REGRAS:
#SOMAR VALOR DO LITRO + VALIDADE.
#A EMPRESA ESCOLHIDA SERÁ A QUE TIVER O MENOR VALOR

valida_empresa1 = lista_litro_atendem[0]+lista_validade_atendem[0]
valida_empresa3 = lista_litro_atendem[1]+lista_validade_atendem[1]

if (valida_empresa1 < valida_empresa3):
    print(lista_concorrentes_atendem[0],"é a vencedora! Preço:",lista_litro_atendem[0],"e validade de",lista_validade_atendem[0],"meses!")
else:
    print(lista_concorrentes_atendem[1],"é a vencedora! Preço:",lista_litro_atendem[1],"e validade de",lista_validade_atendem[1],"meses!")
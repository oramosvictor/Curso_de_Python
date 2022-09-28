'''
EXERCÍCIO 7
Seu diretor comercial te solicitou a criação de alguma coisa, onde fosse possível calcular o bônus dos/as vendedores/as, de acordo com o
atingimento de metas (somente com 2 casas decimais), cuja a regra é:

Atingimento = (Valor vendido/meta) * 100

O Bônus é calculado da seguinte forma:

- Atingimento menor que 100: Não há bônus
- Atingimento maior ou igual a 100 e menor ou igual a 105: 2% sobre o valor vendido do/a vendedor/a
- Atingimento maior que 105: 3% sobre o valor vendido do/a vendedor/a

O salário final do/a vendedor/a deve observar a seguinte regra:

Salário final = Salário base + bônus

Ao final, deve apresentar uma mensagem com as seguintes informações:

Vendedores abaixo da meta:
Nomes:
Atingimento:
Salário final:

Vendedores que bateram a meta entre 100 e 105:
Nomes:
Atingimento:
Bônus:
Salário final:

Vendedores que bateram a meta acima de 105:
Nomes:
Atingimento:
Bônus:
Salário final:

Suponha que os dados de entrada no sistema são:
Meta de vendas: 10.000
Salário base dos/as vendedores/as: 2.000

Vendedor: João
Valor vendido: 8.000

Vendedora: Maria
Valor vendido: 10.800

Vendedor: Sócrates
Valor vendido: 12.150

Vendedora: Isis
Valor vendido: 12.280

Vendedora: Ohana
Valor vendido: 10.390

Vendedor: Platão
Valor vendido: 10.032

Vendedora: Afrodite
Valor vendido: 8.950

'''

#Criando listas

#Lista abaixo da meta

lista_nome_abaixo_meta = []
lista_atingimento_abaixo_meta = []
lista_salario_final_abaixo_meta = []

#Atingiram 100 105

lista_nome_meta_100_105 = []
lista_atingimento_meta_100_105 = []
lista_bonus_meta_100_105 = []
lista_salario_final_meta_100_105 = []

#Acima de 105

lista_nome_meta_105 = []
lista_atingimento_meta_105 = []
lista_bonus_meta_105 = []
lista_salario_final_meta_105 = []

#Variáveis gerais

valor_meta = 10000
salario_base = 2000

#Capturndo Dados

nome = input("Digite nome:")
valor_vendido = int(input("Valor vendido:"))

#Calculo de Atingimento da meta
atingimento = round(((valor_vendido/valor_meta)*100),2)

#Calculo bonus
if (atingimento < 100):
    #Sem bonus
    lista_nome_abaixo_meta.append(nome)
    lista_atingimento_abaixo_meta.append(atingimento)
    lista_salario_final_abaixo_meta.append(salario_base)
elif (atingimento >= 100 and atingimento <= 105):
    #atingimento entre 100 e 105
    valor_bonus = (valor_vendido*0.02)
    salario_final = salario_base + valor_bonus

    lista_nome_meta_100_105.append(nome)
    lista_atingimento_meta_100_105.append(atingimento)
    lista_bonus_meta_100_105.append(valor_bonus)
    lista_salario_final_meta_100_105.append(salario_final)
elif (atingimento > 105):
    #Atingimento maior 105
    valor_bonus = (valor_vendido*0.02)
    salario_final = salario_base + valor_bonus

    lista_nome_meta_105.append(nome)
    lista_atingimento_meta_105.append(atingimento)
    lista_bonus_meta_105.append(valor_bonus)
    lista_salario_final_meta_105.append(salario_final)
else:
    print("ERRO - OS DADOS NÃO SATISFAZEM AS CONDIÇÕES")

#Exibindo

print("")
print("Vendedores abaixo da meta")
print("Nomes",lista_nome_abaixo_meta)
print("Atingimento da meta %",lista_atingimento_abaixo_meta)
print("Salario final",lista_salario_final_abaixo_meta)

print("")
print("Vendedores 100 a 105")
print("Nomes",lista_nome_meta_100_105)
print("Atingimento da meta %",lista_atingimento_meta_100_105)
print("Bonus",valor_bonus)
print("Salario final",lista_salario_final_meta_100_105)

print("")
print("Vendedores acima 105")
print("Nomes",lista_nome_meta_105)
print("Atingimento da meta %",lista_atingimento_meta_105)
print("Bonus",valor_bonus)
print("Salario final",lista_salario_final_meta_105)

#Minutagem 33:29
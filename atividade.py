# O que é uma tabela verdade: É uma ferramenta matemática utilizada para raciocínio lógico, como por exemplo: João foi a praia, ou Maria foi ao cinema. 

# O que é uma variável: É um tipo de gaveta que guarda as informações e que pode ser substituída por outros dados e é inconstante. Ela não pode começar com letra maiúscula, não pode ter espaço e não pode ter acentuação. 

# O que é tupla: É um tipo de lista imodificável, e nela útilizamos parênteses e virgula para separar. 

# O que é lista: É um conjunto de dados que contém: inteiros, floats e strings. Diferente da tupla, ele é modificavel.

# O que é dicionário: É um conjunto de dados com chaves e valores.

# Atividade 4.1:

nota =  int(input('Qual a nota do aluno do PdA? '))
participacao = (input('Você é participativo? '))

if nota >= 7: 
    print('Parabéns! Você está aprovado!!')

if (nota == 6) and (participacao == "Sim"):  
    print('Você está de recuperação!')
    
else:
    print('Você está reprovado!')

# # Atividade 4.2

meses_trabalhados = int(input("Quantas meses Tiago trabalhou? "))
disp = input('Tem disponibilidade entre dezembro e janeiro? ')

if (meses_trabalhados >= 12) and (disp == "Sim"):
    print('Tiago pode sair de férias')
else:
    print('Tiago não pode sair de férias')
    
# Atividade 4.3

pda = int(input("Quantos graus fará no dia da confraternização? "))

if  (pda > 25):
    print ("Oba! A PDA pode marcar a data")

elif (pda <= 25) and (pda > 15):
    print ("Vamos! O que vale é a companhia")

elif (pda <= 15):
    print ("Estará muito frio, não podemos alugar nessa data")


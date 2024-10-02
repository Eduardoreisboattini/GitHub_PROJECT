# Definindo tuplas para representar informações de alunos.
# Cada tupla pode ser considerada como um conjunto de dados de um aluno.

aluno1 = (18632827, "John Lennon", 19, "Bacharelado em Ciência da Computação")   # dados do primeiro aluno
aluno2 = (19817271, "Ringo Star", 21, "Licenciatura em Matemática")   # dados do segundo aluno
aluno3 = (19384729, "Paul McCartney", 20, "Engenharia Elétrica")   # dados do terceiro aluno
aluno4 = (19563218, "George Harrison", 22, "Física")   # dados do quarto aluno
aluno5 = (19928374, "Jimi Hendrix", 23, "Artes Visuais")   # dados do quinto aluno
aluno6 = (19751432, "Janis Joplin", 21, "Psicologia")   # dados do sexto aluno
aluno7 = (19472635, "Bob Dylan", 24, "Letras")   # dados do sétimo aluno
aluno8 = (19283746, "Miles Davis", 25, "Música")   # dados do oitavo aluno

# Imprimindo as tuplas e seus tipos.
print("Dados do primeiro aluno: ", aluno1, "Tipo: ", type(aluno1))
print("Dados do segundo aluno: ", aluno2, "Tipo: ", type(aluno2))
print("Dados do terceiro aluno: ", aluno3, "Tipo: ", type(aluno3))
print("Dados do quarto aluno: ", aluno4, "Tipo: ", type(aluno4))
print("Dados do quinto aluno: ", aluno5, "Tipo: ", type(aluno5))
print("Dados do sexto aluno: ", aluno6, "Tipo: ", type(aluno6))
print("Dados do sétimo aluno: ", aluno7, "Tipo: ", type(aluno7))
print("Dados do oitavo aluno: ", aluno8, "Tipo: ", type(aluno8))

# Obtendo o tamanho da primeira tupla.
print("Número de elementos na tupla do primeiro aluno: ", len(aluno1))

# Acessando um valor específico em uma tupla (por exemplo, o nome do aluno).
print("Nome do primeiro aluno: ", aluno1[1])

# Obtendo uma fatia da segunda tupla (por exemplo, idade e curso do segundo aluno).
print("Idade e curso do segundo aluno: ", aluno2[2:4])

# Iterando sobre todos os elementos da segunda tupla.
# Aqui, podemos considerar a iteração como uma forma de análise de dados.
print("Todos os dados do segundo aluno: ")
for dado in aluno2:
    print(dado)

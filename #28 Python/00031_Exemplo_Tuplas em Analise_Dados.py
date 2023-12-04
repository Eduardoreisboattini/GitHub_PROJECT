# Definindo tuplas para representar informações de alunos.
aluno1 = (18632827, "John Lennon", 19, "Bacharelado em Ciência da Computação")   # primeira tupla
aluno2 = 19817271, "Ringo Star", 21, "Licenciatura em Matemática"   # segunda tupla (sem parênteses!)

# Imprimindo as tuplas e seus tipos.
print("Primeira tupla: ", aluno1, "Tipo: ", type(aluno1))
print("Segunda tupla: ", aluno2, "Tipo: ", type(aluno2))

# Obtendo o tamanho da primeira tupla.
print("Tamanho da primeira tupla: ", len(aluno1))

# Acessando um valor específico em uma tupla.
print("Valor de uma posição da primeira tupla: ", aluno1[1])

# Obtendo uma fatia da segunda tupla.
print("Uma fatia da segunda tupla: ", aluno2[1:3])

# Iterando sobre todos os elementos da segunda tupla.
print("Todos os elementos da segunda tupla: ")
for elemento in aluno2:
    print(elemento)

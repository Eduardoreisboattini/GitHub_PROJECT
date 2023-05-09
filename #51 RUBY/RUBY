def calculate_distribution_queue(initial_queue, n, x)
  m = fila_.length # número de vendedores na fila inicial
  c = (n / m).floor # número de clientes que cada vendedor deve atender
  first_seller = initial_queue[0] # o primeiro vendedor da fila é o primeiro elemento do vetor
  clients_to_reach_x = (x + 1) * c # número de clientes necessários para que o vendedor de ID X chegue à frente da fila
  updated_queue = initial_queue.rotate(c) # atualiza a fila de distribuição rotacionando os elementos em C posições
  [first_seller, updated_queue, clients_to_reach_x] # retorna o primeiro vendedor da fila, a fila atualizada e o número de clientes necessários para chegar ao vendedor de ID X
end

# Exemplo de uso
initial_queue = [1, 2, 3, 4, 5]
n = 20
x = 3
first_seller, updated_queue, clients_to_reach_x = calculate_distribution_queue(initial_queue, n, x)
puts "O primeiro vendedor da fila é o vendedor de ID #{first_seller}"
puts "A fila de distribuição atualizada é #{updated_queue}"
puts "São necessários #{clients_to_reach_x} clientes para que o vendedor de ID #{x} chegue à frente da fila"

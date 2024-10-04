 ### 2. Visualizações com ggplot2

# Gráfico de dispersão
ggplot(trainData, aes(x = Sepal.Length, y = Sepal.Width, color = Species)) +
  geom_point(size = 3) +
  theme_minimal() +
  labs(title = "Gráfico de Dispersão - Comprimento vs Largura da Sépala")

# Histogramas
ggplot(trainData, aes(x = Petal.Length, fill = Species)) +
  geom_histogram(binwidth = 0.5, alpha = 0.7, position = "dodge") +
  theme_minimal() +
  labs(title = "Histograma do Comprimento da Pétala", x = "Comprimento da Pétala")

# Gráfico de barras
ggplot(trainData, aes(x = Species, fill = Species)) +
  geom_bar() +
  theme_minimal() +
  labs(title = "Distribuição das Espécies", x = "Espécie", y = "Contagem")

# Boxplots
ggplot(trainData, aes(x = Species, y = Petal.Length, fill = Species)) +
  geom_boxplot() +
  theme_minimal() +
  labs(title = "Boxplot do Comprimento da Pétala por Espécie", x = "Espécie", y = "Comprimento da Pétala")


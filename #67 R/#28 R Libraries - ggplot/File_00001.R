 ### 2. Visualizações com ggplot2

# Gráfico de dispersão
ggplot(trainData, aes(x = Sepal.Length, y = Sepal.Width, color = Species)) +
  geom_point(size = 3) +
  theme_minimal() +
  labs(title = "Gráfico de Dispersão - Comprimento vs Largura da Sépala")

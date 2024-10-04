
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











/*************  ✨ Codeium Command ⭐  *************/
# Matriz de Confusão com ggplot2
confusion_rf <- confusionMatrix(testData$predicted_rf, testData$Species)
conf_matrix_df <- as.data.frame(confusion_rf$table)

ggplot(conf_matrix_df, aes(Prediction, Reference, fill = Freq)) +
  geom_tile() +
  geom_text(aes(label = Freq), color = "white") +
  scale_fill_gradient(low = "blue", high = "red") +
  theme_minimal() +
  labs(title = "Matriz de Confusão - Random Forest")
/******  9f44fab6-9509-4bf4-b025-31ec31f8e060  *******/
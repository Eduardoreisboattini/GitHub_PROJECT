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
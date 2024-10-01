library(ggplot2)
library(dplyr)
library(caret)
library(e1071)         # SVM
library(randomForest)  # Random Forest
library(xgboost)       # Gradient Boosting (XGBoost)
library(nnet)          # Neural Networks
library(class)         # k-NN
library(naivebayes)    # Naive Bayes

# Carregar o dataset de exemplo (usaremos o dataset iris para simplificação)
data(iris)

# Dividir o dataset em treino e teste
set.seed(123)
trainIndex <- createDataPartition(iris$Species, p = .7, 
                                  list = FALSE, 
                                  times = 1)
trainData <- iris[ trainIndex,]
testData  <- iris[-trainIndex,]

### 1. Implementação de Algoritmos de Machine Learning

# Modelo de Regressão Logística
log_model <- train(Species ~ ., data = trainData, method = "multinom")

# Modelo SVM
svm_model <- train(Species ~ ., data = trainData, method = "svmRadial")

# Modelo k-Nearest Neighbors
knn_model <- train(Species ~ ., data = trainData, method = "knn")

# Modelo Naive Bayes
nb_model <- train(Species ~ ., data = trainData, method = "naive_bayes")

# Modelo de Árvores de Decisão
dt_model <- train(Species ~ ., data = trainData, method = "rpart")

# Modelo Random Forest
rf_model <- randomForest(Species ~ ., data = trainData)

# Modelo Gradient Boosting (XGBoost)
train_matrix <- xgb.DMatrix(data = as.matrix(trainData[, -5]), label = as.numeric(trainData$Species) - 1)
test_matrix <- xgb.DMatrix(data = as.matrix(testData[, -5]))

params <- list(objective = "multi:softprob", num_class = 3)
xgb_model <- xgboost(data = train_matrix, params = params, nrounds = 100, verbose = FALSE)

# Modelo de Redes Neurais
nn_model <- nnet(Species ~ ., data = trainData, size = 5, decay = 0.1, maxit = 200)

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

### 3. Aplicação de Filtros Interessantes com dplyr

# Filtros com dplyr para manipular os dados
# Filtrar apenas os registros com Sepal.Length > 5.0
filtered_data <- trainData %>%
  filter(Sepal.Length > 5.0)

# Visualização do conjunto de dados filtrados
ggplot(filtered_data, aes(x = Sepal.Length, y = Sepal.Width, color = Species)) +
  geom_point(size = 3) +
  theme_minimal() +
  labs(title = "Dados Filtrados - Comprimento da Sépala > 5.0")

# Finalizando - Modelo Random Forest com predições e visualização de resultados
testData$predicted_rf <- predict(rf_model, testData)

# Gráfico de Confusão com ggplot2
confusion_rf <- confusionMatrix(testData$predicted_rf, testData$Species)
conf_matrix_df <- as.data.frame(confusion_rf$table)

ggplot(conf_matrix_df, aes(Prediction, Reference, fill = Freq)) +
  geom_tile() +
  geom_text(aes(label = Freq), color = "white") +
  scale_fill_gradient(low = "blue", high = "red") +
  theme_minimal() +
  labs(title = "Matriz de Confusão - Random Forest")

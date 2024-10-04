 # Load necessary libraries

library(dplyr)
library(ggplot2)

# View the dataset (optional)
View(X021024)

# Create a ggplot object
p <- ggplot(X021024, aes(x = Pais, y = aliado)) +
  geom_bar(stat = "identity") +
  labs(title = "Quantity of Aliado by Country", x = "Country", y = "Quantity of Aliado") +
  annotate("text", x = 1, y = 1, label = "All aesthetics have length 1, but the data has 69143 rows.\nPlease consider using `annotate()` or provide this layer with data containing a single row.", color = "red", size = 4, hjust = 0, vjust = 0)

# Print the plot
print(p)


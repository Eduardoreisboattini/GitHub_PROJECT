# Create a scatter plot with a linear regression line and a count of points for each gender
ggplot(X300924, aes(x = Nome_GPS, y = ..count.., colour = Genero)) + 
  # Add points to the plot
  geom_point() + 
  # Add a linear regression line to the plot
  geom_smooth(method = "lm", se = FALSE) + 
  # Add a count of points for each gender
  stat_sum(aes(label = ..count..), geom = "text", vjust = -1)

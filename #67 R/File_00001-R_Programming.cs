# load the data
data <- read.csv("data.csv")

# get the summary statistics
summary(data)

# get the mean
mean(data$column)

# get the median
median(data$column)

# get the standard deviation
sd(data$column)

# get the distribution of the data
hist(data$column, main="Distribution of Data", col="blue", border="white")

# get the outliers of the data
boxplot(data$column, main="Outliers of Data", horizontal=TRUE)
<<<<<<<  1d6c08c2-ad3c-4585-8289-3d87fc5c5c40  >>>>>>>

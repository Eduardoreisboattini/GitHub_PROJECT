numbers = [1, 2, 3, 4, 5]

sum = numbers.reduce(0) { |acc, num| acc + num }
puts sum      # Output: 15

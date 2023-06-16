print("-----------------------------------")

temperature = 37
print('Temperature is now: ', temperature, 'Celsius Degrees')
if temperature > 30:
    print("It is a HOT day")
    print("Drink plenty of water")
    
print("-----------------------------------")

temperature = 25
print('Temperature is now: ', temperature, 'Celsius Degrees')
if temperature > 30:
    print("It is a HOT day")
    print("Drink plenty of water")    

print("-----------------------------------")

temperature = 12
print('Temperature is now: ', temperature, 'Celsius Degrees')
if temperature > 30:
    print("It is a HOT day")
    print("Drink plenty of water") 
elif temperature > 20: # (20,30]
    print("It is a nice day")
    print('Done')
elif temperature > 10: # (10,20]
    print("It is a bit cold")
    print('Done')
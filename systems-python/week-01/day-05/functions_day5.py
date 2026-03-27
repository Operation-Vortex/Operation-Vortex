
#Pure Function
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


#Impure Function
def celsius_to_fahrenheit_and_print(celsius):
    global temperature
    temperature = (celsius * 9/5) + 32
    print(f"{celsius} degrees Celsius is equal to {temperature} degrees Fahrenheit.")



temperature = 0

print(celsius_to_fahrenheit(100))
celsius_to_fahrenheit_and_print(100)
print(f"Global temperature variable is now: {temperature}")
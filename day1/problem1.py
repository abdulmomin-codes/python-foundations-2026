#Write a script that prompts for temperature in Celsius via input() #
#and prints Fahrenheit ($F = \frac{9}{5}C + 32$), ensuring proper float casting.#


temp_celsius = float(input("enter the temperature in celsius: "))
temp_fahrenheit = 32 + (9 / 5) * temp_celsius
print(f"{temp_celsius} C is equal to {temp_fahrenheit:.2f} F")


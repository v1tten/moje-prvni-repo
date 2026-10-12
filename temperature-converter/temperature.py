
celsius = float(input("Temperature"))
fahrenheit = celsius * 9 / 5 + 32
kelvin = celsius + 273.15

fahrenheit = round(fahrenheit, 2)
kelvin = round(kelvin, 2)

print(f"{celsius} °C = {fahrenheit} °F = {kelvin} K")
print( "=== Temperature Converter===")
temp = float(input("Enter temperature: "))
unit = input("celsius or fahrenheit? (C/f): ").upper()
if unit == "C":
    converted = (temp * 9/5) + 32
    print(f"{temp}°C = {converted:.1f}°F")
elif unit == "F":
    converted = (temp - 32) * 5/9
    print(f"{temp}°F = {converted:.1f}°C")

else:
    print("invalid! Type C or F")


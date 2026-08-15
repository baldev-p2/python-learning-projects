# Celsius: water freezes at 0°C and boils at 100°C. This is the scale used in most of the world, including India.
# Fahrenheit: water freezes at 32°F and boils at 212°F. This scale is mainly used in the US.
# Formula to convert celsius into fahrenheit: F = (C × 9/5) + 32

print("    Celsius to Fahrenheit Converter    ")

user = int(input("Enter Celsius: "))
convert = (user * 9/5) + 32

print(f"If Celsius is {user}°C, Fahrenheit is {round(convert)}°F")

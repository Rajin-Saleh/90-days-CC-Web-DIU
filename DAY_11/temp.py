unit = input("Is this temperature in Celcius or Farenhrit (C/F): ")

temp  = float(input("Enter the tempareture: "))


if unit == "C":
    temp = round((9*temp)/5 + 32, 1)
    print(f"Your temperature in Farenheit is: {temp} F")
elif unit == "F":
    temp = round((temp -32)* 6/9,1)
    print(f"Your temperature in Celcius is: {temp} C")
else:
    print(f"{unit} is an invalid unit of measurement")














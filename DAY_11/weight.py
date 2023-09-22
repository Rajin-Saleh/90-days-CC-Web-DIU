 # weight converstion


 weight = float(input("Enter your weight: "))

 unit = input("Kilograms or Pounds? (k or L): ")

 if unit == "K":
     weight = weight * 2.05
     unit = "Lbs."
     print(f"Your weight is: {round(weight, 3)} lbs")    
 elif unit == "L":
     weight = weight / 2.05
     unit = "Kgs."
     print(f"Your weight is: {round(weight, 3)} kg")    
 else:
     print(f"{unit} was not valid.")




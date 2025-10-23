conversions_feet = {
    "miles": 1 / 5280,
    "yards": 1 / 3,
    "inches": 12,
    "centimeters": 30.48,
    "meters": 0.3048,
    "kilometers": 0.0003048
}

conversions_miles = {
    "feet": 5280,
    "yards": 1760,
    "inches": 63360,
    "centimeters": 160934.4,
    "meters": 1609.344,
    "kilometers": 1.609344
}

conversions_meters = {
    "feet": 3.28084,
    "yards": 1.09361,
    "inches": 39.3701,
    "centimeters": 100,
    "miles": 0.000621371,
    "kilometers": 0.001
}

conversions_yards = {
    "feet": 3,
    "miles": 1 / 1760,
    "inches": 36,
    "centimeters": 91.44,
    "meters": 0.9144,
    "kilometers": 0.0009144
}

conversions_inches = {
    "feet": 1 / 12,
    "yards": 1 / 36,
    "miles": 1 / 63360,
    "centimeters": 2.54,
    "meters": 0.0254,
    "kilometers": 0.0000254
}

conversions_centimeters = {
    "feet": 1 / 30.48,
    "yards": 1 / 91.44,
    "inches": 1 / 2.54,
    "miles": 1 / 160934.4,
    "meters": 0.01,
    "kilometers": 0.00001
}

conversions_kilometers = {
    "feet": 3280.84,
    "yards": 1093.61,
    "inches": 39370.1,
    "centimeters": 100000,
    "meters": 1000,
    "miles": 0.621371
}


continue_script = input("Start the script?: ")

while (continue_script.lower() == "true" or "start" or "continue" or "yes"):
  

  convert_from = input("Convert from: ")
  convert_to = input("Convert to: ")
  

  #convert from feet
  if (convert_from.lower() == "feet") :
    if (convert_to in conversions_feet):
      total = float(input("How many feet: "))
      print(f"The conversion of {convert_from.lower()} to \
      {convert_to.lower()} is \
      {total * conversions_feet[convert_to]}")

  #convert from miles

  if (convert_from.lower() == "miles"):
    if (convert_to in conversions_miles):
      total = float(input("How many miles: "))
      print(f"The conversion of {convert_from.lower()} to\
      {convert_to.lower()} is\
      {total * conversions_miles[convert_to]}")


  #convert from meters

  if (convert_from.lower() == "meters"):
    if (convert_to in conversions_meters):
      total = float(input("How many meters: "))
      print(f"The conversion of {convert_from.lower()} to\
      {convert_to.lower()} is\
      {total * conversions_meters[convert_to]}")

  #convert from yards

  if (convert_from.lower() == "yards"):
    if (convert_to in conversions_yards):
      total = float(input("How many yards: "))
      print(f"The conversion of {convert_from.lower()} to\
      {convert_to.lower()} is\
      {total * conversions_yards[convert_to]}")


  #convert from inches

  if (convert_from.lower() == "inches"):
    if (convert_to in conversions_inches):
      total = float(input("How many inches: "))
      print(f"The conversion of {convert_from.lower()} to\
      {convert_to.lower()} is\
      {total * conversions_inches[convert_to]}")


  #convert from centimeters

  if (convert_from.lower() == "centimeters"):
    if (convert_to in conversions_centimeters):
      total = float(input("How many centimeters: "))
      print(f"The conversion of {convert_from.lower()} to\
      {convert_to.lower()} is\
      {total * conversions_centimeters[convert_to]}")


  #convert from kilometers

  if (convert_from.lower() == "kilometers"):
    if (convert_to in conversions_kilometers):
      total = float(input("How many meters: "))
      print(f"The conversion of {convert_from.lower()} to\
      {convert_to.lower()} is\
      {total * conversions_kilometers[convert_to]}")

  continue_script = input("continue the script?: ")
  if (continue_script.lower() == "no"):
    break 

print("script broken")


month_in=(input("Enter the month number (1 to 12): "))
month=None
if month_in.isdecimal() or month_in.isdigit():
  month=int(month_in)
  if month is not None:
    if month==11 or month==12 or month==1 or month==2:
      temperature=(input("Enter the temperature between -50 and 50 °F: "))
      wind_speed=(input("Enter the wind speed between 3 and 120 mph: "))

      temp=None
      wind=None
      if temperature.isdecimal() or temperature.isdigit():
        temp=float(temperature)
      if wind_speed.isdecimal() or wind_speed.isdigit():
        wind=float(wind_speed)

      if temp is None:
        print("Invalid input. Enter Valid Temperature")
      elif wind is None:
        print("Invalid input. Enter Valid Wind Speed")
      elif -50>temp and temp>50 and 3>wind and wind>120:
        print(f"Invalid input. Temperature {temp} must be between -50 and 50 °F, and wind speed {wind} between 3 and 120 mph.")
      else:
        wind_chill=35.74+0.6215*temp-35.75*(wind**0.16)+0.4275*temp*(wind**0.16)
        print(f"Wind Chill: {round(wind_chill,2)} °F for Month {month} with temperature {temp} and wind speed {wind}")

    else:
      print("Wind chill computation is not applicable for month Test.")
  else:
    print("Invalid input.Enter valid the month number")





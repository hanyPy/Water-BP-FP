                          #is the water boiling ? Let's find out
temprature = int(input("Write the temprature of the water: "))
cof = str(input("Write either c or f: "))
if cof == str("c" or "C" or "f" "F"):
    print("The temprature at " + str(temprature)+str(cof)+" is: ")
else:
   print("Invalid sign.\n " + str(input("Write EITHER C or F : ")))




                                 #celsuis
if int(temprature) >= 100:
    print("The water at " + str(temprature)+ "C" " is at boiling point.")
else:
    print("The water at " + str(temprature)+ "C" " is not at boiling point.")

                          # fahrenheit
if int(temprature) >= 212:
    print("The water at " + str(temprature)+ "F" " is at boiling point.")
else:
    print("The water at " + str(temprature)+ "F" " is not at boiling point.")
                 
                                              #project - is the water boiling? or freezing?

#"im tired boss.jpg"

temprature = int(input("Enter the temprature of the water here: "))



             #celsuis
if temprature >= int(100):
    print("at "+ str(temprature) + "C, " "the water is at more than boiling point.")
    if temprature <int(0):
        print("At " + str(temprature) + "C, " "the water is below freezing point." )
else:
    print("at "+ str(temprature) + "C, " "the water is not at boiling point.")


    #fahrenheit
if temprature >= int(212):
    print("at "+ str(temprature) + "F, " "the water is at more than boiling point.")
else:
   print("at "+ str(temprature) + "F, " "the water is not at boiling point.")

            #kelvin
if temprature >= float(373.2):
 print("At " +str(temprature) + "K, " "the water is at more than boiling point.")
else:
    print("At " +str(temprature) + "K, " "the water is not at boiling point.")



 #FINAL NOTES: needs more polish especially if the bp is at either 100 , 212 and 373.2
 #add freezing points and the "exactly at bp " if statements
 #fix errors when time = available.
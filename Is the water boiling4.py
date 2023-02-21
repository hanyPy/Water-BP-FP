
#                                        is the water boiling?  freezing?
#  Finished Project.
# 19th February 2023 - 21st February 2023.
# "I'm tired boss.jpg"

temprature = float(input("Enter the temprature of the water here: "))


#                C E L S I U S
if temprature > int(100):
 print("At " +str(temprature)+"C , the water is at more than boiling point." )
elif temprature == float(100):
  print("At " +str(temprature) + "C, " "the water is exactly at boiling point.")

elif temprature < int(0):
    print("At " +str(temprature)+ "C , the water is below freezing point.")
elif temprature == 0:
    print("At " + str(temprature)+ "C , the water is exactly at freezing point.")
else:
    print("At " +str(temprature)+"C , the water is not at boiling point.")

#           F A H R E N H E I T
if temprature > int(212):
    print("At "+ str(temprature) + "F, " "the water is at more than boiling point.")
elif temprature == float(212):
  print("At " +str(temprature) + "F, " "the water is exactly at boiling point.")
elif temprature < int(32):
    print("At " +str(temprature)+ "F , the water is below freezing point.")
elif temprature == 32:
    print("At " + str(temprature)+ "F , the water is exactly at freezing point.")
else:
   print("At "+ str(temprature) + "F, " "the water is not at boiling point.")

#          K E L V I N
if temprature > float(373.2):
 print("At " +str(temprature) + "K, " "the water is at more than boiling point.")
elif temprature == float(373.2):
  print("At " +str(temprature) + "K, " "the water is exactly at boiling point.")
elif temprature < float(273.15):
    print("At " +str(temprature)+ "K , the water is below freezing point.")
elif temprature == float(273.15):
    print("At " + str(temprature)+ "K , the water is exactly at freezing point.")
else:
    print("At " +str(temprature) + "K, " "the water is not at boiling point.")


#                            Errors to be fixed or things to be added
 #needs more polish especially if the bp is at either 100 , 212 and 373.2 .
 #add exactly at freezing point statements correctly.
 # Add exactly at boiling point if statements

 #                                  Errors fixed or things added
 #I only had to remove the "=" sign from the if statements.
 #Added the FP statements correctly.
 #Added exactly at BP if statements.
              
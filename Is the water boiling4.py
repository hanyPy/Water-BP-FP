
#                                          project - is the water boiling?  freezing?
#"im tired boss.jpg"    #final try 
#ongoing project
#started 19th february 2023 - 

temprature = float(input("Enter the temprature of the water here: "))


#                C E L S I U S
if temprature >= int(100):
 print("At " +str(temprature)+"C , the water is at more than boiling point." )
elif temprature <= int(0):
    print("At " +str(temprature)+ "C , the water is below freezing point.")
elif temprature == 0:
    print("At " + str(temprature)+ "C , the water is exactly at freezing point.")
else:
    print("At " +str(temprature)+"C , the water is not at boiling temprature")

#           F A H R E N H E I T
if temprature >= int(212):
    print("At "+ str(temprature) + "F, " "the water is at more than boiling point.")
elif temprature <= int(32):
    print("At " +str(temprature)+ "F , the water is below freezing point.")
else:
   print("At "+ str(temprature) + "F, " "the water is not at boiling point.")

#          K E L V I N
if temprature >= float(373.2):
 print("At " +str(temprature) + "K, " "the water is at more than boiling point.")
elif temprature <= float(273.15):
    print("At " +str(temprature)+ "K , the water is below freezing point.")
else:
    print("At " +str(temprature) + "K, " "the water is not at boiling point.")


# available = never
 #FINAL NOTES: needs more polish especially if the bp is at either 100 , 212 and 373.2
 #fix errors when time == available.
 #add exactly at freezing point statemnets correctly.
              
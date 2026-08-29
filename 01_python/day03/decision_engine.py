IA = int(input ("What is you Investment Amount="))
Return = int(input ("Annual Expected Return = "))
Horizon = int(input ("What is your Time Horizon in years = "))

if Return <= 8 and Horizon >= 5:
    print ("Conservative")
elif Return <= 12 and Horizon >= 3:
    print ("Moderate")
else:
    print ("Aggressive")


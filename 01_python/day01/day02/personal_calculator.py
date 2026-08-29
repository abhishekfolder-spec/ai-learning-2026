# name = input("What is your name")
# age = int(input ("How old are you?"))
## print ("Your age is", age)
## future_age = age + 5
#print("in Five years, your age will be", future_age)

investment = float(input("investment amount-"))
return_rate = float(input("Annual Return-"))
years = int(input("Number of years-"))
fv = investment*(1+return_rate/100)**years
profit = investment * return_rate /100
print ("Future Value = ", fv)
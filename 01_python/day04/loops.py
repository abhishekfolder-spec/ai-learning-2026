returns_list= [12,-15, 20, -25, 30]
for return_rate in returns_list:
    print(f"The return rate is: {return_rate}")
    if return_rate > 0:
        print("Return is positive")
    else:
        print("Return is negative")
print("The total return is =",return_rate*100)
average_return = sum(returns_list) / len(returns_list)
print("The average return is =",average_return)
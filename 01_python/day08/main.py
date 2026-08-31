import os
import json

with open("Education/ai-learning-2026/01_python/day08/portfolio.json","r") as file:
    portfolio = json.load(file)
print (portfolio)

total_investment = 0
total_profit = 0
for stock in portfolio:
    print(stock["name"]," ",stock["sector"])
    total_investment += stock["investment"]
    total_profit += stock["investment"] * (stock["return_pct"] / 100)

with open("Education/ai-learning-2026/01_python/day08/output.txt","w") as file:
    file.write("My total investment is " + str(total_investment) + " and my total profit is " + str(total_profit))

import pandas as pd
portfolio= [
    {"name":"HDFC Bank",
     "sector":"Banking",
     "investment":500000,
     "return_pct":12
     },
     {"name":"TCS",
        "sector":"IT",
        "investment":300000,
        "return_pct":8
     },
     {"name":"Sun Pharma",
      "sector":"Pharmaceuticals",
      "investment":200000,
      "return_pct":15
    }     
]

for stock in portfolio:
    print(stock["name"])
    print("Sector:",stock["sector"])
    print("Investment:",stock["investment"])
    print("Return Percentage:",stock["return_pct"])
    print()

total_investment = 0
for stock in portfolio:
    total_investment += stock["investment"]

print("Total Investment in Portfolio:", total_investment)
df= pd.DataFrame(portfolio)
print(df)
highest_value = 0

for stock in portfolio:
    profit = stock["investment"] * (stock["return_pct"] / 100)
    print(f"Profit from {stock['name']} is: {profit}")
    if profit > highest_value:
        highest_value = profit
        best_stock = stock["name"]
print(f"The best performing stock is: {best_stock} with a profit of: {highest_value}")

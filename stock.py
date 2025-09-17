# Short Stock Portfolio Tracker

stock_prices = {"APPLE": 180, "TESLA": 250, "GOOGLE": 140, "MICROSOFT": 300}

portfolio = {}
total = 0

while True:
    stock = input("Enter stock (or 'done'): ").upper()
    if stock == "DONE":
        break
    if stock in stock_prices:
        qty = int(input("Enter quantity: "))
        portfolio[stock] = portfolio.get(stock, 0) + qty
    else:
        print("Stock not found!")

print("\nPortfolio Summary:")
for s, q in portfolio.items():
    value = stock_prices[s] * q
    total += value
    print(f"{s}: {q} × ${stock_prices[s]} = ${value}")

print(f"\nTotal Investment = ${total}")


stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2700,
    "AMZN": 3300,
    "MSFT": 310
}

portfolio = {}


print("Enter your stock portfolio (type 'done' to finish):")
while True:
    stock = input("Stock symbol (e.g., AAPL): ").upper()
    if stock == 'DONE':
        break
    if stock in stock_prices:
        quantity = int(input(f"How many shares of {stock}? "))
        portfolio[stock] = portfolio.get(stock, 0) + quantity
    else:
        print("Stock not found in the price list. Try again.")


total_value = 0
print("\nYour Portfolio:")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    total_value += value
    print(f"{stock}: {qty} shares x ${price} = ${value}")

print(f"\nTotal Investment Value: ${total_value}")


save = input("Do you want to save this report to a file? (yes/no): ").lower()
if save == "yes":
    with open("portfolio_report.txt", "w") as file:
        file.write("Your Portfolio:\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            value = price * qty
            file.write(f"{stock}: {qty} shares x ${price} = ${value}\n")
        file.write(f"\nTotal Investment Value: ${total_value}")
    print("Report saved to portfolio_report.txt")

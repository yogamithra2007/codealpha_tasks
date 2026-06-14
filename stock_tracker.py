stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140
}
stock_name = input("Enter stock name:").upper()
quantity = int(input("Enter quantity:"))
if stock_name in stocks:
    total = stocks[stock_name]*quantity
    print("Total Investent Value:$",total)
else:
    print("Stock not found!")

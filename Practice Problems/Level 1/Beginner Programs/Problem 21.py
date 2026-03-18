Cost_price = float(input("Enter the cost price: "))
Selling_Price = float(input("Enter the selling price: "))

calculate = Cost_price - Selling_Price
if calculate > 0:
    print("Loss of", calculate, "rupees")
else:
    print("Profit of", abs(calculate), "rupees")

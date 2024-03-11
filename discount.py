def calculate_discount(price, discount_percent):
    if (discount_percent>20):
        return (price*(100-discount_percent)/100)
    else: return price

price = int(input("Enter original price:"))
discount = int(input("Enter discount percentage:"))
print(calculate_discount(price,discount))
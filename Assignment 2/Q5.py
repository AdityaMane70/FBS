# 5. WAP to calculate selling price of book based on cost price and discount.
cost_price=int(input("enter price of book:"))
discount=int(input("enter discount to be given:"))

discount_price=cost_price*(discount/100)
selling_price=cost_price-discount_price

print("selling price of book is:",selling_price)
# 5. Write a program to calculate profit or loss.
cost=int(input("Enter cost price:"))
sell=int(input("Enter selling price:"))
profit=sell-cost
loss=cost-sell
if (sell>cost):
    print(f"you made profit of {profit} rupiess")
elif (sell<cost):
    print(f"you made a loss of {loss} rupies")
else:
    print("you made no loss no profit")
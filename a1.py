items=["pencil", "eraser" ,"notebook" ,"sharpener", "glue"]
stock_count=[12,0,8,5,3,]
#dictionary comprehension
inventory={item:count for item,count in zip (items,stock_count)}

print(inventory)

#listcomprehension

in_stock_items=[item for item in items if inventory[item]>0]

print(f"items in stock are {in_stock_items}")

chosen_item=input("which item do you need to buy ")

if chosen_item not in inventory or inventory [chosen_item]==0:
    print("this item is out of stock")
    exit()

prices=[93,34,2,56,70,200]
markup=int(input("Enter the amount you want to add to prices"))

marked_up_prices=list(map(lambda p:p+markup,prices))
print(f"The marked up prices are {marked_up_prices}")

item_index = items.index(chosen_item)
chosen_price=marked_up_prices[item_index]
print(f"the price of {chosen_item} after markup is {chosen_price}")


inventory[chosen_item]=inventory[chosen_item]-1
print(f"{chosen_item} purchased , remaining stock is {inventory[chosen_item]}")
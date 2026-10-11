items=["pencil", "eraser" ,"notebook" ,"sharpener", "glue"]
stock_count=[12,0,8,5,3,]
#dictionary comprehension
inventory={item:count for item,count in zip (items,stock_count)}

print(inventory)

#listcomprehension

in_stock_items=[item for item in items if inventory[item]>0]

print(f"items in stock are {in_stock_items}")
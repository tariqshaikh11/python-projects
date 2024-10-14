menu = {
    'pizza' : 100,
    'pasta' : 150,
    'burger' : 180,
    'salad' : 100,
    'coffe' : 200,
}
print("Welcome To Tariq's Cafe")
print("What You Woould To Order ")
print(" pizza : 100 \n pasta : 150 \n burger : 180 \n salad : 100 \n coffe : 200")
order_total=0
item1=input("Enter a item name you want to order::")
if item1 in menu:
    order_total += menu[item1]
    print("Your Order is "+item1+" has been added to order")
else:
    print(item1,"is not available in menu.please order somthing else we can serve you::")

another_order= input("DO You Want to order onother item (Yes/no)")
if another_order == 'yes':
    item2 = input("Enter The Name of second item::")
    if item2 in menu:
        order_total += menu[item2]
        print("your order "+item2+"is added")
    else:
        print(item2,"this item is not avialabe")

print("you ordered "+item1+"and"+item2+"and Your total is"+str(order_total))

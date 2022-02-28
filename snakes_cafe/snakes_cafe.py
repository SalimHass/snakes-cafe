print("""
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
""")
print("""
Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************
""")
food_list=["Wings","Cookies","Spring Rolls","Salmon","Steak","Meat Tornado","A Literal Garden","Ice Cream","Cake","Pie","Coffee","Tea","Unicorn Tears"]
order_list={}
def order_fun():
    order=input("> ")
    while order != "quit":
        if order in food_list:
            if order not in order_list:
                order_list[order]= 1
                print(f"** 1 order of {order} have been added to your meal **")

            else :
                order_list[order]+=1
                print(f"** {order_list[order]} order of {order} have been added to your meal **")
        else:
            print("we will check with the chef..")
        order=input("> ")

    print("thanks for your visit")


order_fun()

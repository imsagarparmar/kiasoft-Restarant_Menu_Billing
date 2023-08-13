import sys

print("""
█▄▀ █ ▄▀█ █▀ █▀█ █▀▀ ▀█▀
█░█ █ █▀█ ▄█ █▄█ █▀░ ░█░

█▀█ █▀▀ █▀ ▀█▀ ▄▀█ █░█ █▀█ ▄▀█ █▄░█ ▀█▀
█▀▄ ██▄ ▄█ ░█░ █▀█ █▄█ █▀▄ █▀█ █░▀█ ░█░
""")
print ("""
- - - - - - - - - - - - - - - - - - - - - - - - - -  - - -

░░ ▒█▀▄▀█ ▒█▀▀▀ ▒█▄░▒█ ▒█░▒█ 　 ▒█▀▀█ ░█▀▀█ ▒█▀▀█ ▒█▀▀▄ ░░ 
▀▀ ▒█▒█▒█ ▒█▀▀▀ ▒█▒█▒█ ▒█░▒█ 　 ▒█░░░ ▒█▄▄█ ▒█▄▄▀ ▒█░▒█ ▀▀ 
░░ ▒█░░▒█ ▒█▄▄▄ ▒█░░▀█ ░▀▄▄▀ 　 ▒█▄▄█ ▒█░▒█ ▒█░▒█ ▒█▄▄▀ ░░
- - - - - - - - - - - - - - - - - - - - - - - - - -  - - -
"""
)
lst_choice = []
lst_qty = []
menu = {
    1:'GUJARATI DISH', 
    2:'PUNJABI DISH', 
    3:'SOUTH INDIAN DISH', 
    4:'COLD DRINKS'
}
price = {
    1:150, 
    2:160, 
    3:120, 
    4:40
}

while(1):
    print('''1: GUJARATI DISH\t Rs.150 / plate 
    \n2: PUNJABI DISH\t Rs.160/plate 
    \n3: MASALA DOSA & IDALI SAMBHAR\t Rs.120/plat  e 
    \n4: CHAS Rs.40/serving
''')
    try:
        a = input('You want to place an order? (y/n) : ')

    except:
        print("Oops!",sys.exc_info()[0],"occured.")
        continue

    if(a == 'y' or a == 'Y'):
        try:
            choice = int(input('Enter choice'))

        except:
            print("Oops!",sys.exc_info()[0],"occured.")
            continue
        
        if(choice >= 1 and choice <= 4):
            try:
                qty = int(input('How much qty do you need:'))

            except:
                print("Oops!",sys.exc_info()[0],"occured.")
                continue
            
            if(qty >= 1):
                lst_choice.append(choice)
                lst_qty.append(qty)
                print('\n')
                
            else:
                print('Wrong Input \n')
                continue
            
        else:
            print('Wrong Input \n')
            continue

    elif(a == 'n' or a == 'N'):
        print('\n\nBILL:')
        total = 0
        length = len(lst_choice)
        
        for i in range(0, length):
            val = lst_choice[i]
            print(menu[val])
            print('Qty: ', lst_qty[i])
            print('Rs.', price[val], 'per unit')
            print('\n')
            total = total + (price[val] * lst_qty[i])
            
        print('total = Rs.', total)
        print('Thank you')
        break

    else:
        print("Wrong input \n")
        continue
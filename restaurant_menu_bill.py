print("""
                █▄▀ █ ▄▀█ █▀ █▀█ █▀▀ ▀█▀
                █░█ █ █▀█ ▄█ █▄█ █▀░ ░█░

        █▀█ █▀▀ █▀ ▀█▀ ▄▀█ █░█ █▀█ ▄▀█ █▄░█ ▀█▀
        █▀▄ ██▄ ▄█ ░█░ █▀█ █▄█ █▀▄ █▀█ █░▀█ ░█░""")

menu = {
    1:'GUJARATI DISH    ', 
    2:'PUNJABI DISH     ', 
    3:'SOUTH INDIAN DISH', 
    4:'COLD DRINKS      '
}
price = {
    1:150, 
    2:160, 
    3:120, 
    4:40
}
lst_cname=[]
lst_choice=[]
lst_qty=[]
print(".........................................")
cname = input('Enter Customer Name : ')
print(".........................................")

while True:
    print ("""
==================================================================
    ░░ ▒█▀▄▀█ ▒█▀▀▀ ▒█▄░▒█ ▒█░▒█  ▒█▀▀█ ░█▀▀█ ▒█▀▀█ ▒█▀▀▄ ░░ 
    ▀▀ ▒█▒█▒█ ▒█▀▀▀ ▒█▒█▒█ ▒█░▒█  ▒█░░░ ▒█▄▄█ ▒█▄▄▀ ▒█░▒█ ▀▀ 
    ░░ ▒█░░▒█ ▒█▄▄▄ ▒█░░▀█ ░▀▄▄▀  ▒█▄▄█ ▒█░▒█ ▒█░▒█ ▒█▄▄▀ ░░
=================================================================="""
    )
    print('''
    - + - + - + - + - + - + - + - + - + - + - + - + - + - + - + -
    Item Code           Food Item                   Price
    - + - + - + - + - + - + - + - + - + - + - + - + - + - + - + -
        1             GUJARATI DISH              ₹.150 / plate 
    -------------------------------------------------------------
        2              PUNJABI DISH              ₹.160 / plate 
    -------------------------------------------------------------
        3             SOUTH INDIAN DISH          ₹.120 / plate 
                (MASALA DOSA & IDALI SAMBHAR)
    -------------------------------------------------------------
        4                  CHAS                  ₹.40 / serving
    -------------------------------------------------------------
''')
    try:
        order = input('You want to place an order? (y/n) : ')
    except:
        print("Please Enter Correct choice Yes for n & No for n")
    if(order == 'y' or order == 'Y'):
        try:
            print(".........................................")
            choice = eval(input('Enter Food Item Code : '))
            print(".........................................")
        except:
            print("Please Enter Correct choice Yes for n & No for n")
            continue    
        if(choice >= 1 and choice <= 4):
            try:
                qty = int(input('Please Enter Food Quantity : '))
            except:
                print("Please Enter Correct Quantity")
                continue
            if(qty >= 1):
                lst_cname.append(cname)
                lst_choice.append(choice)
                lst_qty.append(qty)
                print('\n')         
            else:
                print('Incorrect Entered Data \n')
                continue
        else:
            print('Incorrect Entered Data \n')
            continue
    elif(order == 'n' or order == 'N'):
        print('************************************ BILL ************************************')
        print(".............................................................................")
        print('Customer Name : ', cname)
        print(".............................................................................")
        print('- + - + - + - + - + - + - + - + - + - + - + - + - + - + - + - + - + - + - + -')
        print('Food Item\t\t\t\tQTY\t\t\tPrice')
        print('- + - + - + - + - + - + - + - + - + - + - + - + - + - + - + - + - + - + - + -')
        total = 0
        length = len(lst_choice)
        for i in range(0, length):
            val = lst_choice[i]
            print('-----------------------------------------------------------------------------')
            print(f'{menu[val]}\t\t\t{lst_qty[i]}\t\t ₹.{price[val]}, Per Dish')
            print('-----------------------------------------------------------------------------')
    
            total=total+(price[val]*lst_qty[i])
            sgst=total*5/100
            cgst=total*5/100
            grand_total=total+(sgst+cgst)
        print('\t\t\t\t\t\t____________________________')
        print('\t\t\t\t\t\tTotal = ₹.', total,'/-')
        print('\t\t\t\t\t\t____________________________')
        print('\t\t\t\t\t\tSGST = ₹.', sgst,'/-')
        print('\t\t\t\t\t\t____________________________')
        print('\t\t\t\t\t\tCGST = ₹.', cgst,'/-')
        print('\t\t\t\t\t\t____________________________')
        print('\t\t\t\t\t\tGrand Total = ₹.',grand_total,'/-')
        print('\t\t\t\t\t\t____________________________')
        print('-----------------------------------------------------------------------------')
        print('\t\t\t\tThank You')
        print('-----------------------------------------------------------------------------')
        break
    else:
        print("---------------------------------")
        print("\tWrong Entry, \tTry again...")
        print("---------------------------------")
        continue

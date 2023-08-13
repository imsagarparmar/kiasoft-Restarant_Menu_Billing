print("""
                █▄▀ █ ▄▀█ █▀ █▀█ █▀▀ ▀█▀
                █░█ █ █▀█ ▄█ █▄█ █▀░ ░█░

        █▀█ █▀▀ █▀ ▀█▀ ▄▀█ █░█ █▀█ ▄▀█ █▄░█ ▀█▀
        █▀▄ ██▄ ▄█ ░█░ █▀█ █▄█ █▀▄ █▀█ █░▀█ ░█░""")

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
                print('Wrong Input \n')
                continue
        else:
            print('Wrong Input \n')
            continue
    elif(order == 'n' or order == 'N'):
        print('****************** BILL******************')
        print(".........................................")
        print('Customer Name : ', cname)
        print(".........................................")
        total = 0
        length = len(lst_choice)
        print("""- + - + - + - + - + - + - + - + - + - + - + - + - + - + - + -
                Food Item                           QTY               Price
        - + - + - + - + - + - + - + - + - + - + - + - + - + - + - + -""")
        for i in range(0, length):
            val = lst_choice[i]
            print(f'''
    -------------------------------------------------------------
    {menu[val]}                    {lst_qty[i]}  ₹.{price[val]}, per unit")
    -------------------------------------------------------------
    ''')
            total = total + (price[val] * lst_qty[i])
            
        print('total = Rs.', total)
        print('Thank you')
        break
    else:
        print("---------------------------------")
        print("\tWrong Entry \n \tTry again...")
        print("---------------------------------")
        continue

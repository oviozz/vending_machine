#prints intro ---------------------------------
print('Welcome to the vending machine change maker program')
print('Change maker initialized.')
print('Stock contains:')


# storing coins and the value using dictionary
store = {'nickels': 25,
         'dimes': 25,
         'quarters': 25,
         'ones': 0,
         'fives': 0}

# looping through each item in the dictionary and printing it
for name, coin in store.items():
    print(f'  {coin} {name}')

# user input
purchase_price = input("\nEnter the purchase price (xx.xx) or `q' to quit: ")
user_money_deposit = 0

# the loop runs till the user_input (purchase_price) == q
while purchase_price != 'q':

    if purchase_price == 'q':
        exit()

    #checks if the input is multiple of .05 using string ( checks for the end letter of the inputs to check if it's multiple of 5 or 10 )
    while purchase_price[-1] != '5' and purchase_price[-1] != '0':
        print('Illegal price: Must be a non-negative multiple of 5 cents.')
        purchase_price = input("\nEnter the purchase price (xx.xx) or `q' to quit: ")
        # exist if user == q
        if purchase_price == 'q':
            exit()

    print('Menu for deposits:')


    menu_deposits = {'n': 'deposit a nickel',
                     'd': 'deposit a dime',
                     'q': 'deposit a quarter',
                     'o': 'deposit a one dollor bill',
                     'f': 'deposit a five dollor bill',
                     'c': 'cancel the purchase'
                     }
    # loop through menu_depisit and prints out both key,value (symbol, explain)
    for symbol, explain in menu_deposits.items():  # prints menu_deposit in format
        print(f"  '{symbol}' -  {explain}")
    print()

    # this function formats the input ( example: $3.15 == 3 Dollor and 15 cents ) ( .05 == 5 cents )
    def purchase_price_checker(checker):  # formats the changes

        # checks if the input is below 0 and above -1
        if float(checker) < 0:
            if float(checker) < 0 and float(checker) > -1:
                return f'Payment due: -{abs(float(checker))}'


            else:
                # checks if the value has . from index 1 and if 0. is not in the input
                # if so it returns (Payment due: X dollors and X cents)
                if '.' in checker[1:] and '0.' not in checker:
                    index_of_dot = checker.index('.')
                    return (f"Payment due: {int(float(checker) // 1)} dollors and {checker[index_of_dot + 1:].lstrip('0')} cents")

                # checks if the input start with . or if the first two character == 0. if so it returns (Payment due: X cents)
                elif checker[0] == '.' or checker[0:2] == '0.':
                    return (f'Payment due: {int(float(checker) * 100)} cents')

                # anything else it returns ( Payment due: X dollor and 0 cents )
                else:
                    return (f'Payment due: {int(float(checker))} dollors and 0 cents')


        # same function as above but this only runs if the input is less than 0
        else:
            if '.' in checker[1:] and '0.' not in checker:
                index_of_dot = checker.index('.')
                return (
                    f"Payment due: {int(float(checker))} dollors and {checker[index_of_dot + 1:].lstrip('0')} cents")


            elif checker[0] == '.' or checker[0:2] == '0.':
                return (f'Payment due: {int(float(checker) * 100)} cents')

            else:
                return (f'Payment due: {int(float(checker))} dollors and 0 cents')


    print(purchase_price_checker(purchase_price))

    user_money_deposit = 0

    deposit_sign = input('Indicate your deposit: ').lower() # -> .lower() turns the input into lower case

    log_deposit_sign = []
    # the loop checks and run till the deposit_sign == only of these [ n, d, q, o, f, c]
    while deposit_sign not in menu_deposits.keys():
        print(purchase_price_checker(purchase_price))
        print(f'Illegal selection: {deposit_sign}')
        deposit_sign = input('Indicate your deposit: ').lower()

    # loops runs till the input == c
    while deposit_sign != 'c':

        # the loop checks and run till the deposit_sign == only of these [ n, d, q, o, f, c]
        while deposit_sign not in menu_deposits.keys():
            print(f'Illegal selection: {deposit_sign}')
            deposit_sign = input('Indicate your deposit: ').lower()

        purchase_price = float(purchase_price)
        # checks if input == n
        if deposit_sign == 'n':
            purchase_price = round(purchase_price - 0.05, 2) # rounds the value to 2 signifi
            user_money_deposit += 0.05 # collects chages
            store['nickels'] += 1

            print(purchase_price_checker(str(purchase_price)))

            if purchase_price == 0: # if it == 0 it will assume there's no more money due so it will break
                break

            deposit_sign = input('Indicate your deposit: ').lower()
        
        # checks if the input == n
        elif deposit_sign == 'd':
            purchase_price = round(purchase_price - 0.10, 2)
            user_money_deposit += 0.10
            store['dimes'] += 1
            
            #checks if the value is less than 0
            if purchase_price < 0:
                break
            print(purchase_price_checker(str(purchase_price)))
            
            # for each it will check if it == 0 it will assume there's no more money due so it will break
            if purchase_price == 0:
                break

            deposit_sign = input('Indicate your deposit: ').lower()

        elif deposit_sign == 'q':
            log_deposit_sign.append('q')
            purchase_price = round(purchase_price - 0.25, 2)
            user_money_deposit += 0.25
            store['quarters'] += 1

            if purchase_price < 0:
                break
            print(purchase_price_checker(str(purchase_price)))

            if purchase_price == 0.0:
                break

            deposit_sign = input('Indicate your deposit: ').lower()

        elif deposit_sign == 'o':
            purchase_price = round(purchase_price - 1.00, 2)  # need to fix this
            user_money_deposit += 1.00
            store['ones'] += 1

            if purchase_price < 0:
                break
            print(purchase_price_checker(str(purchase_price)))

            if purchase_price == 0:
                break

            deposit_sign = input('Indicate your deposit: ').lower()

        elif deposit_sign == 'f':
            purchase_price = round(purchase_price - 5.00, 2)
            user_money_deposit += 5.00
            store['fives'] += 1

            if purchase_price < 0:
                break
            print(purchase_price_checker(str(purchase_price)))

            if purchase_price == 0:
                break

            deposit_sign = input('Indicate your deposit: ').lower()

        if (float(purchase_price)) <= 0:  # add int if not working
            break

    # calcualues the number of change needed to equal the due value
    def coin_change(store_value_credit):
        coin_types = [5, 10, 25] # different kind of change -> to make it easier I used 5,10,25 
        length_of_coin = len(coin_types)   # checks for the length of the list [ 3 ] 

        result_hold = []

        collect = length_of_coin - 1
        
        #loops runs till the length - 1 > 0: 
        while collect >= 0:
            
            # will loop till it appends the change to match with the input_value 
            while store_value_credit >= coin_types[collect]:
                store_value_credit -= coin_types[collect]
                result_hold.append(coin_types[collect])

            collect -= 1

        # Print result
        return result_hold

    # calacutes the values to coin/cents format
    #checks if it's less than 0 if so it will call using purchase_price (input)
    if purchase_price < 0:
        nickle = coin_change(abs(purchase_price) * 100).count(5) # -> counts how many 5 is in the list 
        dime = coin_change(abs(purchase_price) * 100).count(10) # -> counts how many 10 is in the list 
        quarter = coin_change(abs(purchase_price) * 100).count(25) # -> counts how many 25 is in the list 

    # if not it will call user_money_deposit to coin_change function
    else:
        nickle = coin_change(abs(user_money_deposit) * 100).count(5)  # -> counts how many 5 is in the list 
        dime = coin_change(abs(user_money_deposit) * 100).count(10) # -> counts how many 10 is in the list 
        quarter = coin_change(abs(user_money_deposit) * 100).count(25) # -> counts how many 25 is in the list 

    total_store_refund = 0
    
    # checks if deposit_sign == c in which case it will check if the purcahse_price is greator than 0 meaning it will have change remaning
    if deposit_sign == 'c':
        if float(purchase_price) > 0:
            print("\nPlease take the change below.")

        if quarter > 0: 
            store['quarters'] -= quarter # after using the change it will call in the dictionary and deduct the number of change used
            if store['quarters'] < 0:
                store['quarters'] = 0
                total_store_refund += quarter * 0.25 # convert it into coin/cents fromat ( float) 
            else:
                print(f'   {quarter} quarters')

        if dime > 0:
            store['dimes'] -= dime # deducts the coin change
            if store['dimes'] < 0:
                store['dimes'] = 0
                total_store_refund += dime * 0.10
            else:
                print(f'   {dime} dimes')

        if nickle > 0:
            store['nickels'] -= nickle # deducts the coin change
            if store['nickels'] < 0:
                store['nickels'] = 0
                total_store_refund += nickle * 0.05
            else:
                print(f'   {nickle} nickels')

        # checks if the coin_store value is 0 if so it will return no more change left 
        if store['quarters'] == 0 or store['nickels'] == 0 or store['dimes'] == 0:
            print('\nMachine is out of change.\nSee store manager for remaining refund.')
            print(f'Amount due is: {int(total_store_refund)} dollors and {int(round(total_store_refund % 1, 2) * 100)} cents')

    # if the purchase_price is 0 it will assume there's no change due
    if purchase_price == 0:
        print("\nPlease take the change below.\n   No change due.")

    if purchase_price < 0:
        print("\nPlease take the change below.")

        if quarter > 0:
            store['quarters'] -= quarter
            if store['quarters'] < 0:
                store['quarters'] = 0
                total_store_refund += quarter * 0.25
            else:
                print(f'   {quarter} quarters')

        if dime > 0:
            store['dimes'] -= dime
            if store['dimes'] < 0:
                store['dimes'] = 0
                total_store_refund += dime * 0.10
            else:
                print(f'   {dime} dimes')

        if nickle > 0:
            store['nickels'] -= nickle
            if store['nickels'] < 0:
                store['nickels'] = 0
                total_store_refund += nickle * 0.05
            else:
                print(f'   {nickle} nickels')

        if store['quarters'] == 0 or store['nickels'] == 0 or store['dimes'] == 0:
            print('\nMachine is out of change.\nSee store manager for remaining refund.')
            print(f'Amount due is: {int(total_store_refund)} dollors and {int(round(total_store_refund % 1, 2) * 100)} cents')

    # loops over the dictionary and prints out the values
    print('\nStock contains:')
    for name, coin in store.items():
        print(f'  {coin} {name}')

    purchase_price = input("\nEnter the purchase price (xx.xx) or `q' to quit: ")


print(f'Total: {int(user_money_deposit)} dollors and {int(round(user_money_deposit % 1,2) * 100)} cents')

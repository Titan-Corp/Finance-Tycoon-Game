#    *DISCLAIMER THIS IS NOT THE MOST CURRENT VERSION OF THE CODE!!!*
# 2+2=4

from time import time
import random

#starting stuff
cash = 100.00
money_per_sec = .10
Amazon = round(random.uniform(0.00, 1000.00), 2)
stock_in_amazon = 0
WallMart = round(random.uniform(0.00, 75.00), 2)
stock_in_wallmart = 0
Microsoft = round(random.uniform(0.00, 500.00), 2)
stock_in_micro = 0
companies = ['Amazon', 'WallMart', 'Microsoft']

while True:
    start_time = time()
    
    user_input = input('What would you like to do? 1. Check your Money, 2. Look at the stock Market, 3. Look at the news, 4. Look at your stocks ')
#your money
    if user_input == '1':
        #updating cash and showing the user their balance
        time_passed = round(time() - start_time)
        cash += time_passed * money_per_sec
        cash = round(cash, 2)
        print(cash)

    elif user_input == '2':
        #updating the cash 
        time_passed = round(time() - start_time)
        cash += time_passed * money_per_sec
        cash = round(cash, 2)
        #stock Market stuff

        print("Some stocks that are out right now: ")
        print(f"1. The company Amazon has a current stock value of " + str(Amazon) )
        print(f"2. The company WallMart has a current stock value of {WallMart}")
        print(f"3. The company Microsoft has a current stock value of {Microsoft}")
        invest = input('Would you like to invest? y/n ')
        if invest == 'y':
            company = input("What company would you like to invest in? ")
            #stock Amazon
            if company == '1':
                buy_or_no = input(f"Would You Like to Buy a Amazon Stock for {Amazon} y/n: ")
                #can you afford 
                
                if buy_or_no == 'y':
                    if cash > Amazon:
                        many = int(input("How many Amazon stocks would you like to buy? "))
                        if many * Amazon <= cash:
                            cash -= Amazon * many
                            stock_in_amazon += many
                        elif many * Amazon > cash:
                            print("You can't afford that many Amazon Stocks")
                        else:
                            print(SyntaxError)
                        
                    else:
                        print(' you can\'t afford one right now! ')
                elif buy_or_no == 'n':
                    print('You did not buy a Amazon Stock ')
                else:
                    print('error, you will not get the stock right now, try again')
            #stock Wallmart
            elif company == '2':
                buy_or_no = input(f"Would You Like to Buy a WallMart Stock for {WallMart} y/n: ")
                if buy_or_no == 'y' or 'yes':
                    if cash > WallMart:
                        many = int(input("How many WallMart stocks would you like to buy? "))
                        if many * WallMart <= cash:
                            cash -= WallMart * many
                            stock_in_wallmart += many
                        elif many * WallMart > cash:
                            print("You can't afford that many WallMart Stocks")
                        else:
                            print(SyntaxError)
                elif buy_or_no == 'n' or 'no':
                    print('You did not buy a WallMart Stock')
                else:
                    print('error, you will not get the stock right now, try again')
            elif company == 'placeholder':
                buy_or_no = input(f"Would You Like to Buy a Microsoft Stock for {Microsoft} y/n: ")
                if buy_or_no == 'y' or 'yes':
                    if cash > Microsoft:
                        many = int(input("How many Microsoft stocks would you like to buy? "))
                        if many * Microsoft <= cash:
                            cash -= Microsoft * many
                            stock_in_micro += many
                        elif many * Microsoft > cash:
                            print("You can't afford that many Microsoft Stocks")
                        else:
                            print(SyntaxError)
                elif buy_or_no == 'n' or 'no':
                    print('You did not buy a Microsoft Stock')
                else:
                    print('error, you will not get the stock right now, try again')
            else:
                print('error')
        #nothing happens
        else:
            print('Just looking today I see.')
            
    #looking a news code
    elif user_input == "3":
        news = random.choice(companies)
        selection = random.randint(1,5)
        #good
        if selection == 1:
            print(f'You see the news, looks like the company {news} has Released a new product that is going well!')
            #making money
            if news == 'Amazon':
                Amazon += 1.50
            elif news == 'WallMart':
                WallMart += 1.50
            elif news == 'Microsoft':
                Microsoft += 1.50
            else:
                print(SyntaxError)   
        #really good
        elif selection == 2:
            print(f'You see the news, looks like the company {news} has a released a new product that is going really well!')
            if news == 'Amazon':
                Amazon += 10
            elif news == 'WallMart':
                WallMart += 10
            elif news == 'Microsoft':
                Microsoft += 10
            else:
                print(SyntaxError)
        #nothing happens
        elif selection == 3:
            print('you see the news, nothing is happening')
        #bad
        elif selection == 4:
            print(f'you see the news, looks like the company {news} is loosing money on some projects')
            if news == 'Amazon':
                Amazon -= 1.50
            elif news == 'WallMart':
                WallMart -= 1.50
            elif news == 'Microsoft':
                Microsoft -= 1.50
            else:
                print(SyntaxError)
        #really bad
        elif selection == 5:
            print(f'you see the news, looks like the company {news} has workers on strike!')
            if news == 'Amazon':
                Amazon -= 10.50
            elif news == 'WallMart':
                WallMart -= 10.50
            elif news == 'Microsoft':
                Microsoft -= 10.50
            else:
                print(SyntaxError)
        else:
            print(SyntaxError)
    #look at your stocks
    elif user_input == "4":
        print(f"You have {stock_in_wallmart} stocks in WallMart worth " + str(stock_in_wallmart * WallMart))
        print(f"You have {stock_in_amazon} stocks in Amazon worth " + str(stock_in_amazon * Amazon))
        print(f"You have {stock_in_micro} stocks in Microsoft worth" + str(stock_in_micro * Microsoft))
        
        total = stock_in_wallmart * WallMart + stock_in_amazon * Amazon + stock_in_micro * Microsoft
        
        print(f"your total stock portfolio value is {total}")
        sell = input("would you like to sell any stock? y/n ")
        if sell == 'y':
            whichOne = input('You can sell, 1. WallMart or 2. Amazon or 3. Microsoft: ')
            #wallamrt
            if whichOne == '1':
                print("how many do you want to sell?")
                how_many = int(input())
                if how_many > stock_in_wallmart:
                    print('You don\'t have that many stocks in WallMart!')
                elif how_many <= stock_in_wallmart:
                    print(f"you sold {how_many} stocks WallMart")
                    cash += how_many * WallMart
                    stock_in_wallmart -= how_many
                else:
                    print(SyntaxError)
            #amazon       
            elif whichOne == '2':
                print("how many do you want to sell?")
                how_many = int(input())
                if how_many > stock_in_amazon:
                    print('You don\'t have that many stocks in Amazon!')
                elif how_many <= stock_in_amazon:
                    print(f"you sold {how_many} stocks Amazon")
                    cash += how_many * Amazon
                    stock_in_amazon -= how_many
                else:
                    print(SyntaxError)
            elif whichOne == "3":
                print("how many do you want to sell?")
                how_many = int(input())
                if how_many > stock_in_micro:
                    print('You don\'t have that many stocks in Microsoft!')
                elif how_many <= stock_in_micro:
                    print(f"you sold {how_many} stocks Microsoft")
                    cash += how_many * Microsoft
                    stock_in_micro -= how_many
                else:
                    print(SyntaxError)
        elif sell == 'n':
            print()
        else:
            print(SyntaxError)
    else:
        print('error, try again')
        

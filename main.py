"""current goals include: 
1. create a variable that can increase in the backgound while other things happen DONE
2. create an investing system for stock
3. allow players to buy things, like houses and cars and stuff
4. allow player to use things like crypto in a fluctuating market.
5.  
"""

from time import time
import random
#starting stuff
cash = .10
money_per_sec = .10
test_stock = random.randfloat(0.00 - 100.00)


while True:
    start_time = time()
    
    user_input = input('What would you like to do? 1. Check your Money, 2. Look at the stock Market, 3. Look at crypto markets ')

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
        print("The company Test_Stock has a current stock value of " + str(test_stock) )

    else:
        print('error')

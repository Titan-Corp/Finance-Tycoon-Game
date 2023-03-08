from time import time

coins = .10
money_per_sec = .01

while True:
    start_time = time()
    
    input('Check Shop')
    time_passed = round(time() - start_time)
    
    coins += time_passed * money_per_sec
    coins = round(coins, 2)
    
    
    print(coins)
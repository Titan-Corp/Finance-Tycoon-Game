class Company:
    '''Create a company that can hold stocks'''
    
    def __init__(self, name:str, base_stock_price:float):
        self.name = name
        self.stock_price = base_stock_price
        self.stocks = 0
        
    def update_stocks(self, change_amount:float):
        '''Update Stocks by a float 
        (1 stays the same, .5 is a reduction by half, etc)'''
        
        self.stock_price *= change_amount
    
    def buy_stocks(self, update_stocks:int):
        '''Update Stocks to buy or sell them'''
        self.stocks += update_stocks

# List of Companies. Each List item is a list
companies = [Company('Amazon', 500), Company('Walmart', 5)]

companies[0].update_stocks(1.2) # Update Amazon Stocks by 120%
companies[1].update_stocks(0.85) # Update Walmart Stocks by 85%

companies[0].buy_stocks(5) # Buy 5 Stocks in Amazon

# Prints Each Companies Stock Price
for x in companies:
    print(x.stock_price)
    
# Prints Stocks In Each Company
for x in companies:
    print(x.stocks)

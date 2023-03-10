class Company:
    '''Create a company that can hold stocks'''
    
    def __init__(self, name:str, base_stock_price:float):
        self.name = name
        self.stock_price = base_stock_price
        
    def update_stocks(self, change_amount:float):
        '''Update Stocks by a float 
        (1 stays the same, .5 is a reduction by half, etc)'''
        
        self.stock_price *= change_amount

# List of Companies. Each List item is a list
companies = [Company('Amazon', 500), Company('Walmart', 5)]
companies[0].update_stocks(1.2) # Update Amazon Stocks by 120%
companies[1].update_stocks(0.85) # Update Walmart Stocks by 85%

# Prints Each Companies Stock
for x in companies:
    print(x.stock_price)
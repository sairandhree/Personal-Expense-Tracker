class Expense:
    def __init__(self, desc, category, amount, date):
        self.desc = desc
        self.category = category
        self.amount = amount
        self.date = date

    
    # def __str__(self):
    #     return "<Expense: {self.name}, {self.category}, ${self.amount:.2f} >"
    def __repr__(self):
         return f"{{'date': {self.date}, 'category': {self.category}, 'amount':{self.amount}, 'description':{self.desc} }}"
    

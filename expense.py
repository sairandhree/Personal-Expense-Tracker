class Expense:
    def __init__(self, name, category, amount):
        self.name = name
        self.category = category
        self.amount = amount
    
    # def __str__(self):
    #     return "<Expense: {self.name}, {self.category}, ${self.amount:.2f} >"
    def __repr__(self):
         return "{self.name}, {self.category}, ${self.amount:.2f}"
    
